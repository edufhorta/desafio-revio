from fastapi import FastAPI
from fastapi import Query
import sys
sys.path.append("..")
from main import procurar_produtos

app = FastAPI()
lista_de_produtos=procurar_produtos()

@app.get("/")
def procurar_produtos_e_commerce():

    """Lista todos os produtos encontrados na página de e-commerce"""
    
    
    
    return lista_de_produtos


@app.get("/preco")
def filtrar_por_preço(min:float=Query(...,description="digite o preço minímo:"), max:float=Query(...,description="digite o preço máximo:")):
    
    lista_filtrada=[]
    for geladeira in lista_de_produtos:
        
        if min<=geladeira.preco<=max:
            
            print(geladeira.nome)
            print("")
            lista_filtrada.append(geladeira.nome)
    return lista_filtrada
@app.get("/nota")
def filtrar_por_nota(min:float=Query(...,description="digite a nota miníma:"), max:float=Query(...,description="digite a nota máxima:")):
    lista_filtrada=[]
    for geladeira in lista_de_produtos:
            
                if min<=geladeira.nota<=max:
                    print(geladeira.nome)
                    print("")
                    lista_filtrada.append(geladeira.nome)
    return lista_filtrada
@app.get("/nome")
def filtrar_por_nome(x:str=Query(...,description="digite o nome da geladeira:")):
    lista_filtrada=[]
   
    for geladeira in lista_de_produtos:
        nome_geladeira=geladeira.nome
        lista_pesquisa=x.split(" ")
        if all(palavra.upper() in nome_geladeira.upper() for palavra in lista_pesquisa):
            print(geladeira)
            print("")
            lista_filtrada.append(geladeira)
    return lista_filtrada