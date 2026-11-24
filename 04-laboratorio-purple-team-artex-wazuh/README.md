# Laboratorio Purple Team: Ataque Autónomo (ARTEX) + Detección SIEM (Wazuh)

## Arquitectura del Ejercicio
Este laboratorio integra capacidades ofensivas (**Red Team**) y defensivas (**Blue Team / Detection Engineering**) para validar la visibilidad ante ataques web en tiempo real:

1. **Vector Ofensivo (ARTEX + AI Gateway):** Agentes autónomos ejecutando pruebas OWASP Top 10 (XSS Reflejado, SQL Injection y Remote Command Execution) contra una aplicación web instrumentada (`DVWA`).
2. **Ingesta de Telemetría:** Recolección continua de logs de acceso HTTP (`web-accesslog`) hacia el servidor **Wazuh Manager v4.8.0**.
3. **Ingeniería de Detección (`local_rules.xml`):** Creación de reglas personalizadas de severidad crítica (Niveles 12 y 13) con mapeo **MITRE ATT&CK** (`T1190` - *Exploit Public-Facing Application* y `T1059` - *Command and Scripting Interpreter*).

## Reglas Personalizadas Implementadas
- **Rule ID `100100` (Nivel 12):** Correlaciona intentos de ataque web que devuelven código `HTTP 200 OK`, confirmando explotación exitosa.
- **Rule ID `100101` (Nivel 13):** Detecta intentos de ejecución remota de comandos (RCE) mediante inspección de payloads en URL (`/etc/passwd`, `whoami`, `cat`).

Archivo de reglas listo para despliegue: [local_rules.xml](local_rules.xml)
