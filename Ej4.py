frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal que haya en su frase: ")

for i in range(len(frase)):
    if frase[i] == vocal:
        frase = frase.replace(frase[i], vocal.upper())

print(frase)