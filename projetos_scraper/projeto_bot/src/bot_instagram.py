import time
import json
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def login_instagram(driver, usuario, senha):
    driver.get("https://www.instagram.com/")
    
    wait = WebDriverWait(driver, 20)
    input_user = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    input_pass = driver.find_element(By.NAME, "password")

    input_user.send_keys(usuario)
    input_pass.send_keys(senha)
    input_pass.send_keys(Keys.RETURN)

def handle_popups(driver):
    wait = WebDriverWait(driver, 15)
    try:
        save_info_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Agora não'] | //button[text()='Agora não']")))
        save_info_button.click()
    except Exception:
        pass

    try:
        notifications_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Agora não']")))
        notifications_button.click()
    except Exception:
        pass

def extract_complete_bio(driver, perfil):
    url_perfil = f"https://www.instagram.com/{perfil}/"
    driver.get(url_perfil)
    
    wait = WebDriverWait(driver, 20)
    time.sleep(5)
    
    bio_parts = []
    
    bio_selectors = [
        "//header//section/div/div/span",
        "//header//section/div/div//span",
        "//header//section//div//span",
        "//header//section//span",
    ]
    
    for selector in bio_selectors:
        try:
            bio_elements = driver.find_elements(By.XPATH, selector)
            
            for element in bio_elements:
                text = element.text.strip()
                if (text and 
                    len(text) > 1 and 
                    text not in ['Seguir', 'Message', 'Mensagem', 'Segue você'] and
                    not text.isdigit() and
                    'seguidor' not in text.lower() and
                    'publicação' not in text.lower() and
                    'seguindo' not in text.lower() and
                    text not in bio_parts):
                    
                    bio_parts.append(text)
                    
        except Exception:
            continue
    
    return bio_parts

def format_bio_for_json(bio_parts):
    if not bio_parts:
        return {"linhas": [], "texto_completo": ""}
    
    bio_structured = {
        "linhas": bio_parts,
        "texto_completo": "\n".join(bio_parts),
        "quantidade_linhas": len(bio_parts)
    }
    
    return bio_structured

def main():
    driver = setup_driver()
    load_dotenv()
    inicio = time.time()

    # Carregar variaveis de ambiente do seu .env
    usuario = os.getenv("INSTAGRAM_USERNAME")
    senha = os.getenv("INSTAGRAM_PASSWORD")
    # Modifique aqui para o perfil que deseja extrair a bio
    perfil_alvo = "computacaounifavip_"

    if not usuario or not senha:
        print("Erro: Variaveis de ambiente nao definidas.")
        return

    try:
        login_instagram(driver, usuario, senha)
        time.sleep(8)
        handle_popups(driver)
        
        bio_parts = extract_complete_bio(driver, perfil_alvo)
        bio_structured = format_bio_for_json(bio_parts)

        dados = {
            "perfil": perfil_alvo,
            "biografia": bio_structured,
            "data_extracao": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        if bio_parts:
            output_path = "bio_instagram.json"
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            
            fim = time.time()
            tempo_decorrido = fim - inicio
            
            print("Processo concluido com sucesso")
            print(f"Biografia encontrada ({len(bio_parts)} linhas):")
            for i, linha in enumerate(bio_parts, 1):
                print(f"   {i}. {linha}")
            print(f"Arquivo salvo em: {output_path}")
            print(f"Tempo de execucao: {tempo_decorrido:.2f} segundos")
        else:
            print("Nenhuma biografia foi encontrada.")

    except Exception as e:
        print(f"Erro geral: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()