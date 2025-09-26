import subprocess
import sys
import os

def get_python_executable():
    return sys.executable

def run_script(script_path, working_dir):
    python_executable = get_python_executable()
    script_full_path = os.path.join(working_dir, script_path)
    
    if not os.path.exists(script_full_path):
        print(f"\nErro: O script '{script_full_path}' não foi encontrado.")
        return

    try:
        print(f"\n--- Executando '{script_path}' ---")
        subprocess.run([python_executable, script_path], check=True, cwd=working_dir)
        print(f"--- Execução de '{script_path}' concluída ---\n")
    except subprocess.CalledProcessError as e:
        print(f"\nOcorreu um erro ao executar o script: {e}")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")

def main_menu():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    news_scraper_dir = os.path.join(base_dir, "projeto_noticias", "scr")
    instagram_bot_dir = os.path.join(base_dir, "projeto_bot", "src")

    while True:
        print("=" * 50)
        print("MENU PRINCIPAL DE AUTOMAÇÕES".center(50))
        print("=" * 50)
        print("Escolha o projeto que deseja executar:")
        print("1. 📰 Extrator de Notícias do G1")
        print("2. 🤖 Bot para extrair Bio do Instagram")
        print("3. Sair")
        print("-" * 50)

        choice = input("Digite o número da sua opção: ")

        if choice == '1':
            run_script("extrator_noticias.py", news_scraper_dir)
        elif choice == '2':
            run_script("bot_instagram.py", instagram_bot_dir)
        elif choice == '3':
            print("\nSaindo do programa. Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main_menu()
