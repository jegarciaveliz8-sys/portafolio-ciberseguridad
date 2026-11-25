# Respuesta a Incidentes: Análisis Forense de Red y Contención Cloud WAF

## 1. Triaje Forense de Protocolos (Capa 3/4 y DNS)
Captura y análisis automatizado de paquetes (`PCAP`) mediante Python y **Scapy** ([analizador_pcap.py](analizador_pcap.py)) para extraer Indicadores de Compromiso (`IoCs`) de escaneos sigilosos `TCP SYN` y exfiltración por túnel `DNS`.

## 2. Contención Perimetral y Cloud WAF en Producción (Capa 7)
- **Host Firewall (`UFW`):** Política restrictiva `Default: deny incoming` con auditoría activa.
- **Contención Activa en la Nube ([waf_middleware.py](waf_middleware.py)):** Implementación y despliegue en producción de un middleware WAF que intercepta User-Agents maliciosos (`sqlmap`, `nikto`, `gobuster`) y rutas críticas (`/.env`, `/.git`, `/wp-admin`, `/phpMyAdmin`), respondiendo `403 Forbidden` y generando alertas de telemetría en tiempo real.
