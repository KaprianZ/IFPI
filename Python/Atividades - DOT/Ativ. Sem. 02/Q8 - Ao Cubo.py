def SN(r):
    if r == "S":
        return None
    elif r == "N":
        return Break
    else:
        print("Caractere inválido. Digite novamente")
        print("Você quer continuar?")
        r = input().upper()[0]

def cubo(n):
    return n**3


while True:
    n = float(input("Digite algum número: "))

    print(f" {n} ao cubo é {cubo(n)}.")

    print("Você quer continuar?")
    r = input().upper()[0]
    SN(r)
