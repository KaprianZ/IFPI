def fatorar(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def soma(n):
    s = 1
    for i in range(1, n+1):
        s += 1/fatorar(i)
    return s


while True:
    try:
        n = int(input("Digite um número inteiro e positivo: "))
        if n >= 0:
            print(f"A soma é {round(soma(n), 2)}")
            break
        else: print("Número Negativo.")
    except:
        print("Número Inválido.")
