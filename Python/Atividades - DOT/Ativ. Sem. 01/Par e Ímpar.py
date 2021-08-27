def par_impar(n):
    if n%2 == 0: return True
    else: return False

def main():
    num = int(input("Digite um número?"))
    print(par_impar(num))

if __name__ == "__main__":
    main()
