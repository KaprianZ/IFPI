def divisores(n):
    cont = 0
    for i in range(1, n/2+1):
        if n % i == 0:
            cont += 1
    return cont


def main():
    num = int(input("Digite um número inteiro e positivo para descobri quantos divisores ele possui: "))

    d = divisores(num)

    print(f"{num} tem {d} divisor(es).")


if __name__ == "__main__":
    main()
