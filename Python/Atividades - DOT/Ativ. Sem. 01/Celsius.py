def celsius(f):
    return ((f-32)/9)*5


f = float(input("Digite a temperatura em Fahrenheit:"))
print(f"A temperatura convertida em celsius {round(celsius(f), 2)}")
