import random
import csv

opcion = 0
opcionmenu= 0
asignar_sueldo_y_cantidad = 0
clasificar_sueldos = 0
clasificar_sueldo = 0
mostrar_estadisticas = 0
generar_reporte = 0
opcion = 0
rut = 0


trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


while opcionmenu:
    print("Menu")
    print("1. Asignar sueldos aleatorios")
    print("2. clasificar sueldos")
    print("3. ver estadisticas")
    print("4. reporte de sueldos ")
    print("5. salir del programa")
    




opcion = input("por favor ingrese el numero de la opcion que desea realizar: ")

if opcion==0:
        opcion = int(opcion)

        
        if opcion == 1:
            asignar_sueldo_y_cantidad
            print("se han asignado aleatorioamente los sueldos")

        if opcion == 2:
            clasificar_sueldos
            print ("clasificacion de sueldo")


        if opcion == 3:
            mostrar_estadisticas
            print (" mostar en la pantalla ,sueldo mas alto ,bajo,promedio y media geomtrica")

        if opcion == 4:
            generar_reporte

            print("El reporte se ha generado en 'reporte_sueldo.csv'")

        if opcion == 5:
            print ("finalizando programa.....")
        else:
            print("esta opcion no es valida, por favor ingrese un numero del 1 al 5.")


        print ("desarollado por adelain septembre")
        rut = ("24.667.418-3")





