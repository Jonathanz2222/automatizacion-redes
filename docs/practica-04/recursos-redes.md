# Parte 3. Explorar documentación y comunidades de redes

## Paso 4. Investigar recursos de GNS3 y automatización de redes

### 1. ¿Qué tipo de problema podrías resolver consultando la documentación de GNS3?

La documentación de GNS3 permite resolver problemas relacionados con la creación de topologías, conexión de dispositivos, configuración de interfaces, instalación de máquinas virtuales y solución de errores al iniciar routers o switches.

### 2. ¿Qué diferencia existe entre la documentación de una herramienta y el repositorio de una biblioteca?

La documentación de una herramienta explica cómo instalarla, configurarla y utilizar sus funciones. El repositorio de una biblioteca contiene su código fuente, instrucciones de instalación, ejemplos, versiones y cambios realizados por sus desarrolladores.

### 3. ¿Qué información revisarías antes de utilizar una biblioteca de automatización?

Revisaría su instalación, requisitos, versión de Python, dependencias, ejemplos de uso, funciones disponibles, dispositivos compatibles y medidas de seguridad para establecer conexiones con los equipos de red.

### 4. ¿Por qué es importante comprobar qué plataformas y funciones admite una biblioteca?

Porque no todas las bibliotecas funcionan con todos los fabricantes, sistemas operativos o modelos de dispositivos. Verificar la compatibilidad evita errores y permite elegir una herramienta adecuada para realizar las tareas de automatización.

### 5. ¿Cómo podrían utilizarse estos recursos en las siguientes prácticas?

La documentación de GNS3 permitiría construir y configurar topologías para probar la conectividad. El repositorio de Netmiko ayudaría a aprender cómo conectarse a dispositivos mediante SSH y ejecutar comandos. Estos recursos también servirían para desarrollar programas en Python que consulten información de routers y switches y faciliten tareas de administración de redes.

---

## Recursos técnicos consultados

### Recurso 1: Documentación oficial de GNS3

- **URL:** https://docs.gns3.com/docs/
- **Tema:** Creación, configuración y administración de topologías de red.
- **Tipo de información:** Tutoriales, instrucciones, ejemplos y solución de problemas.
- **Utilidad para el proyecto integrador:** Permite construir una red virtual para probar dispositivos y verificar su conectividad antes de automatizar tareas.
- **Ejemplo de consulta:** La utilizaría si necesito conectar dos routers en GNS3 y comprobar que pueden comunicarse mediante `ping`.

### Recurso 2: Repositorio oficial de Netmiko en GitHub

- **URL:** https://github.com/ktbyers/netmiko
- **Tema:** Automatización de conexiones SSH con dispositivos de red.
- **Tipo de información:** Código fuente, instrucciones de instalación, ejemplos, documentación y lista de plataformas compatibles.
- **Utilidad para el proyecto integrador:** Permite investigar cómo crear un programa en Python que se conecte a equipos de red y ejecute comandos para consultar su información.
- **Ejemplo de consulta:** Lo utilizaría para aprender a establecer una conexión SSH con un router compatible y obtener información de sus interfaces.

### Recurso 3: Plataformas compatibles con Netmiko

- **URL:** https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md
- **Tema:** Fabricantes, sistemas operativos y dispositivos de red compatibles con Netmiko.
- **Tipo de información:** Listado de plataformas probadas, con pruebas limitadas o experimentales.
- **Utilidad para el proyecto integrador:** Ayuda a comprobar si los dispositivos que se desean automatizar son compatibles con la biblioteca.
- **Ejemplo de consulta:** Revisaría la lista antes de intentar conectar mi programa de Python a un router Cisco IOS o a un equipo de otro fabricante.

---

## Conclusión

La documentación de GNS3 y los recursos de Netmiko son importantes para aprender a diseñar, configurar y automatizar redes. Consultarlos permite resolver problemas técnicos, conocer las funciones disponibles y comprobar la compatibilidad de los dispositivos. Estos conocimientos ayudarán a desarrollar un programa en Python que facilite la administración y consulta de información de routers y switches.
