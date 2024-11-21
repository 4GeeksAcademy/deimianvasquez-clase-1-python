import random


lista_numeros = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(lista_numeros)
seleccion_maquina = lista_numeros[0:3]

# print(seleccion_maquina)
while True:
    herido = 0
    muerto= 0

    entrada_usuario = input("Ingresa tres números: ")
    if len(entrada_usuario)!= 3:
        print("Por favor ingresa un número de tres cifras :) ")
        continue

    seleccion_usuario = []
    for num in entrada_usuario:
        seleccion_usuario.append(int(num))


    for index_maquina, valor_maquina in enumerate(seleccion_maquina):
        for index_usurio, valor_usuario in enumerate(seleccion_usuario):
            # print(index_maquina, valor_maquina, index_usurio, valor_usuario)
            if index_maquina == index_usurio and valor_maquina == valor_usuario:
                muerto+=1
            elif valor_maquina == valor_usuario:
                herido+=1
    
    print(f"Tienes {herido} heridos \nTienes {muerto} muertos")
    if muerto == 3:
        print("GANASTE!!!!!")
        break           
    
    print(seleccion_maquina,"maquina")
    print(seleccion_usuario)
