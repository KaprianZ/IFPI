def poli(l, m):
    return l * m

l = int(input("Número de lado: "))
m = float(input("Digite o tamanho do lado: "))

peri = poli(l, m)

if l == 3:
    print(f"TRIÂNGULO, com o perímetro de {peri} cm.")
elif l == 4:
    print(f"QUADRADO, com o perímetro de {peri} cm.")
elif l == 5:
    print(f"PENTÁGONO, com o perímetro de {peri} cm.")
