from pymongo import MongoClient

def obter_colecao_mongodb(url_conexao, colecao):
    conn = MongoClient(url_conexao)
    db = conn[colecao]
    print("Conexão realizada com sucesso")

obter_colecao_mongodb('mongodb+srv://last_project_gama:gama_1234@cluster0.jruk8oe.mongodb.net/test', 'data')


