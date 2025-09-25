# Projetos de Automação Python 🐍

Este repositório abriga uma coleção de scripts de automação e web scraping desenvolvidos em **Python**. Cada projeto é focado em uma tarefa específica, desde a extração de dados de redes sociais até a coleta de notícias.

---

## 🚀 Como Executar os Projetos

A maneira mais fácil de executar os projetos é através do menu interativo. Navegue até a pasta raiz `projetos_scraper`, baixe as dependências necessárias e, em seguida, execute o `main.py`:

```bash
cd projetos_scraper
pip install -r requirements.txt
python main.py
```

O menu permitirá que você escolha qual automação deseja rodar.

---

## 🤖 Projeto 1: Extrator de Biografia do Instagram

Este bot utiliza **Selenium** para automatizar o login no Instagram, navegar até um perfil específico e extrair as informações da biografia.

### ✨ Principais Funcionalidades
- **Login Seguro**: Realiza login automático utilizando credenciais armazenadas em um arquivo `.env`.
- **Navegação Automatizada**: Acessa a página do perfil alvo.
- **Extração Inteligente**: Coleta o texto da biografia, tentando filtrar informações irrelevantes.
- **Tratamento de Pop-ups**: Lida com as caixas de diálogo de "Salvar informações" e "Ativar notificações".
- **Saída Estruturada**: Salva os dados extraídos no arquivo `bio_instagram.json`.
 
### 🛠️ Tecnologias e Dependências
- **Tecnologias**: Python, Selenium.
- **Dependências**: `selenium`, `webdriver-manager`, `python-dotenv`.

### 📖 Mais Informações
Para instruções detalhadas de configuração e uso, consulte o README específico:  
➡️ **Documentação do Bot do Instagram** 

## 📰 Projeto 2: Extrator de Notícias do G1

Este scraper utiliza **Requests** e **BeautifulSoup** para extrair as principais manchetes da página inicial do portal de notícias G1.

### ✨ Principais Funcionalidades
- **Coleta Rápida**: Acessa o G1 e extrai os dados das notícias sem a necessidade de um navegador.
- **Extração de Dados**: Captura o título, link e resumo de cada manchete.
- **Saída Organizada**: Salva a lista de notícias no arquivo `manchetes.json`.

### 🛠️ Tecnologias e Dependências
- **Tecnologias**: Python, Requests, BeautifulSoup.
- **Dependências**: `requests`, `beautifulsoup4`.

### 📖 Mais Informações
Para instruções detalhadas de uso e exemplos, consulte o README específico:
➡️ **Documentação do Extrator de Notícias**

## 📝 Observações Gerais
- Cada projeto é autocontido em sua respectiva pasta (`projeto_bot` e `projeto_noticias`).
- Antes de executar um script pela primeira vez, certifique-se de instalar suas dependências.
