import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

def extrair_noticias_g1():
    url = "https://g1.globo.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    manchetes = []
    
    try:
        print("Iniciando extração de notícias do G1...")
        print("Conectando ao site...")
        
        resposta = requests.get(url, headers=headers, timeout=15)
        resposta.raise_for_status()
        
        print("Conexão estabelecida com sucesso")
        print("Processando HTML...")
        
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        
        seletores_noticias = [
            '.feed-post-body',
            '.bastian-feed-item', 
            '.widget--info__text-container',
        ]
        
        print("Buscando notícias...")
        
        for seletor in seletores_noticias:
            elementos = sopa.select(seletor)
            if elementos:
                print(f"Encontrados {len(elementos)} elementos com seletor: {seletor}")
                for elemento in elementos:
                    try:
                        titulo_element = elemento.select_one('.feed-post-body-title, .feed-post-link, a')
                        titulo = titulo_element.get_text(strip=True) if titulo_element else None
                        
                        link_element = elemento.select_one('a')
                        link = link_element.get('href') if link_element else None
                        
                        if link and not link.startswith('http'):
                            link = 'https://g1.globo.com' + link
                        elif link and link.startswith('//'):
                            link = 'https:' + link
                        
                        resumo_element = elemento.select_one('.feed-post-body-resumo, .bstn-relatedtext')
                        resumo = resumo_element.get_text(strip=True) if resumo_element else "Resumo não disponível"
                        
                        if titulo and link and len(titulo) > 10:
                            manchetes.append({
                                'titulo': titulo,
                                'link': link,
                                'resumo': resumo,
                                'data_extracao': datetime.now().isoformat(),
                                'site': 'G1'
                            })
                            
                    except:
                        continue
        
        if len(manchetes) < 3:
            print("Poucas notícias encontradas. Buscando método alternativo...")
            links_noticias = sopa.find_all('a', href=True)
            
            for link in links_noticias:
                try:
                    href = link.get('href')
                    titulo = link.get_text(strip=True)
                    
                    if (href and titulo and len(titulo) > 20 and 
                        ('noticia' in href or '/g1/' in href or '.html' in href)):
                        
                        if not href.startswith('http'):
                            href = 'https://g1.globo.com' + href
                        elif href.startswith('//'):
                            href = 'https:' + href
                        
                        resumo = "Resumo não disponível"
                        parent = link.parent
                        if parent:
                            resumo_element = parent.find_next_sibling('p')
                            if resumo_element:
                                resumo = resumo_element.get_text(strip=True)[:150] + "..."
                        
                        manchetes.append({
                            'titulo': titulo,
                            'link': href,
                            'resumo': resumo,
                            'data_extracao': datetime.now().isoformat(),
                            'site': 'G1'
                        })
                        
                except:
                    continue
        
        # Remove duplicados
        manchetes_unicas = []
        links_vistos = set()
        
        for noticia in manchetes:
            if noticia['link'] not in links_vistos:
                manchetes_unicas.append(noticia)
                links_vistos.add(noticia['link'])
        
        print(f"Extracao concluida. {len(manchetes_unicas)} noticias encontradas.")
        return manchetes_unicas
        
    except Exception as e:
        print(f"Erro durante a extracao: {e}")
        return []

def main():
    print("=" * 50)
    print("Extrator de Noticias - G1")
    print("=" * 50)
    
    inicio = time.time()
    manchetes = extrair_noticias_g1()
    fim = time.time()
    
    if manchetes:
        output_path = "manchetes.json"
        print("Salvando dados no arquivo manchetes.json...")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(manchetes, f, ensure_ascii=False, indent=2)
        
        tempo_decorrido = fim - inicio
        print(f"Processo concluido com sucesso!")
        print(f"Noticias salvas: {len(manchetes)}")
        print(f"Tempo de execucao: {tempo_decorrido:.2f} segundos")
        print(f"Arquivo salvo em: {output_path}")
    else:
        print("Nenhuma noticia foi encontrada. Verifique a conexao com a internet.")

if __name__ == "__main__":
    main()