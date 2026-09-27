## Descripción de las topologías

A continuación se describen brevemente las dos topologías utilizadas en la práctica.

### 1. Topología 1 — Red básica PC-Switch-PC

Consiste en una topología sencilla de **Capa 2**, formada por dos equipos **VPCS** (`PC1` y `PC2`) conectados a un **Ethernet Switch**.

Esta topología permitió:

- Familiarizarse con el entorno de **GNS3**.
- Personalizar los íconos de los dispositivos.
- Configurar direcciones IP estáticas mediante el comando `ip`.
- Probar la conectividad entre los equipos.
- Guardar la configuración utilizando el comando `save`.

### 2. Topología 2 — Red de routers y switch multicapa

Consiste en una infraestructura más avanzada de **Capa 3**, compuesta por:

- Dos routers Cisco (`R1` y `R2`) utilizando la imagen **Cisco IOSv**.
- Un switch multicapa (`S1`) utilizando la imagen **Cisco IOSvL2**.

En esta topología se realizaron las siguientes configuraciones:

- Asignación de direcciones IP.
- Configuración de interfaces **Loopback**.
- Configuración de **VLAN 1**.
- Implementación del protocolo de enrutamiento dinámico **OSPF** en el **Área 0**.
- Guardado de cambios mediante el comando `write`.
- Verificación de las vecindades OSPF.
- Inspección y verificación de las tablas de enrutamiento.