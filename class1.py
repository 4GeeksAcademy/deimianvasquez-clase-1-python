# name = "Juan"
# last_name = "Peréz"

# print(f"{name} {last_name} dijo \"chao\"")

# suma = lambda item: print(f"Hola {item}")

# suma("deimian")


# for index in range(100, -1, -1):
#     print(index)

names = ["Deimian", "José", "Mario", "Cristopher", "Jesus", "Ricardo 1", "Elio"]
# print(len(names))
names.append("Ricardo 2")
# imprimir ultimo de la una lista
# print(names[len(names)-1])
# print(names[-1])
names[1] = "Alejandro"
names.append("José Morrone")
names.insert(3,"Jose Pinto")
# result = names.pop(0)
# names.remove("Ricardo 1")
# print(f"El usuario {result} se elimino.")
# print(names)
# del names[0:int(len(names) / 2)]

# loops 
# print(names) 

# for index in range(0, len(names)):
#     print(names[index])

# count = 0

# while count< len(names):
#     text = input("Ingresa algo: ")
#     print(names[count])
    

# message = """
#     Bienvenido a mi conversor de moneda, elija una opción para cambiar:
#     1.- Bolivares a dólares
#     0.- Salir
# """

# while True:
#     print(message)
#     option = int(input("Ingrese la opción: "))

#     if option == 1:
#         total_change = float(input("Ingresa el monto en bolívares: "))
#         total = 56  * total_change
#         print(f"Es un total de {round(total, 3)} Bolívares")
#     else:
#         print("Gracias por usar nuestro servicio")
#         break


# for index in range(100, -1, -1):
#     print(index)


# List comprension
# numeros = [1, 2, 3, 4, 5]
# #      devuelve for item in lista 
# pares = [item*2 for item in numeros]
# # pares = [x for x in numeros if x % 2 == 0]
# print(pares)


## functions
# def sum(num1=0, num2=0):
#     # una identación estara dentro de la funcion
#     result = num1 + num2
#     return result

# print(sum(5))

# def sum(*args): # acepta todos los parametros

#     total = 0
#     for i in args:
#         total+=i
#     return total

# def mult(num1=1, num2=0):
#     return num1*num2


# print(mult(sum(5,6,9), mult(58, 63)))

# # funciones lambda
# resta = lambda num1, num2: num1-num2
# print(resta(10, 5)

# print(names)

# for item in names:
#     print(f"Hola ¿qué tal {item}?")

# def saludar(item):
#     return f"Hola ¿qué tal {item}?"


# result = list(map(lambda item: f"Hola ¿qué tal {item}?" , names))
# print(result)

def letter(item):
    return

result = list(filter(lambda item:  "io" in item.lower() , names))
print(result)