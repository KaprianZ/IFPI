def main():
    li = []
    print("Primeira lista:")
    for i in range(4):
        l = []
        for j in range(4):
            n = int(input("Digite um número:"))
            l.append(n)
        m = max(l)
        li.append(m)
        print("Outra lista:")
    print(f"O maior número da 1º série é {li[0]}, o 2º é {li[1]}, o 3º {li[2]} e o 4º{li[3]}.")

if __name__ == "__main__":
    main()
