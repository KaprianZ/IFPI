def somatorio(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s


n = int(input("Digite um número inteiro e positivo: "))

print(f"A somatória de {n} é {somatorio(n)}.")
