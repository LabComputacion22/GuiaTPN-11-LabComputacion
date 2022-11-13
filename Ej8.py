productos = []
producto_nuevo = ""
while producto_nuevo != "0":
    producto_nuevo = input("Ingrese un producto o \"0\" para finalizar: ")
    if producto_nuevo != "0":
        productos.append(producto_nuevo)
    else:
        break

for i in range(len(productos)):
    print(productos[i])
