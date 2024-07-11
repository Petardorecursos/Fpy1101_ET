import csv
import random
import time
import os

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trab1 = ["Juan Pérez"]
trab2 = ["María García"]
trab3 = ["Carlos López"]
trab4 = ["Ana Martínez"]
trab5 = ["Pedro Rodríguez"]
trab6 = ["Laura Hernández"]
trab7 = ["Miguel Sánchez"]
trab8 = ["Isabel Gómez"]
trab9 = ["Francisco Díaz"]
trab10 = ["Elena Fernández"]

sueldo = []
sueldomin = []
sueldomed = []
sueldotop = []
def generarsueldos():
    sueldo1 = alea()
    sueldo.append(sueldo1)
    sueldo2 = alea()
    sueldo.append(sueldo2)
    sueldo3 = alea()
    sueldo.append(sueldo3)
    sueldo4 = alea()
    sueldo.append(sueldo4)
    sueldo5 = alea()
    sueldo.append(sueldo5)
    sueldo6 = alea()
    sueldo.append(sueldo6)
    sueldo7 = alea()
    sueldo.append(sueldo7)
    sueldo8 = alea()
    sueldo.append(sueldo8)
    sueldo9 = alea()
    sueldo.append(sueldo9)
    sueldo10 = alea()
    sueldo.append(sueldo10)

    


def alea():
    return random.randint(300000,2500000)
def menu():
    generarsueldos()
    while True:
        print("bienvenido al sistema nuevamente")
        print("-"*50)
        print("1-Asignar sueldos aleatorios")
        
        print("2-Clasificar sueldos")
        
        print("3-Ver estadísticas.")
        
        print("4-Reporte de sueldos")
        
        print("5-Salir del programa")
        print("-"*50)
        
        
        try:
            opcion = int(input("ingrese su opcion preferida: "))
            
            if opcion >=1 and opcion <=5:
                if opcion == 1:
                    os.system("cls")
                    print("sueldos asignados correctamente")
                    # fue hecho antes para asegurar
                    input("Presione enter para continuar")
                    

                elif opcion == 2:
                    os.system("cls")
                    clasificarsueldo()
                    
                elif opcion == 3:
                    os.system("cls")
                    verestadisticas()
                    
                elif opcion == 4:
                    os.system("cls")
                    reportesueldo()
                    
                else:
                    os.system("cls")
                    salir()
                    break
            
            else:
                print("opcion Ingresada no valida, vuelva a intentarlo")
                input("Presione enter para continuar")
                os.system("cls")
        except ValueError:
            print("Dato ingresado No valido, vuelva a intentarlo")
            input("Presione enter para continuar")
            os.system("cls")    
        
def clasificarsueldo():
    for i in sueldo:
        if i <800000:
            sueldomin.append(i)
            
        elif i >= 800000 and i <= 2000000:
            sueldomed.append(i)
        else:
            sueldotop.append(i)
            
    for i in sueldo:
        if i == sueldo[0]:
            trab1.append(i)
        elif i == sueldo[1]:
            trab2.append(i)
        elif i == sueldo[2]:
            trab3.append(i)
        elif i == sueldo[3]:
            trab4.append(i)
        elif i == sueldo[4]:
            trab5.append(i)
        elif i == sueldo[5]:
            trab6.append(i)
        elif i == sueldo[6]:
            trab7.append(i)
        elif i == sueldo[7]:
            trab8.append(i)
        elif i == sueldo[8]:
            trab9.append(i)
        elif i == sueldo[9]:
            trab10.append(i)
    print("trabajador y sueldo base")
    print(trab1)
    print()
    print(trab2)
    print()
    print(trab3)
    print()
    print(trab4)
    print()
    print(trab5)
    print()
    print(trab6)
    print()
    print(trab7)
    print()
    print(trab8)
    print()
    print(trab9)
    print()
    print(trab10)
    
    totalsueldos = trab1[1] + trab2[1] + trab3[1] + trab4[1] + trab5[1] + trab6[1] + trab7[1] + trab8[1] + trab9[1] + trab10[1]
    print()
    print("total de gastos en sueldos: ", totalsueldos)
    input("presione enter para continuar")
            
        
def salir():
    print("Saliendo del Programa...")
    time.sleep(2)
    print("Desarrollado por: Ricardo henriquez")
    print("Rut: 21.904.573-5")

def promedio():
    totalsueldos = sum(sueldo)
    return totalsueldos / len(sueldo)
    
def verestadisticas():
    sueldomasalto = max(sueldo)
    sueldomasbajo = min(sueldo)
    promedi = promedio()
    print(promedi)
    
    datos = f"el sueldo mas alto es: {sueldomasalto}, el sueldo mas bajo es: {sueldomasbajo}, el promedio de sueldo es: {promedi}"
    print(datos)
    input("Presione enter para continuar")
    
def reportesueldo():
    print(trab1)
    print(trab2)
    print(trab3)
    print(trab4)
    print(trab5)
    print(trab6)
    print(trab7)
    print(trab8)
    print(trab9)
    print(trab10)
    input("presione enter para continuar")

    
        

menu()