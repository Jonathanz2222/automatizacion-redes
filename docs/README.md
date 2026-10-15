# Práctica 3. Primer programa de Python para representar información de dispositivos

## 1. Propósito

El propósito de esta práctica fue desarrollar un programa básico en Python para representar y organizar información de dispositivos de red. Se registraron tres dispositivos (R1, R2 y SW1) mediante diccionarios y una lista. También se implementaron ciclos, condicionales y funciones para mostrar sus características y verificar su estado de funcionamiento.

## 2. Conceptos utilizados

- **Variables:** permiten almacenar información y utilizarla durante la ejecución del programa.
- **Tipos de datos:** se utilizaron principalmente cadenas de texto (`str`) para representar nombres, tipos de dispositivos, direcciones IP, interfaces y estados.
- **`print()`:** permite mostrar en la terminal la información de cada dispositivo.
- **Diccionarios:** almacenan los datos de cada equipo mediante pares de clave y valor, como nombre, tipo, IP, loopback, interfaz, ubicación, marca y estado.
- **Listas:** permiten agrupar los diccionarios de R1, R2 y SW1 en una sola colección llamada `dispositivos`.
- **Ciclo `for`:** recorre la lista para procesar y mostrar la información de cada dispositivo.
- **Condicional `if`:** comprueba si el estado del dispositivo es `"Activo"` y muestra un mensaje según su condición.
- **Funciones:** se creó la función `mostrar_dispositivo()` para mostrar la información de un equipo y comprobar su estado sin repetir el código.

## 3. Dispositivos representados

| Dispositivo | Tipo | Dirección IP | Estado | Función |
|---|---|---|---|---|
| R1 | Router | 10.1.1.1 | Activo | Enrutamiento |
| R2 | Router | 10.1.1.2 | Activo | Enrutamiento |
| SW1 | Switch | 10.1.1.3 | Activo | Conectividad |

Los datos corresponden a la topología utilizada durante la práctica. El programa también registra la dirección loopback, la interfaz, la ubicación y la marca de cada dispositivo.

## 4. Evidencias

Se deben incluir capturas de pantalla que demuestren el desarrollo y funcionamiento del programa.

1. Código fuente con las variables y los datos de los dispositivos.
2. Diccionarios de R1, R2 y SW1.
3. Lista `dispositivos` con los tres equipos.
4. Ciclo `for` mostrando la información.
5. Condicional `if` funcionando con dispositivos activos.
6. Prueba con SW1 en estado `"Fuera de servicio"`.
7. Función `mostrar_dispositivo()` y resultado de su ejecución.
8. Ejecución final con los dispositivos restaurados al estado `"Activo"`.

Las capturas se encuentran organizadas en la carpeta `evidencias` de esta práctica.

## 5. Problemas y soluciones

| Problema | Causa | Solución |
|---|---|---|
| Al principio, la información se mostraba mediante instrucciones individuales. | Todavía no se utilizaban estructuras para organizar los datos. | Se crearon diccionarios para cada dispositivo y una lista para agruparlos. |
| Fue necesario comprobar el estado de los equipos. | El programa debía distinguir entre dispositivos activos y fuera de servicio. | Se implementó una condición `if/else` para mostrar mensajes diferentes. |
| Se necesitaba evitar repetir las instrucciones para mostrar cada equipo. | El código de impresión podía repetirse para cada dispositivo. | Se creó la función `mostrar_dispositivo()` y se llamó desde un ciclo `for`. |

## 6. Conclusión

Durante esta práctica aprendí a utilizar Python para representar y organizar información de dispositivos de red. Comprendí cómo funcionan las variables, los diccionarios, las listas, los ciclos, las condiciones y las funciones. También comprobé que es posible identificar el estado de un dispositivo y mostrar un mensaje según su condición. Este programa puede servir como base para desarrollar herramientas de automatización de redes, ya que posteriormente se podrían agregar funciones para consultar dispositivos, verificar conectividad, recopilar información de routers y switches y generar reportes automáticamente.