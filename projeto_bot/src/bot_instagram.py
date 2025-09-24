import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do Chrome
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 1. Acessar o Instagram
    driver.get("https://www.instagram.com/")
    time.sleep(20)

    # 2. Login
    usuario = "alunounifavip_2023"
    senha = "Test@123qwe"

    input_user = driver.find_element(By.NAME, "username")
    input_pass = driver.find_element(By.NAME, "password")

    input_user.send_keys(usuario)
    input_pass.send_keys(senha)
    input_pass.send_keys(Keys.RETURN)

    time.sleep(5)

    # 3. Tratar tela "Salvar informações"
    try:
        btn_salvar = driver.find_element(By.XPATH, "//button[contains(text(),'Agora não')]")
        btn_salvar.click()
    except:
        pass
    time.sleep(20)

    # 4. Procurar pelo perfil
    driver.get("https://www.instagram.com/computacaounifavip_/")
    time.sleep(10)

    # 5. Extrair a bio
    try:
    # Espera o header carregar
        header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "header"))
        )

    # Captura todos os textos dentro do header
        texts = header.text.split("\n")

    # Filtra descartando o que não faz parte da bio
        ignorar = ["Seguindo", "Seguir", "Mensagem", "⋯", "Publicações", "seguidores", "seguindo"]
        bio_lines = [t for t in texts if all(ig.lower() not in t.lower() for ig in ignorar)]

        bio = "\n".join(bio_lines).strip()
    except Exception as e:
        bio = "Bio não encontrada."


    # 6. Salvar em JSON
    dados = {
        "perfil": "computacaounifavip_",
        "bio": bio
    }

    with open("bio_instagram.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print("Bio salva com sucesso em bio_instagram.json!")

finally:
    driver.quit()
