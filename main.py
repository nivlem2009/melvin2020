# # EJERCICIO I

print(type(4<2))


# # EJERCICIO II

usuario = input("escriba su nombre de usuario:")
print("bienvenido : " + usuario)

# EJERCICIO III

numero = input("ingrese el numero a evaluar")
numero = float(numero)

if numero % 2 == 0:
    print("el numero es par")
    

# # EJERCICIO IV

primernumero = input ("ingrese el primer numero")
primernumero = float (primernumero)
segundonumero = input("ingrese el segundo numero")
segundonumero = float(segundonumero)
if primernumero > segundonumero:
    print("el primer numero es mayor que el segundo")



# # EJERCICIO V

cantidad_Dollar = input("ingresa cantidad de dolares")
cantidad_Dollar = float(cantidad_Dollar)
tasa = 58.34
print(cantidad_Dollar * tasa)


# # EJERCICIO VI

celcius = input("ingrese grados celcius")
celcius = float(celcius)
fahrenheit = (celcius * 1.8) + 32
print(fahrenheit)

# # EJERCICIO VII

valor1 = input("ingrese el primer valor")
valor1 = float(valor1)
valor2 = input("ingrese el segundo valor")
valor2 = float(valor2)
valor3 = input("ingrese el tercer valor")
valor3 = float(valor3)
valor4 = input("ingrese el cuarto valor")
valor4 = float(valor4)
print((valor1 + valor2 + valor3 + valor4) / 4)


promedio = ((valor1 + valor2 + valor3 + valor4) / 4)
if promedio >= 90:
    print("su calificacion es A")

elif 80<= promedio <90:
    print("su calificacion es B")

elif 70<= promedio <=79:
    print("su calificacion es C pasaste a chepa")
    
elif 60<= promedio <=69:
    print("su calificacion es D usted ta feo")

elif promedio <=59:
    print("su calificacion es F usted se jodio")


# # EJERCICIO VIII

monto = input("ingrese el monto")
monto = float(monto)
cuotas = input("ingrese la cantidad de cuotas")
cuotas = float(cuotas)
tasa = input("ingrese la tasa de interes anual")

cuotamensual = ((monto * 0.12) / 12) + (monto / 12)
print(cuotamensual)






















    


    








































