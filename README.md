# Avance del proyecto integrador

## 1. Práctica 1: Mi estación de automatización de redes

**Estado:** Completada.

### Propósito

Configurar un entorno colaborativo e instalar las herramientas necesarias para la automatización de redes, documentando su instalación y verificación.

### Herramientas instaladas y configuración

- **Entorno de desarrollo:** Python 3, VS Code y un entorno virtual configurado.
- **Control de versiones y utilidades:** Git, con usuario y correo configurados, GitHub, Postman, OpenConnect y Docker.
- **Laboratorio virtual:** VMware Workstation Pro con la máquina virtual GNS3 VM integrada a GNS3 GUI.

### Verificación del entorno

Se verificó el correcto funcionamiento de:

- Python 3.
- Ejecuciones de código en VS Code mediante `hola_mundo.py`.
- Vinculación del repositorio con GitHub.
- Contenedores Docker.
- Integración de la GNS3 VM con GNS3 GUI.

---

## 2. Práctica 2: Construcción de la red simulada en GNS3

**Estado:** Completada.

### Infraestructura construida

- **Topología 1:** Red básica de Capa 2 compuesta por dos hosts virtuales (VPCS) conectados a través de un switch Ethernet básico.

- **Topología 2:** Red de laboratorio de Capa 3 estructurada con dos routers Cisco (IOSv) y un switch multicapa (IOSvL2).

- **Direccionamiento IP:** Asignación de direcciones IP estáticas en las interfaces de red de hosts y routers, así como en interfaces virtuales (VLAN 1 y Loopback 0).

- **Conectividad:** Verificación de conectividad de red punto a punto mediante pruebas de `ping` exitosas entre hosts y entre routers.

- **Protocolo de enrutamiento:** Habilitación y configuración del protocolo dinámico OSPF en el Área 0 entre los routers.

- **Verificación:** Validación de la vecindad OSPF mediante `show ip ospf neighbor` y análisis de la tabla de enrutamiento mediante `show ip route`.

### Próximo paso

Desarrollo e integración de scripts en Python, APIs y herramientas para la automatización de tareas sobre la infraestructura de red virtualizada.