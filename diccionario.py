# persona={
#     "nombre" : "xiomara",
#     "edad":38,
#     "nacimiento" : "palmira",
#     "telefono" : 3249016527,
#     "profe" : "comunicadora",
#     "cc" : "123456789"
# }
# print(persona)
#---------------------------------------------------------------
# auto= {
#   "marca":"ford",
#   "modelo":"mustang",
#   "año": 2022,
#   "color":"morado",
#   "placa":"FDN-23U",
#  }
# #--------------------------acceder a valores
# print(auto["modelo"])#resultado: mustang
# #--------------------------modificar valores
# auto[año]="rojo"
# #--------------------------añadir nuevos valores
# del auto["modelo"]
# #--------------------------aliminar elementos
# auto.pop("marca")

#--------------------------------TALLER----------------------------------
#------------------1

# nota1=float(input("ingrese la primera nota: "))
# nota2=float(input("ingrese la segnda nota: "))
# nota3=float(input("ingrese la tercera  nota: "))
# lista=[]
# lista.append(nota1)
# lista.append(nota2)
# lista.append(nota3)
# print(lista)
# suma=nota1+nota2+nota3
# promedio=suma/3
# print(f"el proedio de sus calificaciones es {promedio}")


#-------------2
# productos= {
#     "leche": 5000,
#     "pan":5000,
#     "huevos":700
#     }
# print(productos)
# porcentaje=float(input("procentaje de aumento (%): "))
# productos["pan"]+=productos["pan"]*(porcentaje/100)
# productos["leche"]+=productos["leche"]* (porcentaje/100)
# productos["huevos"]+=productos["huevos"*(porcentaje/100)]
# print(productos)


#-------------3

# temperatura1=float(input("ingrese la primer temperatura: "))
# temperatura2=float(input("ingrese la primer temperatura: "))
# temperatura3=float(input("ingrese la primer temperatura: "))
# temperatura4=float(input("ingrese la primer temperatura: "))
# temperatura5=float(input("ingrese la primer temperatura: "))

# celcius=(temperatura1),(temperatura2),(temperatura2),(temperatura3),(temperatura4),(temperatura5)

# operacion1= temperatura1* 9/5+32
# operacion2=temperatura2* 9/5+32
# operacion3=temperatura3* 9/5+32
# operacion4=temperatura4* 9/5+32
# operacion5=temperatura5* 9/5+32
# fahrenheit=(operacion1),(operacion2),(operacion3),(operacion4),(operacion5)
# print("temperatura en °c: ")

#----------------4

# edades= [int(input("edad 1: ")), int(input("edad 2: ")), int(input("edad 3: ")), int(input("edad 4: ")), int(input("edad 5: "))]
# promedio=sum(edades)/len(edades)
# print(f"mayor: {max(edades)}, menor:{min(edades)},promedio: {promedio}")

#---------------5
# frutas=("uva" : 3000 , "manzana" : 2500 , "piña": 3500))
# print(frutas)

# valortotal = [float(input(f"Cuantos kilos de manzana deseas?: ")), float(input(f"Cuantos kilos de pera deseas??: ")), float(input(f"Cuantos kilos de mango deseas?: "))]

# frutas["Manzana"] = (frutas["Manzana"]) * (valortotal[0])
# frutas["Pera"] = (frutas["Pera"]) * (valortotal[1])
# frutas["Mango"] = (frutas["Mango"]) * (valortotal[2])

# sm = frutas["Manzana"] + frutas["Pera"] + frutas["Mango"]
# print(f"El valor total de todos los kilos de fruta es: ${sm}")