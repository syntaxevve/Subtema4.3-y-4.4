import os 
nombre_mascotas = [""]*3 #Rocky
edad_mascotas = [0]*3 

def insertar ():  
   for i in  range (len(nombre_mascotas)): # .Length en C#
      nombre_mascotas [i]= input(f"Ingrese nombre de la mascota: ") 
      edad_mascotas[i] = int (input(f"Ingrese edad mascota: "))
def mostrar ():  
   for i in  range (len(nombre_mascotas)): # .Length en C#
      print(f"Nombre: {nombre_mascotas [i]} , Edad: {edad_mascotas [i]}")

def eliminar(nombreAborrar):
    for i in range(len(nombre_mascotas)):
       if nombre_mascotas[i] == nombreAborrar:                         # encuntre a la mascota que quiero borrar
          for j in range(i.len(nombre_mascotas)-1):
              nombre_mascotas[j] = nombre_mascotas [j+1]
              edad_mascotas[j] = edad_mascotas[j+1]

              #dejar en blanco la ultima ubicacion
              nombre_mascotas[-1] = ""
              edad_mascotas[-1] = 0
              print(f"Mascota eliminda {nombre_mascota[i]}")
              return #detener la busqueda de la mascota con el mismo nombre
def ordenarMascotita():

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
        print("[4] Ordenar mascotas alfabeticamente")
        print("[5] Salir")
        opcion = int (input("Elija una opcion: "))
        if opcion==1:
            insertar()
        elif opcion==2:
            mostrar()
        elif opcion==3:
             mascotaAborrar = input("Ingrese mascota a borrar: ")
             eliminar(mascotaAborrar)
        elif opcion==4:
            print("Ordenar")
        elif opcion==5:
            print("Saliendo...")
        else: print ("Opcion invalida")
        if opcion !=4: input ("Presiona para continuar")

    

main()

