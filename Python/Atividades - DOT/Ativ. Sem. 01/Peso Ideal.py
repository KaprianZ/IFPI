def peso_ideal(a, s):
    if s == 1:
        return (62.1 * a) - 44.7
    if s == 2:
        return (72.7 * a) - 58


def main():
    h = float(input("Digite a sua altura: "))
    s = int(input("Você é homen ou mulher? 1 - Mulher 2 - Homem "))

    c = peso_ideal(h, s)
    
    print(f"Seu peso ideal é {c} kg.")


if __name__ == "__main__":
    main()
