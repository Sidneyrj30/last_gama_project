def teste(n1, n2):
    resultado = f"{n1}, {n2}"
    return resultado

def mostrar():
    n1 = input("Digite a primeira palavra: ")
    n2 = input("Digite a segunda palavra: ")

    resultado = teste(n1,n2)

    print("-------------")
    print(resultado)
    print("-------------")

mostrar()    