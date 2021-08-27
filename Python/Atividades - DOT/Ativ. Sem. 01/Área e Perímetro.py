def area(r):
    return 3.14 * r ** 2
def peri(r):
    return 3.14 * 2 * r
def main():
    raio = float(input("Digite o valor do raio:"))
    a = round(area(raio), 2)
    p = round(peri(raio), 2)
    print(f"A área da circulo é {a} e o perímetro é {p}")
if __name__=="__main__":
    main()
