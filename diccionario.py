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

#-----------------------------EJERCICIO 6-------------------------------------------

# n1=int(input("ingrese el primer numero: "))
# n2=int(input("ingrese el segundo numero: "))
# n3=int(input("ingrese el tercer numero: "))
# n4=int(input("ingrese el cuarto numero: "))
# n5=int(input("ingrese el quinto numero: "))

# tupla= (n1,n2,n3,n4,n5)

# print (f"La suma de los numeros es", sum(tupla))

#-----------------------------EJERCICIO 7---------------------------------------------

# lista=[]

# nombre=input("ingrese el nombre del primer producto: ")
# cantidad=int(input("ingrese la cantidad que desea del primer producto: "))
# precio=float(input("ingrese el precio del primer producto: "))

# producto={"nombre":nombre,
# "cantidad": cantidad,
# "precio" : precio,
# }

# lista.append(producto)

# nombre2=input("ingrese el nombre del segundo producto: ")
# cantidad2=int(input("ingrese la cantidad que desea del segundo producto: "))
# precio2=float(input("ingrese el precio del segundo producto: "))

# producto2={"nombre":nombre2,
# "cantidad": cantidad2,
# "precio" : precio2,
# }

# lista.append(producto2)

# nombre3=input("ingrese el nombre del tercer producto: ")
# cantidad3=int(input("ingrese la cantidad que desea del tercer producto: "))
# precio3=float(input("ingrese el precio del tercer producto: "))

# producto3={"nombre":nombre3,
# "cantidad": cantidad3,
# "precio" : precio3,
# }

# lista.append(producto3)

# inventario=(
#     producto["cantidad"] * producto["precio"] +
#     producto2["cantidad"] * producto2["precio"] +
#     producto3["cantidad"] * producto3["precio"]
# )
# print (f"el valor del inventario es {inventario}")

#----------------------------EJERCICIO7 8-------------------
#precios = [100, 200, 300, 400, 500]

# descuento = float(input("Ingresa el descuento en porcentaje: "))
# descuento = descuento / 100

# precios[0] = precios[0] - precios[0] * descuento
# precios[1] = precios[1] - precios[1] * descuento
# precios[2] = precios[2] - precios[2] * descuento
# precios[3] = precios[3] - precios[3] * descuento
# precios[4] = precios[4] - precios[4] * descuento

# print("Precios con descuento:", precios)

# --------------------ejercicio9----------------------

# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# n3 = float(input("Nota 3: "))
# n4 = float(input("Nota 4: "))

# notas = (n1, n2, n3, n4)

# print("Nota más alta:", max(notas))
# print("Nota más baja:", min(notas))

# ----------------------ejercicio10--------------------

# conversiones = {
#     "km": 1000,
#     "m": 1,
#     "cm": 0.01
# }


# unidad = input("Ingresa la unidad (km, m, cm): ")
# cantidad = float(input("Ingresa la cantidad: "))

# resultado = cantidad * conversiones[unidad]

# print("Equivalente en metros:", resultado)

# #-------------------------------EJERCICIO 11-------------------------------

# p1 = float(input("Precio 1: "))
# p2 = float(input("Precio 2: "))
# p3 = float(input("Precio 3: "))

# precios = [p1, p2, p3]

# iva1 = p1 * 1.19
# iva2 = p2 * 1.19
# iva3 = p3 * 1.19

# precios_con_iva = [iva1, iva2, iva3]

# print("Precios con IVA:", precios_con_iva)

# -----------------EJERCICIO 12---------------------------------------

# n1 = float(input("Ingresa el primer número: "))
# n2 = float(input("Ingresa el segundo número: "))

# suma = n1 + n2
# resta = n1 - n2
# multiplicacion = n1 * n2
# division = n1 / n2

# operaciones = (suma, resta, multiplicacion, division)

# print("Resultados (suma, resta, multiplicación, división):", operaciones)

# -------------------------------------------EJERCICIO 13--------------------------
# nombre1 = input("Nombre 1: ")
# nota1 = float(input("Nota 1: "))

# nombre2 = input("Nombre 2: ")
# nota2 = float(input("Nota 2: "))

# nombre3 = input("Nombre 3: ")
# nota3 = float(input("Nota 3: "))

# estudiantes = {
#     nombre1: nota1,
#     nombre2: nota2,
#     nombre3: nota3
# }

# promedio = (nota1 + nota2 + nota3) / 3

# print(estudiantes)
# print("Promedio general:", promedio)

#--------------------------------EJERCICIO 14 -------------------------------------

# s1 = float(input("Salario 1: "))
# s2 = float(input("Salario 2: "))
# s3 = float(input("Salario 3: "))
# s4 = float(input("Salario 4: "))
# s5 = float(input("Salario 5: "))

# salarios = [s1, s2, s3, s4, s5]

# a1 = s1 * 1.10
# a2 = s2 * 1.10
# a3 = s3 * 1.10
# a4 = s4 * 1.10
# a5 = s5 * 1.10

# salarios_con_aumento = [a1, a2, a3, a4, a5]

# print("Salarios con aumento del 10%:")
# print(salarios_con_aumento)
#----------------------------------EJERCICIO 15--------------------------------------

# productos = {
#     "producto1": 1000,
#     "producto2": 2000,
#     "producto3": 3000
# }

# impuesto = input("Ingresa el porcentaje de impuesto: ")
# imp = float(impuesto) / 100

# precio1 = productos["producto1"] + productos["producto1"] * imp
# precio2 = productos["producto2"] + productos["producto2"] * imp
# precio3 = productos["producto3"] + productos["producto3"] * imp

# productos_finales = {
#     "producto1": precio1,
#     "producto2": precio2,
#     "producto3": precio3
# }

# print("Precios finales con impuesto:")
# print(productos_finales)

#-------------------------------------EJERCICIO 16-----------------------------------

# e1 = int(input("Edad 1: "))
# e2 = int(input("Edad 2: "))
# e3 = int(input("Edad 3: "))
# e4 = int(input("Edad 4: "))
# e5 = int(input("Edad 5: "))

# mayores = (e1 >= 18) + (e2 >= 18) + (e3 >= 18) + (e4 >= 18) + (e5 >= 18)

# menores = 5 - mayores

# print("Mayores de edad:", mayores)
# print("Menores de edad:", menores)

# -------------------------------------EJERCICIO 17-------------------------

# dolares = float(input("Cantidad en dólares: "))

# euro = 0.85
# peso = 4000
# yen = 110

# en_euros = dolares * euro
# en_pesos = dolares * peso
# en_yenes = dolares * yen

# conversiones = (en_euros, en_pesos, en_yenes)

# print("Conversión (euros, pesos, yenes):", conversiones)

#-------------------------------EJERCICIO 18-------------------------------------------

# nombre1 = input("Nombre del producto 1: ")
# cantidad1 = int(input("Cantidad vendida: "))

# nombre2 = input("Nombre del producto 2: ")
# cantidad2 = int(input("Cantidad vendida: "))

# nombre3 = input("Nombre del producto 3: ")
# cantidad3 = int(input("Cantidad vendida: "))

# ventas = {
#     nombre1: cantidad1,
#     nombre2: cantidad2,
#     nombre3: cantidad3
# }

# total = cantidad1 + cantidad2 + cantidad3

# print("Ventas registradas:", ventas)
# print("Total de unidades vendidas:", total)

#----------------------------------------EJERCICIO 19----------------------------

# t1 = float(input("Temperatura 1: "))
# t2 = float(input("Temperatura 2: "))
# t3 = float(input("Temperatura 3: "))
# t4 = float(input("Temperatura 4: "))
# t5 = float(input("Temperatura 5: "))
# t6 = float(input("Temperatura 6: "))
# t7 = float(input("Temperatura 7: "))
# t8 = float(input("Temperatura 8: "))
# t9 = float(input("Temperatura 9: "))
# t10 = float(input("Temperatura 10: "))

# temperaturas = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]

# a1 = t1 * (t1 > 30)
# a2 = t2 * (t2 > 30)
# a3 = t3 * (t3 > 30)
# a4 = t4 * (t4 > 30)
# a5 = t5 * (t5 > 30)
# a6 = t6 * (t6 > 30)
# a7 = t7 * (t7 > 30)
# a8 = t8 * (t8 > 30)
# a9 = t9 * (t9 > 30)
# a10 = t10 * (t10 > 30)

# b1 = t1 * (t1 < 10)
# b2 = t2 * (t2 < 10)
# b3 = t3 * (t3 < 10)
# b4 = t4 * (t4 < 10)
# b5 = t5 * (t5 < 10)
# b6 = t6 * (t6 < 10)
# b7 = t7 * (t7 < 10)
# b8 = t8 * (t8 < 10)
# b9 = t9 * (t9 < 10)
# b10 = t10 * (t10 < 10)

# mayores_30 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
# menores_10 = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]

# print(f"Lista de temperaturas: {temperaturas}")
# print(f"Temperaturas mayores a 30 grados: {mayores_30}")
# print(f"Temperaturas menores a 10 grados: {menores_10}")

#--------------------------------EJERCICIO 20------------------------------------------ 

# precios = [1000, 2500, 1500, 3000, 2000]

# print(f"Lista original: {precios}")

# precio_eliminar = float(input("Ingresa el precio que deseas eliminar: "))
# precios.remove(precio_eliminar)

# precio_agregar = float(input("Ingresa el nuevo precio que deseas agregar: "))
# precios.append(precio_agregar)

# precios.sort()

# print(f"Lista actualizada y ordenada: {precios}")

