import bs4

class Geladeira:
    def __init__(this,nome,nota,preco):
        this.nome =nome
        this.nota = nota 
        this.preco = preco 
    def __str__(this):
        return f"Nome:{this.nome} \nNota:{this.nota}\nPreço:R$ {this.preco}"
    
def procurar_produtos() -> list[Geladeira]:
    """Método de exemplo para interagir com o HTML da página do e-commerce"""
    geladeiras = []
    # Carrega o arquivo HTML com a codificação correta
    with open("C:/Users/Duhor/desafio/page/revio-e-commerce.html", encoding='utf-8') as html_pagina:
        # Parseia o arquivo
        soup = bs4.BeautifulSoup(html_pagina, "html.parser")

    # Captura o grid HTML com todos os produtos
    grid_de_produtos = soup.find("div", class_="products-grid")

    # Cria uma lista apenas com HTML específico dos produtos
    produtos = grid_de_produtos.find_all("div", attrs={"class": "product-card"})
    produtos_valores = grid_de_produtos.find_all("div",attrs={"class":"price"})
    produtos_nota = grid_de_produtos.find_all("div",attrs={"class":"rating"})
    # Cria uma lista apenas com o atributo do nome dos produtos
    for i in range(len(produtos)):
        nomes_de_produtos = produtos[i].find("h3").text 
        valores_produtos = produtos_valores[i].find("span", attrs={"class": "current-price"}).text 
        valores_produtos=valores_produtos.replace(".","")
        valores_produtos=valores_produtos.replace(",",".")
        valores_produtos=valores_produtos.replace("R$ ","")
        preco_float = float(valores_produtos)
        nota_produtos = produtos_nota[i].find("span",attrs={"class":"rating-value"}).text 
        nota_float=float(nota_produtos)
       
        geladeira = Geladeira(nomes_de_produtos,nota_float,preco_float)
        geladeiras.append(geladeira)
    return geladeiras

                       
            
                
