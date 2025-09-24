# Extração de Bio do Instagram com Selenium

Este projeto utiliza **Python** e **Selenium** para automatizar o login no Instagram e extrair a bio de um perfil específico, salvando os dados em um arquivo JSON.  

---

## Funcionalidades

- Acessa o Instagram e realiza login automático.
- Lida com a tela de "Salvar informações" após o login.
- Navega até o perfil desejado.
- Extrai a bio do usuário ignorando elementos desnecessários como botões ou contagem de seguidores.
- Salva os dados em um arquivo JSON (`bio_instagram.json`).  

---

## Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- Acesso à internet  

---

## Dependências

O projeto utiliza os seguintes pacotes Python:

```bash
pip install selenium
pip install webdriver-manager
```
