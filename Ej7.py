fecha = input("Ingrese su fecha de nacimiento: ")

dia = fecha[:fecha.find("/")]
fecha = fecha.removeprefix(dia+"/")
# print(fecha)
mes = fecha[:fecha.find("/")]
fecha = fecha.removeprefix(mes+"/")
# print(fecha)
año = fecha

print(f"{dia}\n{mes}\n{año}")