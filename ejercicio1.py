
def main():
    #Ejercicio1

    num1=10  #Se inicializa las varaibles
    num2=20

    #Se hace la operacion suma, sumando las dos variables declaradas anteriormente
    suma=num1+num2

    #Se muestra por pantalla el resultado
    print(f"El resultado de la suma es: {suma}")

    #Ejercicio2

    cadena1="Hola"
    cadena2=" Mundo"
    # se conectan las dos variables que declaramos, mostrando "Hola Mundo"
    print(cadena1 + cadena2)

    #Ejercicio3

    #Se pide al usuario ingresar su nombre y dni
    nombre= input("Ingrese su Nombre: ")
    dni= input("Ingrese su DNI: ")

    #Se muestra por pantalla el nombre y dni del usuario
    print(f"El nombre del usuario es {nombre} y su DNI es {dni}")

if __name__ == '__main__':

    main()
