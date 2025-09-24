# Projetos de Automação Python 🐍

Este repositório contém dois projetos distintos de automação em **Python**, cada um com sua funcionalidade específica.  

---

## 1. Extração de Bio do Instagram com Selenium

Este projeto utiliza **Selenium** para automatizar o login no Instagram e extrair a bio de um perfil específico, salvando os dados em um arquivo JSON.  

### Funcionalidades

- Acessa o Instagram e realiza login automático.
- Lida com a tela de "Salvar informações" após o login.
- Navega até o perfil desejado.
- Extrai a bio do usuário, ignorando elementos desnecessários como botões ou contagem de seguidores.
- Salva os dados em um arquivo JSON (`bio_instagram.json`).  

### Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- Acesso à internet  

### Dependências

```bash
pip install selenium
pip install webdriver-manager
```

## Mais informações

Para instruções detalhadas de uso, exemplos e informações adicionais, consulte o README específico:  
[`Login Instagram`](bot_instagram.md)

---

## 2. Extrator de Notícias do G1 📰

Este projeto utiliza **Requests** e **BeautifulSoup** para extrair automaticamente as manchetes do portal G1 e salvar os dados em JSON.

### Funcionalidades

- Extrai título, link, resumo e data de extração das notícias.
- Salva os dados em `manchetes.json`.
- Permite analisar rapidamente as últimas notícias do portal G1.

### Dependências

```bash
pip install requests beautifulsoup4
```

### Exemplo de saída JSON

```json
[
  {
    "titulo": "Título da notícia exemplo 1",
    "link": "https://g1.globo.com/politica/noticia/2024/01/01/exemplo1.html",
    "resumo": "Resumo da notícia quando disponível...",
    "data_extracao": "2024-01-01T10:30:45.123456",
    "site": "G1"
  },
  {
    "titulo": "Título da notícia exemplo 2",
    "link": "https://g1.globo.com/economia/noticia/2024/01/01/exemplo2.html",
    "resumo": "Resumo não disponível",
    "data_extracao": "2024-01-01T10:30:45.123456",
    "site": "G1"
  }
] 
```

## Mais informações

Para instruções detalhadas de uso, exemplos e informações adicionais, consulte o README específico:
[`Extrator Notícias`](extrator_noticias.md)

##Observações Gerais
- Cada projeto é independente, podendo ser executado separadamente.

- Certifique-se de instalar as dependências específicas de cada projeto antes de executar os scripts.

- Para instruções detalhadas, exemplos de saída e informações adicionais, consulte os READMEs individuais listados acima.
