# README - Extrator de Notícias G1 📰

## 📋 Instruções para Executar
    🔧 Instalar Dependências:
    ```
    pip install requests beautifulsoup4
    ````
    🚀 Executar o Script:
    ````
    python noticias_g1.py
    ````

## 📦 Dependências Necessárias:
   -  requests
    beautifulsoup4

## 📊 Exemplo de Saída JSON:

````[
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
````


## ⚙️ Funcionamento:
O script extrai automaticamente as manchetes do portal G1 e salva em manchetes.json.