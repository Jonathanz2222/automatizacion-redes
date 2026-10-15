# Practica 3: Informacion de dispositivos de red

#Datos de R1
router1 = {
    "nombre": "R1",
    "tipo": "Router",
    "ip": "10.1.1.1",
    "submascara": "255.255.255.0",
    "loopback": "1.1.1.1",
    "interfaz": "GigabitEthernet0/0",
    "Marca" : "Cisco",
    "estado": "Activo"
}

#Datos de R2
router2 = {
    "nombre": "R2",
    "tipo": "Router",
    "ip": "10.1.1.2",
    "submascara": "255.255.255.0",
    "loopback": "2.2.2.2",
    "interfaz": "GigabitEthernet0/0",
    "Marca" : "Cisco",
    "estado": "Activo"
}
#Datos de SW1
switch1 = {
    "nombre": "SW1",
    "tipo": "Switch",
    "ip": "10.1.1.3",
    "submascara": "255.255.255.0",
    "loopback": "3.3.3.3",
    "interfaz": "GigabitEthernet0/0",
    "Marca" : "Cisco",
    "estado": "Fuera de Servicio"
}

#Lista de dispositivos
dispositivos = [router1, router2, switch1]

'''
#paso 9
for dispositivo in dispositivos:
    print(f"Nombre: {dispositivo['nombre']}")
    print(f"Tipo: {dispositivo['tipo']}")
    print(f"IP: {dispositivo['ip']}")
    print(f"Loopback: {dispositivo['loopback']}")
    print(f"Interfaz: {dispositivo['interfaz']}")
    print(f"Estado: {dispositivo['estado']}")
    print("-----------------------------")
'''


#creaemos una funcion para mostrar la informacion de los dispositivos
def mostrar_dispositivo(dispositivo):
    print("-----------------------------")
    print(f"Nombre: {dispositivo['nombre']}")
    print(f"Tipo: {dispositivo['tipo']}")
    print(f"IP: {dispositivo['ip']}")
    print(f"Submascara: {dispositivo['submascara']}")
    print(f"Loopback: {dispositivo['loopback']}")
    print(f"Interfaz: {dispositivo['interfaz']}")
    print(f"Marca: {dispositivo['Marca']}")
    print(f"Estado: {dispositivo['estado']}") 
    print("-----------------------------")



    #verificar el estado del dispositivo
    if dispositivo['estado'] == "Activo":
        print(f"El dispositivo {dispositivo['nombre']} esta activo")

        print("-----------------------------")  
    else:
        print(f"El dispositivo {dispositivo['nombre']} esta inactivo")

        print("-----------------------------")

while True:
        print("-----------------------------")
        print("Menu de opciones:")
        print("1. Mostrar todos los dispositivos")
        print("2. Buscar un dispositivo por nombre")
        print("3. Salir")  
        
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
             for dispositivo in dispositivos:
                 mostrar_dispositivo(dispositivo)
                 
        elif opcion == "2":
            buscar = input("Ingrese el nombre del dispositivo: ").strip().upper()
            encontrado = False
        
            for dispositivo in dispositivos:
              if dispositivo['nombre'] == buscar:
                 mostrar_dispositivo(dispositivo)
                 encontrado = True
                 break

              if not encontrado:
                 print(f"El dispositivo {buscar} no se encuentra en la lista")
                 break
                 
        elif opcion == "3":
            print("Saliendo del programa...")
            break 
        
        else:
            print("Opcion no valida, intente de nuevo")