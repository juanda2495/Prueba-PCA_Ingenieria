import random
saldo=15000
colores = ["Verde", "Rojo", "Negro"]
probabilidades = [ 0.01, 0.495, 0.495]
#Menu principal
menu = """

¿Que acción desea realizar?
1.Modificar monto en Juego
2.Jugar
3.Salir
Seleccionar acción: """
# Función para solicitar la apuesta
def dinero_apuesta (monto):
    apuesta_min = monto*11/100
    apuesta_max = monto*19/100
    dinero_apostado = 0
    if monto <= 1000 and monto != 0:
        dinero_apostado = monto
        print ("All in ", monto)
    else:
        while dinero_apostado < apuesta_min or dinero_apostado > apuesta_max:
            dinero_apostado = float (input(f"Rango de apuesta entre {apuesta_min} y {apuesta_max} ¿Cuanto desea apostar? "))
            if dinero_apostado < apuesta_min or dinero_apostado > apuesta_max:
                print ("Por favor ingrese un monto que este dentro del rango")
    return (dinero_apostado)

#Función para las probabilidades de cada color
def probabilidad_colores(datos, pesos):
    r = random.random()
    for i, p in enumerate(pesos):
        if p > r:
            break
    return datos[i]


#Función para elegir el color ganador
def color():
    lista_colores = [probabilidad_colores(colores, probabilidades) for _ in range (1000)]
    indice = random.randint (0, len(lista_colores)-1)
    return lista_colores[indice]

def main():
    global saldo
    print ("Su saldo actual es de: ", saldo)
    eleccion = ""
    while eleccion != "3":
        eleccion = input (menu)
        if eleccion == "1":
            saldo = int(input (f"Ingrese nuevo monto: "))
            print (f"Su nuevo saldo es de {saldo}")
        elif eleccion == "2":
            if saldo == 0:
                print ("Lo sentimos, su saldo actual es de $0.0 por favor ingrese una acción distinta")
                pass
            else:
                apuesta = dinero_apuesta (saldo)
                saldo = saldo - apuesta
                color_apuesta = input ("Elija un color entre:\n1.Verde \n2.Rojo \n3.Negro \nIngrese el numero que corresponde a su elección: ")
                if color_apuesta == "1":
                    color_apuesta = "Verde"
                elif color_apuesta == "2":
                    color_apuesta = "Rojo"
                elif color_apuesta == "3":
                    color_apuesta = "Negro"
                # Elección aleatoria
                color_random = color()
                print ("El color obtenido fue: ", color_random)
                # Acertar
                if color_random == color_apuesta:
                    print ("¡Felicidades! Acertaste")
                    if color_random == "Verde":
                        ganancia = apuesta*10
                    elif color_random == ("Rojo" or "Negro"):
                        ganancia = apuesta*2
                    saldo = saldo + ganancia
                else:
                    print ("Lo sentimos, vuelve a intentarlo")
                print ("Su nuevo saldo es de: ", saldo)
                pass
    print ("Gracias por jugar, su saldo final es de: ", saldo)


main()
                    
           
