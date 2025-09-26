# README - Extrator de Biografia Instagram 📲

## 📋 Descrição
---
Este projeto utiliza **Python** e **Selenium** para automatizar o login no Instagram e extrair a bio de um perfil específico, salvando os dados em um arquivo JSON.  
---

## ⚙️ Configuração

1.  **Crie um arquivo `.env`** na pasta `projeto_bot/src/` 

2.  **Adicione suas credenciais** de login do Instagram ao arquivo `.env`:
    ```
    INSTAGRAM_USERNAME="seu_usuario"
    INSTAGRAM_PASSWORD="sua_senha"
    ```
> **Importante**: O arquivo `.env` contém informações sensíveis e não deve ser versionado (já está no `.gitignore` do projeto).

---

## 🛠 Funcionalidades

    - Acessa o Instagram e realiza login automático;
    - Navega até o perfil desejado;
    - Extrai a biografia do perfil;
    - Salva os dados em um arquivo JSON (`bio_instagram.json`). 

---

## 📋 Instruções para Executar
    🔧 Instalar Dependências:
    ```
    pip install selenium

    pip install webdriver-manager

    pip install python-dotenv
    ````
    🚀 Executar o Script:
    ````
    cd projeto_bot

    cd src

    python bot_instagram.py
    ````

## 📦 Pré requisitos:
    - Python 3.8 ou superior
    - Google Chrome instalado
    - Acesso à internet 

## 📊 Exemplo de Saída JSON:

````
{
  "perfil": "computacaounifavip_",
  "biografia": {
    "linhas": [
      "CC e ADS - UNIFAVIP",
      "computacaounifavip_",
      "Eventos",
      "Aulas",
      "Comunicados",
      "Filmes e séries",
      "Time",
      "Certificações",
      "224 publicações",
      "1.503",
      "Perfil oficial dos cursos:\n👨‍💻 Ciência da Computação\n👨‍💻 Análise e Desenvolvimento de Sistemas\n📍UniFavip | Wyden"
    ],
    "texto_completo": "CC e ADS - UNIFAVIP\ncomputacaounifavip_\nEventos\nAulas\nComunicados\nFilmes e séries\nTime\nCertificações\n224 publicações\n1.503\nPerfil oficial dos cursos:\n👨‍💻 Ciência da Computação\n👨‍💻 Análise e Desenvolvimento de Sistemas\n📍UniFavip | Wyden",
    "quantidade_linhas": 11
  },
  "data_extracao": "2025-09-25 09:54:05"
}
````

## ⚙️ Funcionamento:
O script extrai automaticamente a biografia de um perfil específico do Instagram e salva em bio_instagram.json.