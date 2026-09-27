# Mi estación de automatización de redes

## 1. Datos del equipo

**Integrantes:**

* Jonathan De Jesus De Luna Garcia
* Joshua Garcia Huerta
* Victor Martinez Curiel

---

## 2. Propósito de la práctica

El propósito de esta práctica es preparar y configurar una estación de trabajo completa dedicada a la automatización de redes.

Se busca establecer un entorno integrado que combine herramientas de programación, control de versiones, contenedores, pruebas de API y virtualización de redes, sentando las bases necesarias para desarrollar, probar y desplegar scripts de automatización sobre arquitecturas de red virtuales y reales.

---

## 3. Herramientas instaladas

Durante el desarrollo de la práctica se instalaron y verificaron las siguientes herramientas indispensables para el flujo de trabajo:

* **Python 3:** Lenguaje de programación principal para el desarrollo de scripts de automatización.
* **Visual Studio Code:** Editor de código fuente con extensiones para Python y control de versiones.
* **Git y Git Bash:** Sistema de control de versiones distribuido y terminal orientada a comandos Unix/Git en Windows.
* **GitHub:** Plataforma de hospedaje para el repositorio colaborativo del proyecto.
* **Postman:** Cliente para la prueba, interacción y documentación de APIs REST.
* **OpenConnect GUI:** Cliente VPN para conexiones seguras a entornos de red y laboratorios remotos.
* **Docker Desktop:** Plataforma de contenedores para la ejecución de servicios de red e imágenes livianas.
* **GNS3 (GUI y VM):** Emulador de redes para la simulación de topologías y dispositivos.
* **VMware Workstation Pro:** Hipervisor utilizado para alojar la máquina virtual de GNS3 VM.

---

## 4. Configuración realizada

### 4.1 Entorno de desarrollo Python

* Instalación de Python 3 y validación del intérprete.
* Configuración de la extensión oficial de Python en Visual Studio Code.
* Creación y activación de un entorno virtual (`venv`) dentro del directorio del proyecto.

### 4.2 Control de versiones colaborativo

* Instalación de Git y Git Bash.
* Configuración de la identidad global de usuario (`user.name` y `user.email`).
* Creación del repositorio remoto en GitHub denominado `automatizacion-redes`.

### 4.3 Herramientas de red y virtualización

* Instalación de Docker Desktop y actualización del Kernel de Linux para WSL 2.
* Instalación de OpenConnect GUI a través de su ejecutable oficial para Windows.
* Importación de la imagen `GNS3 VM.ova` en VMware Workstation Pro.
* Integración y vinculación entre la interfaz de GNS3 GUI y la máquina virtual GNS3 VM.

---

## 5. Verificación del entorno

Para asegurar el funcionamiento correcto de la estación de automatización, se ejecutaron las siguientes pruebas de verificación:

* **Python:** Ejecución exitosa del script de prueba `hola_mundo.py` en el entorno virtual activo a través de VS Code.
* **Git / GitHub:** Vinculación exitosa del repositorio local con el servidor remoto y realización de envíos de cambios (`commit` y `push`).
* **Docker:** Inicio correcto del servicio de Docker Desktop y verificación mediante la ejecución de contenedores de prueba.
* **GNS3:** Confirmación de estado verde/activo para los servidores local y GNS3 VM dentro del panel de estado de GNS3 GUI.

---

## 6. Estructura del proyecto

La estructura de carpetas configurada en el repositorio para la organización del código, datos y documentación es la siguiente:

```text
automatizacion-redes/
├── data/
│   └── .gitkeep
├── docs/
│   └── 01-estacion-automatizacion/
│       └── evidencias/
│           ├── 01-python.png
│           ├── 02-vscode.png
│           ├── ...
│           └── 16-integracion-gns3.png
├── src/
│   ├── .gitkeep
│   └── hola_mundo.py
├── tests/
│   └── .gitkeep
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 7. Problemas encontrados y soluciones

### Problema 1: Docker Desktop no iniciaba

**Problema:** Docker Desktop no iniciaba correctamente y mostraba el error:

> `WSL 2 installation is incomplete`

**Solución:** Se descargó e instaló manualmente la actualización del paquete del Kernel de Linux para WSL 2 desde el enlace oficial (`aka.ms/wsl2kernel`). Posteriormente, se ejecutó el comando `wsl --update` en la consola de comandos de Windows con privilegios de administrador, permitiendo que Docker iniciara correctamente.

### Problema 2: Git no era reconocido en VS Code

**Problema:** Al intentar ejecutar comandos de Git desde la terminal integrada de Visual Studio Code (PowerShell), el sistema devolvía un error indicando que el comando `git` no se reconocía.

**Solución:** Se seleccionó **Git Bash** como el perfil de terminal predeterminado dentro de Visual Studio Code, permitiendo la ejecución de comandos como:

```bash
git add
git commit
git push
```

---

## 8. Conclusiones

La preparación de una estación de automatización de redes es un paso fundamental antes de abordar tareas de programación sobre infraestructura de TI. La integración de herramientas de desarrollo con emuladores de red como GNS3 y plataformas de contenedores como Docker permite simular escenarios reales dentro de un entorno controlado y seguro.

Además, el uso del control de versiones mediante Git y GitHub facilitó el trabajo en equipo y la organización estructurada del proyecto.

La resolución de las dependencias del sistema, como WSL 2 para Docker y la configuración de terminales en VS Code, permitió comprender mejor la interacción entre el sistema operativo base y las diferentes herramientas utilizadas para la automatización de redes.