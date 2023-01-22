from pymongo import MongoClient

url_conexao = 'mongodb+srv://last_project_gama:gama_1234@cluster0.jruk8oe.mongodb.net/test'
conn = MongoClient(url_conexao)
collection = conn.gama.produto

def ajustar_estoque(sku, estoque, collection):
    collection.update_one({"sku":sku}, {"$set":{"estoque": estoque}})

print("Alteração de estoque:")
sku = input("Digite o sku: ")
estoque = int(input("Digite o novo estoque: "))

ajustar_estoque(sku, estoque, collection)


