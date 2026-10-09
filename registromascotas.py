import os 
nombre_mascotas = [""]*3 #Rocky
edad_mascotas = [0]*3 

def insertar ():  
   for i in  range (len(nombre_mascotas)): # .Length en C#
      nombre_mascotas [i]= input(f"ingrese nombre de la mascota: ") 
      edad_mascotas[i] = int (input(f"ingrese edad mascota: "))
def mostrar ():  
   for i in  range (len(nombre_mascotas)): # .Length en C#
      print(f"nombre: {nombre_mascotas [i]} , edad: {edad_mascotas [i]}")

def main ():
    global nombre_mascotas, edad_mascotas #para modificar las listas declaradas fuera del arreglo
    #arreglar paraleloss ambas listas deben tener la misma longitud 3
    nombre_mascotas = [""]*3 #iniciar la lista vacia para cadenas de longitud 3
    edad_mascotas = [0]*3 #iniciar la lista vacia para numeros enteros de longitud 3
   
    opcion=0
    while opcion !=4:
        os.system('cls' if os.name== 'nt' else 'clear')
        print("[1] Ingresar mascota (nombre | edad)")
        print("[2] Mostrar mascota (noombre | edad)")
        print("[3] Eliminar mascotas por nombre 8en ambos vectores)")
        print("[4] Salir")
        opcion = int (input("Elija una opcion: "))
        if opcion==1:
            insertar()
        elif opcion==2:
            print("Mostar")
        elif opcion==3:
            print("Eliminar")
        elif opcion==4:
            print("Saliendo...")
        else: print ("Opcion invalida")
        if opcion !=4: input ("presiona para continuar")

    

main()

