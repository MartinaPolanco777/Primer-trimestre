#--------------------------TALLER CONDICIONALES-----------------------------------

#1 verifica si el numero es positivo o negativo

# num1 = float (input("ingrese n numero: "))

# if num1 > 0:
#     print (f"positivo")
# elif num1 < 0 :
#     print (f"es negativo porque es {num1}")
# else:
#     print ("es cero")

#2 calcula el mayor de los numeros ingresados

# num1= float(input("ingresa el primer numero: "))
# num2= float(input("ingresa el segundo numero: "))
# if num1>num2:
#     print(f"el numero {num1} es mayor que {num2}")
# elif num2>num1:
#     print(f"el numero {num2} es mayor que {num1}")


#3 determina si el numero es par o impar

# numero= float (input("ingrese un numero"))
# if numero == 0:
#     print("El número es cero, que es considerado par.")
# elif numero % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")

# #4 dado un numero, verifica si esta entre 10 y 20

# numero = int(input("Ingresa un número: "))
# if 10 <= numero <= 20:
#     print("El número está entre 10 y 20.")
# else:
#     print("El número NO está entre 10 y 20.")

#5 encuentra el mayor usando condicionales

# num1 = float(input("Ingresa el primer número: "))
# num
# 2 = float(input("Ingresa el segundo número: "))
# num3 = float(input("Ingresa el tercer número: "))
# if num1 >= num2 and num1 >= num3:
#     mayor = num1
# elif num2 >= num1 and num2 >= num3:
#     mayor = num2
# else:
#     mayor = num3
# print("El número mayor es:", mayor)

#6 calcula el precio final con un 10% de descuento si el total es mayor a $100

# precios= float(input("que vale el tomate?: "))
# if precios> 100:
#     els= precios*0.10
#     preciostotales= els - precios
#     print(f"el precio final del producto con el 18% de descuenmto  de {precios}$ del tomate es {els}$")
# else:
#     print(f" el producto esta menos que $100 es un buen  precio y no nse le hara el desdduento")

# 7 verifica si una persona puede votar
# edad = int(input("porfavor ingresa tu Edad: "))
# if edad >= 18:
#     print("Puede votar")
# else:
#     print("No puede votar")

#8 dado el precio  y tipo de cliente (VIP o normal), aplica un descueto de 20% solo a VIP

# precio = (float(input(f" por favor ngrese del precio de producto: ")), input(f"Eres cliente VIP? (Si/No): "))
# precios = precio[0] - (precio[0] * 0.2)
# if precio[1] == "Si":
#     print(f"El precio total con el descuento VIP del 20% es {precios}")
# else:
#     print (f"El precio total sin el descuento VIP es de {precio[0]}")

#9 determina si un numero es multiplo de 5 y de 3 al mismo tiempo
# numero = float(input(f"Ingresa un numero: "))
# if numero % 3 == 0 and numero % 5 == 0:
#     print(f"El numero {numero} es multiplo de 3 y 5")
# else:
#     print(f"El numero {numero} no es múltiplo de 3 y 5")

# 10 dado un numero, verifica si es divisible entre dos numeros dados
# num1 = float(input(f"Ingresa un numero: "))
# num2 = float(input(f"Ingresa un numero para dividirlo: "))
# num3 = float(input(f"Ingresa otro numero para dividirlo: "))
# if num1 % num2 == 0 and num1 %num3 == 0:
#     print(f"{num1} es divisible entre {num2} y {num3}")
# else:
#     print(f"{num1} no es divisible entre {num2} y {num3}")

#------------------TALLER-----------------

#1 Pide tu edad y muestra si eres menor de edad, mayor de edad o adulto mayor

# Edad = int(input("ingresa porfavor tu edad: "))

# if Edad < 18:
#     print("Eres menor de edad")
# elif Edad < 65:
#     print("Eres mayor de edad")
# else:
#     print("Eres adulto mayor")

#2 Solicita tu estatura en metros. Si mide menos de 1.5 m, eres considerado bajo; entre 1.5 y 1.8 m, estatura media; más de 1.8 m, alto

# estatura = float(input("ingresa porfavor tu estatura en metros: "))

# if estatura < 1.5:
#     print(f"Con {estatura} metros, eres considerado bajo.")
# elif estatura <= 1.8:
#     print(f"Con {estatura} metros, tienes estatura media.")
# else:
#     print(f"Con {estatura} metros, eres alto.")

#3 Ingresa un número y muestra si es múltiplo de 2, de 3, o de ninguno.

# num = int(input("Ingresa un número: "))

# if num % 2 == 0 and num % 3 == 0:
#     print(f"{num} es múltiplo de 2 y de 3.")
# elif num % 2 == 0:
#     print(f"{num} es múltiplo de 2.")
# elif num % 3 == 0:
#     print(f"{num} es múltiplo de 3.")
# else:
#     print(f"{num} no es múltiplo de 2 ni de 3.")

#4 Pide un número decimal y determina si tiene 1, 2 o más de 2 decimales (usa str() y split()).

# num = input("Ingresa un número decimal: ")
# prt = str(num).split(".")

# if len(prt) == 1:
#     print("El número no tiene decimales.")
# else:
#     decimales = prt[1]
#     if len(decimales) == 1:
#         print("El número tiene 1 decimal.")
#     elif len(decimales) == 2:
#         print("El número tiene 2 decimales.")
#     else:
#         print("El número tiene más de 2 decimales.")

#5 Solicita un país y muestra si está en la siguiente tupla: ("Colombia", "Perú", "Argentina", "México").

# paises = ("Colombia", "Perú", "Argentina", "México")

# pais = input("Ingresa un país, con la primera letra mayuscula: ")

# if pais in paises:
#     print(f"{pais} está en la lista.")
# else:
#     print(f"{pais} no está en la lista.")

#6 Pide tu tipo de sangre (A, B, AB, O) y muestra tu compatibilidad según un diccionario predefinido.

# compatibilidad = {
#     "A": "A, AB",
#     "B": "B, AB",
#     "AB": "AB",
#     "O": "A, B, AB, O"
# }

# tipo = input("Tipo de sangre (A, B, AB, O): ")

# if tipo in compatibilidad:
#     print(f"Compatible con: {compatibilidad[tipo]}")
# else:
#     print("Tipo de sangre no válido.")

#7Ingresa una temperatura en °C. Si es menor de 10, hace frío. Si está entre 10 y 25, templado. Más de 25, hace calor.

# temperatura = float(input("Ingresa una temperatura en °C: "))

# if temperatura < 10:
#     print(f"Hace frío. La temperatura es {temperatura}°C.")
# elif 10 <= temperatura <= 25:
#     print(f"Templado. La temperatura es {temperatura}°C.")
# else:
#     print(f"Hace calor. La temperatura es {temperatura}°C.")

#8 Crea un menú con opciones 1. Sumar, 2. Restar, 3. Multiplicar. Pide dos números y ejecuta la operación seleccionada

# print("Selecciona una opcion:")
# print("1. Sumar")
# print("2. Restar")
# print("3. Multiplicar")

# opcion = input("Ingresa el numero de la opcion: ")

# num1 = float(input("Ingresa el primer numero: "))
# num2 = float(input("Ingresa el segundo numero: "))

# if opcion == "1":
#     resultado = num1 + num2
#     print(f"La suma de {num1} y {num2} es {resultado}.")
# elif opcion == "2":
#     resultado = num1 - num2
#     print(f"La resta de {num1} menos {num2} es {resultado}.")
# elif opcion == "3":
#     resultado = num1 * num2
#     print(f"La multiplicación de {num1} por {num2} es {resultado}.")
# else:
#     print("Opción no válida.")

#9 Pide un número entre 1 y 12 y muestra el mes correspondiente usando un diccionario.
# meses = {
#     1: "Enero",
#     2: "Febrero",
#     3: "Marzo",
#     4: "Abril",
#     5: "Mayo",
#     6: "Junio",
#     7: "Julio",
#     8: "Agosto",
#     9: "Septiembre",
#     10: "Octubre",
#     11: "Noviembre",
#     12: "Diciembre"
# }
# numero = int(input("Ingresa un numero entre 1 y 12: "))
# if 1 <= numero <= 12:
#     print(f"El mes nmero {numero} es {meses[numero]}.")
# else:
#     print(f"{numero} no es un numero valido, Debe estar entre 1 y 12")

#10 Solicita un número de 4 dígitos y determina si comienza con 1, 2 o cualquier otro.

# num = (input("Ingresa un numero de 4 digitos por favor: "))
# if num[0] ==  "1":
#     print(f"El numero de 4 digitos: {num} comienza por el numero uno")
# elif num[0] == "2":
#     print(f"El numero de 4 digitos: {num} comienza por el numero dos")
# else:
#     print(f"El numero de 4 digitos: {num} no comienza ni por el numero 2 ni por el numero 1")

#11  Ingresa una palabra. Muestra si su primera letra es vocal, consonante o un número

# palabra = input("Ingresa una palabra: ")
# if palabra:
#     primera = palabra[0].lower()  

#     if primera.isdigit():
#         print(f"La primera letra '{primera}' es un número.")
#     elif primera in "aeiou":
#         print(f"La primera letra '{primera}' es una vocal.")
#     elif primera.isalpha():
#         print(f"La primera letra '{primera}' es una consonante.")
#     else:
#         print(f"La primera letra '{primera}' no es una letra ni un número.")
# else:
#     print("No ingresaste ninguna palabra.")

#12 Pide una fruta. Si está en la lista ["manzana", "pera", "piña"], muestra su precio. Si no, indica que no está disponible 

# precios = {
#     "manzana": 1.50,
#     "pera": 1.20,
#     "piña": 2.00
# }

# fruta = input("Ingresa una fruta: ")

# if fruta in precios:
#     print(f"El precio de la {fruta} es ${precios[fruta]:.2f}.")
# else:
#     print(f"La fruta '{fruta}' no está disponible.")

#13 Pide tu calificación (0 a 5). Si es menor que 3, reprobado. Entre 3 y 4, aprobado. Mayor a 4, excelente

# calificacion = float(input("Ingresa tu calificación (0 a 5): "))
# if 0 <= calificacion <= 5:
#     if calificacion < 3:
#         print(f"Tu calificación es {calificacion}. Resultado: Reprobado.")
#     elif 3 <= calificacion <= 4:
#         print(f"Tu calificación es {calificacion}. Resultado: Aprobado.")
#     else:
#         print(f"Tu calificación es {calificacion}. Resultado: ¡Excelente!")
# else:
#     print("Calificación inválida. Debe estar entre 0 y 5.")

#14 Pide un número y muestra si es divisible entre 4, entre 6, o no lo es

# numero = int(input("Ingresa un número: "))
# if numero % 4 == 0 and numero % 6 == 0:
#     print(f"El número {numero} es divisible entre 4 y 6.")
# elif numero % 4 == 0:
#     print(f"El número {numero} es divisible entre 4.")
# elif numero % 6 == 0:
#     print(f"El número {numero} es divisible entre 6.")
# else:
#     print(f"El número {numero} no es divisible entre 4 ni entre 6.")

#15 Crea un sistema de autenticación básico. Pide usuario y clave. Usa un diccionario para validar.

# datos = {
#     "usuario": input("Crea tu nombre de usuario: "),
#     "clave": int(input("Crea tu clave numérica: "))
# }

# print("Tus datos fueron guardados correctamente.\n")

# usuario_ingresado = input("Ingresa tu usuario: ")
# clave_ingresada = int(input("Ingresa tu clave: "))

# if usuario_ingresado == datos["usuario"] and clave_ingresada == datos["clave"]:
#     print("Acceso concedido.")
# else:
#     print("Acceso denegado.")


#16 Solicita una edad y muestra a qué grupo pertenece: niño (0-12), adolescente (13-17), adulto (18-64), mayor (65+)

# edad = int(input("Ingresa tu edad: "))
# if 0 <= edad <= 12:
#     print(f"Tienes {edad} años. Eres un niño.")
# elif 13 <= edad <= 17:
#     print(f"Tienes {edad} años. Eres un adolescente.")
# elif 18 <= edad <= 64:
#     print(f"Tienes {edad} años. Eres un adulto.")
# elif edad >= 65:
#     print(f"Tienes {edad} años. Eres una persona mayor.")
# else:
#     print("Edad no válida.")

#17 Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si no, muestra “ciudad secundaria”.
# capitales = ("bogota", "lima", "quito", "caracas")
# ciudad = input("Ingresa el nombre de una ciudad: ")
# ciudades = ciudad
# if ciudades in capitales:
#     print(f"{ciudad} es una capital.")
# else:
#     print(f"{ciudad} es una ciudad secundaria.")

#18 . Ingresa el valor de una compra. Si es mayor de $200.000 aplica un 15% de descuento. Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay descuento

# valor_compra = float(input("Ingresa el valor de la compra: "))
# if valor_compra > 200000:
#     descuento = valor_compra * 0.15
#     total = valor_compra - descuento
#     print(f"Se aplica un 15% de descuento (${descuento:.2f}). Total a pagar: ${total:.2f}")
# elif 100000 <= valor_compra <= 200000:
#     descuento = valor_compra * 0.10
#     total = valor_compra - descuento
#     print(f"Se aplica un 10% de descuento (${descuento:.2f}). Total a pagar: ${total:.2f}")
# else:
#     print(f"No hay descuento. Total a pagar: ${valor_compra:.2f}")

#19 Pide el nombre y el número de horas trabajadas. Calcula el salario con tarifa de $10.000/hora. Si trabajó más de 40 horas, aplica un bono del 20%

# tarifa = 10000
# nombre = input("Ingresa tu nombre: ")
# horas = float(input("Ingresa el número de horas trabajadas: "))

# salario = horas * tarifa

# if horas > 40:
#     bono = salario * 0.20
#     salario_total = salario + bono
#     print(f"{nombre}, trabajaste más de 40 horas. Se aplica un bono del 20%.")
#     print(f"Salario base: ${salario:.2f}, Bono: ${bono:.2f}, Total a pagar: ${salario_total:.2f}")
# else:
#     print(f"{nombre}, tu salario es: ${salario:.2f} (sin bono)")

#20 Ingresa tu puntaje en una prueba (0 a 100). Si es menor a 50, insuficiente. De 50 a 79, aceptable. 80 a 100, sobresaliente

# puntaje = float(input("Ingresa tu puntaje (0 a 100): "))
# if 0 <= puntaje < 50:
#     print(f"Tu puntaje es {puntaje}. Resultado: Insuficiente.")
# elif 50 <= puntaje <= 79:
#     print(f"Tu puntaje es {puntaje}. Resultado: Aceptable.")
# elif 80 <= puntaje <= 100:
#     print(f"Tu puntaje es {puntaje}. Resultado: Sobresaliente.")
# else:
#     print("Puntaje inválido. Debe estar entre 0 y 100.")