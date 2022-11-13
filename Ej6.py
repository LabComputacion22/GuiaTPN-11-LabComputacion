precio = input("Ingrese el precio: ")

parte_entera = precio[:precio.find(",")]

parte_decimal = precio[precio.find(",")+1:]

print(parte_entera)
print(parte_decimal)