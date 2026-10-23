# Parte 5. Evaluar la confiabilidad de los recursos

## Paso 6. Comparar la calidad de la información

### Tabla de evaluación de recursos

| Criterio | Recurso 1: Python | Recurso 2: GNS3 | Recurso 3: Netmiko |
|---|---|---|---|
| **¿Quién publica o mantiene el recurso?** | Python Software Foundation y colaboradores de Python. | Equipo de GNS3. | Kirk Byers y colaboradores del proyecto Netmiko. |
| **¿La información corresponde al tema investigado?** | Sí, explica el lenguaje Python y sus características. | Sí, explica la creación y configuración de redes virtuales. | Sí, aborda la automatización de dispositivos de red mediante conexiones SSH. |
| **¿Incluye ejemplos o instrucciones verificables?** | Sí, incluye tutoriales, ejemplos y explicaciones de código. | Sí, ofrece guías e instrucciones para configurar proyectos de red. | Sí, contiene ejemplos de uso e instrucciones de instalación. |
| **¿Se identifica la versión o fecha de actualización cuando corresponde?** | Sí, la documentación está organizada por versiones de Python. | La documentación puede incluir guías y procedimientos que deben contrastarse con la versión instalada. | Sí, el repositorio muestra versiones, cambios y archivos relacionados con el desarrollo. |
| **¿Es posible comprobar la información con otra fuente?** | Sí, comparando los ejemplos con la ejecución del código y otras referencias de Python. | Sí, realizando las configuraciones en GNS3 y comprobando la conectividad. | Sí, probando los ejemplos en un entorno compatible y comparando los resultados con la documentación de los dispositivos. |
| **¿Qué utilidad tiene para el proyecto integrador?** | Ayuda a programar en Python y organizar los datos de los dispositivos de red. | Permite construir una topología virtual y realizar pruebas de conectividad. | Permite investigar cómo automatizar conexiones y ejecutar comandos en equipos de red compatibles. |

### Enlaces de los recursos evaluados

1. **Documentación oficial de Python:** https://docs.python.org/es/3/
2. **Documentación oficial de GNS3:** https://docs.gns3.com/docs/
3. **Repositorio oficial de Netmiko:** https://github.com/ktbyers/netmiko

---

## Preguntas de análisis

### 1. ¿Cuál de los recursos consideras más útil para resolver dudas de Python? ¿Por qué?

La documentación oficial de Python es la más útil porque explica la sintaxis, las funciones y las estructuras del lenguaje mediante ejemplos. Además, permite consultar información correspondiente a distintas versiones y comprobar cómo debe utilizarse cada instrucción.

### 2. ¿Cuál consultarías para resolver un problema relacionado con GNS3?

Consultaría la documentación oficial de GNS3, porque contiene instrucciones para crear topologías, configurar dispositivos y solucionar problemas de simulación. También realizaría pruebas dentro del programa para verificar que la solución funciona.

### 3. ¿Por qué no conviene copiar directamente una solución sin comprobar que funciona en el entorno de trabajo?

Porque la solución podría utilizar una versión diferente, depender de otras herramientas o no ser compatible con los dispositivos disponibles. Es importante comprender el código, verificar los requisitos y probarlo antes de integrarlo al proyecto, para evitar errores y problemas de seguridad.

---

## Conclusión

Evaluar la confiabilidad de los recursos permite seleccionar información adecuada, actualizada y útil para el proyecto integrador. La documentación de Python ayuda con la programación, GNS3 facilita la simulación de redes y Netmiko permite investigar técnicas de automatización. Comparar la información y realizar pruebas ayuda a confirmar que las soluciones sean correctas para el entorno de trabajo.

---
# Parte 6. Aplicar la investigación a un problema del proyecto

## Paso 7. Analizar un problema técnico hipotético

### Estrategia de investigación

| Elemento | Respuesta del equipo |
|---|---|
| **Problema identificado** | El programa `dispositivos.py` muestra correctamente la información de R1 y R2, pero no identifica un dispositivo cuando se busca por su nombre. |
| **Palabras clave para realizar la búsqueda** | Python buscar dispositivo por nombre, búsqueda en listas de diccionarios, comparación de cadenas, condiciones `if`, errores en búsqueda de dispositivos Python. |
| **Documentación o comunidad que consultarían primero** | Primero consultaríamos el tutorial oficial de Python: https://docs.python.org/es/3/tutorial/. Si no encontramos la solución, buscaríamos preguntas similares en Stack Overflow en español: https://es.stackoverflow.com/. |
| **Información que revisarían en el código** | Revisaríamos cómo se guarda el nombre de cada dispositivo, cómo se solicita el nombre al usuario, qué variable se utiliza para realizar la búsqueda y cómo se comparan los valores. También comprobaríamos la indentación y las condiciones del programa. |
| **Tipo de ejemplo o solución que buscarían** | Buscaríamos un ejemplo de Python que recorra una lista de diccionarios, compare el nombre ingresado con el nombre almacenado y muestre la información del dispositivo cuando coincidan. |
| **Cómo comprobarían que la solución funciona** | Probaríamos la búsqueda con un dispositivo existente, como R1, y después con R2. También ingresaríamos un nombre inexistente para verificar que el programa muestre un mensaje adecuado sin repetirlo innecesariamente. |
| **Cómo documentarían la solución encontrada** | Registraríamos el problema, la causa identificada, el recurso consultado, los cambios realizados en el código y los resultados de las pruebas. Si se utiliza una solución externa, indicaríamos la fuente consultada. |

---

## Conclusión

Una estrategia de investigación organizada permite identificar las posibles causas de un error antes de modificar el programa. Consultar documentación oficial y comunidades de programación ayuda a encontrar soluciones adecuadas. Finalmente, realizar pruebas con dispositivos existentes y nombres inexistentes permite comprobar que la búsqueda funcione correctamente y documentar los resultados para futuras prácticas.

---
---
---
# Práctica 4. Construir una base de conocimiento para el proyecto

## 1. Propósito de la práctica

El propósito de esta práctica es investigar, seleccionar y organizar recursos técnicos confiables que permitan resolver dudas y problemas relacionados con Python, GNS3 y la automatización de redes. También se busca aprender a utilizar documentación oficial y comunidades de colaboración para encontrar soluciones y comprobar su funcionamiento.

## 2. Relación con el proyecto integrador

Esta práctica se relaciona con el proyecto de automatización de redes desarrollado con Python. En la Práctica 3 se creó el programa `dispositivos.py`, que permite representar routers y switches mediante información como su nombre, dirección IP, tipo y estado.

Los recursos investigados permitirán mejorar el programa, resolver errores de búsqueda de dispositivos, comprender el uso de bibliotecas de automatización y realizar pruebas en redes simuladas mediante GNS3.

## 3. Recursos consultados: síntesis y enlaces

### 3.1. Documentación oficial de Python

**Enlace:** https://docs.python.org/es/3/tutorial/

Este tutorial explica los fundamentos de Python mediante ejemplos y ejercicios. Incluye temas como variables, listas, diccionarios, ciclos, condiciones y funciones.

**Utilidad:** permite consultar la sintaxis y aprender a organizar los datos de los dispositivos de red dentro del programa `dispositivos.py`.

### 3.2. Documentación oficial de GNS3

**Enlace:** https://docs.gns3.com/docs/

Este recurso contiene guías e instrucciones para crear topologías, configurar dispositivos y solucionar problemas de simulación de redes.

**Utilidad:** permite construir entornos virtuales para probar la conectividad entre routers y switches antes de realizar actividades de automatización.

### 3.3. Repositorio oficial de Netmiko

**Enlace:** https://github.com/ktbyers/netmiko

Este repositorio contiene el código fuente, las instrucciones de instalación y ejemplos de la biblioteca Netmiko, utilizada para facilitar conexiones de administración con dispositivos de red compatibles.

**Utilidad:** permite investigar cómo establecer conexiones SSH desde Python y ejecutar comandos para obtener información de los dispositivos.

### 3.4. Stack Overflow en español

**Enlace:** https://es.stackoverflow.com/questions

Es una comunidad de preguntas y respuestas sobre programación donde los usuarios comparten problemas técnicos y posibles soluciones.

**Utilidad:** permite buscar errores similares a los que pueden aparecer al desarrollar el programa de automatización y comparar las soluciones propuestas.

### 3.5. GitHub Discussions

**Enlace:** https://github.com/orgs/community/discussions

Es un espacio de discusión donde los usuarios pueden compartir dudas, ideas y experiencias relacionadas con GitHub y el desarrollo colaborativo.

**Utilidad:** ayuda a comprender buenas prácticas para organizar repositorios y colaborar en proyectos de software.

## 4. Evaluación de confiabilidad: tabla comparativa

| Criterio | Python | GNS3 | Netmiko |
|---|---|---|---|
| **¿Quién mantiene el recurso?** | Python Software Foundation y colaboradores. | Equipo de GNS3. | Kirk Byers y colaboradores. |
| **¿La información corresponde al tema?** | Sí, aborda el lenguaje Python. | Sí, aborda la simulación y configuración de redes. | Sí, aborda la automatización de conexiones con dispositivos de red. |
| **¿Incluye ejemplos o instrucciones?** | Sí, incluye tutoriales y ejemplos de código. | Sí, incluye guías y procedimientos de configuración. | Sí, incluye instrucciones de instalación y ejemplos de uso. |
| **¿Se identifica la versión o actualización?** | La documentación se organiza por versiones de Python. | Deben revisarse las instrucciones correspondientes a la versión utilizada. | El repositorio muestra versiones y cambios del proyecto. |
| **¿Puede comprobarse con otra fuente?** | Sí, ejecutando los ejemplos y comparándolos con otras referencias. | Sí, realizando pruebas de conectividad en GNS3. | Sí, verificando los ejemplos con dispositivos compatibles y su documentación. |
| **¿Qué utilidad tiene para el proyecto?** | Ayuda a desarrollar y corregir el código Python. | Permite simular y probar topologías de red. | Permite investigar conexiones SSH y tareas de automatización. |

La evaluación se basa en las características generales observables de estos recursos. Antes de aplicar una solución, es importante revisar la versión, los requisitos y la compatibilidad correspondientes.

## 5. Estrategia de solución del problema

### Situación hipotética

El programa `dispositivos.py` muestra correctamente la información de R1 y R2, pero no identifica un dispositivo cuando se busca por su nombre.

| Elemento | Estrategia propuesta |
|---|---|
| **Problema identificado** | La búsqueda por nombre no encuentra un dispositivo registrado. |
| **Palabras clave** | Python buscar dispositivo por nombre, listas de diccionarios, comparación de cadenas y condiciones `if`. |
| **Primer recurso que consultaríamos** | El tutorial oficial de Python, especialmente las secciones sobre estructuras de datos y control de flujo. |
| **Información que revisaríamos** | Los nombres almacenados, la variable de entrada, las condiciones de comparación, la indentación y el recorrido de la lista de dispositivos. |
| **Tipo de solución que buscaríamos** | Un ejemplo que recorra una lista de diccionarios y compare el nombre ingresado con el nombre almacenado. |
| **Cómo comprobaríamos la solución** | Probaríamos con R1, R2 y un nombre inexistente para verificar que los resultados sean correctos. |
| **Cómo documentaríamos el resultado** | Registraríamos la causa del error, el recurso consultado, la solución aplicada y los resultados de las pruebas. |

La estrategia consiste en identificar primero la causa probable, consultar información confiable, adaptar la solución al código existente y comprobar el resultado antes de incorporarlo definitivamente.

## 6. Aprendizajes obtenidos

Durante esta práctica aprendí que la documentación oficial permite comprender el funcionamiento de las herramientas y consultar ejemplos confiables. También identifiqué que los repositorios de GitHub permiten revisar el código, las versiones y las instrucciones de instalación de las bibliotecas.

Además, comprendí que las comunidades de programación ayudan a encontrar soluciones a problemas similares, pero que las respuestas deben verificarse antes de utilizarlas. La compatibilidad de versiones y dispositivos también es importante para evitar errores durante la automatización de redes.

Finalmente, aprendí que organizar los enlaces, las explicaciones y los resultados de las pruebas permite construir una base de conocimiento útil para futuras modificaciones del proyecto.

## 7. Conclusiones individuales

### Integrante Jonathan de Jesus de Luna Garcia

Durante esta práctica aprendí que la documentación oficial es una herramienta importante para desarrollar programas correctamente.  
Comprendí que Python cuenta con tutoriales y ejemplos que ayudan a resolver dudas sobre el código.  
También aprendí que las listas y los diccionarios permiten organizar la información de los dispositivos de red.  
La documentación de GNS3 me permitió conocer recursos para construir y configurar redes virtuales.  
Además, comprendí que es importante verificar la información antes de aplicarla a un proyecto.  
Las comunidades de programación permiten encontrar soluciones a problemas que otras personas ya han experimentado.  
Estos conocimientos pueden ayudarme a mejorar el programa `dispositivos.py` y corregir posibles errores.  
En conclusión, investigar y utilizar recursos confiables facilita el aprendizaje y el desarrollo de proyectos de automatización de redes.

### Integrante Victor Martinez Curiel

Esta práctica me ayudó a comprender la importancia de consultar diferentes recursos para resolver problemas técnicos.  
Aprendí que GitHub permite revisar el código fuente, las versiones y las instrucciones de instalación de diferentes bibliotecas.  
También conocí Netmiko, una biblioteca que facilita la administración de dispositivos de red mediante conexiones compatibles.  
Comprendí que antes de utilizar una biblioteca es necesario revisar sus requisitos y plataformas compatibles.  
Otro aprendizaje fue que las comunidades, como Stack Overflow, permiten consultar experiencias y soluciones de otros programadores.  
Sin embargo, las respuestas encontradas deben revisarse y probarse antes de utilizarlas.  
Estos recursos pueden ayudar al equipo a desarrollar nuevas funciones para nuestro proyecto integrador.  
En conclusión, investigar, verificar y documentar la información permite crear programas más confiables y fáciles de mantener.

### Integrante Joshua Garcia Huerta

Al realizar esta práctica aprendí que no todas las fuentes de información tienen el mismo nivel de confiabilidad.  
Por eso, es importante revisar quién publica los recursos, qué información contienen y si están actualizados.  
La documentación de Python ayuda a comprender las instrucciones y a solucionar errores de programación.  
Por otra parte, GNS3 permite practicar la configuración de redes sin depender únicamente de equipos físicos.  
También comprendí que Netmiko puede utilizarse para investigar cómo automatizar tareas en dispositivos compatibles.  
Las comunidades de colaboración ayudan a compartir conocimientos y encontrar diferentes alternativas para resolver problemas.  
En nuestro proyecto, estos recursos pueden servir para mejorar la búsqueda y administración de routers y switches.  
En conclusión, utilizar información confiable y comprobar las soluciones permite aprender mejor y desarrollar un proyecto de automatización más eficiente.

