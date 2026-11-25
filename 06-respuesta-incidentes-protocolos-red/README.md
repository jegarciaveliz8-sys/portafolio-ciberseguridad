# Respuesta a Incidentes y Análisis Forense de Protocolos de Red

## 1. Escenario y Detección
Simulación y triaje forense de un incidente multi-vector a nivel de paquete (`PCAP`):
- **Reconocimiento (TCP SYN Scan):** Detección de paquetes TCP con bandera `SYN` aislada sobre los puertos `[21, 22, 80, 443, 3306, 8080]`.
- **Exfiltración de Datos (DNS Tunneling):** Identificación de consultas DNS anómalas transportando credenciales y tokens codificados en subdominios.

## 2. Triaje Forense Automatizado
Desarrollo de analizador en Python con **Scapy** ([analizador_pcap.py](analizador_pcap.py)) para extraer automáticamente Indicadores de Compromiso (`IoCs`) desde capturas `.pcap`.

## 3. Contención Perimetral
Implementación de política restrictiva en cortafuegos **UFW** (`Default: deny incoming`, `allow outgoing`) y habilitación de registros de auditoría (`ufw logging on`) para bloquear conexiones entrantes no autorizadas.
