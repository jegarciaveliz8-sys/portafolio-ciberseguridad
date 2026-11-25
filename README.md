# Portafolio de Ciberseguridad

Repositorio práctico enfocado en automatización de seguridad, DevSecOps y auditoría de sistemas en la nube.

## 🛠️ Proyectos Incluidos en este Repositorio

### 1. Pipeline de DevSecOps (CI/CD Seguro)
- **Ubicación:** `.github/workflows/security-scan.yml`
- **Herramientas:** GitHub Actions, Gitleaks.
- **Descripción:** Automatización de integración continua configurada para escanear de forma estática el código fuente en busca de secretos, tokens o credenciales expuestas antes de llegar a producción.

### 2. Auditoría de Identidades en la Nube
- **Ubicación:** `cloud_audit.py`
- **Lenguaje:** Python.
- **Descripción:** Script diseñado para evaluar políticas de control de acceso (IAM), identificar cuentas con privilegios excesivos (sobreprivilegios) y generar reportes estructurados en formato JSON.

---

### 3. Auditoría Automatizada OWASP Top 10 con Agentes Autónomos y AI Gateway
- **Ubicación:** [03-auditoria-pentest-autonomo-artex/](03-auditoria-pentest-autonomo-artex/)
- **Documentos:** [Reporte Técnico](03-auditoria-pentest-autonomo-artex/README.md) | [Metodología Paso a Paso](03-auditoria-pentest-autonomo-artex/METODOLOGIA.md) | [Informe PDF](03-auditoria-pentest-autonomo-artex/reporte_pentest.pdf)
- **Herramientas:** ARTEX (Multi-Agent Pentesting), LiteLLM AI Gateway, Docker, Python, Pandoc/WeasyPrint.
- **Descripción:** Implementación de una arquitectura de pentesting autónomo respaldada por un AI Gateway centralizado con balanceo de carga y failover automático entre múltiples proveedores LLM. Ejecución de auditorías OWASP Top 10, generación de informes ejecutivos con evidencia HTTP reproducible (PoC) y aplicación de parches de remediación en ciclo DevSecOps (`DEBUG=False` y control de acceso en APIs REST).


### 4. Laboratorio Purple Team: Ataque Autónomo (ARTEX) y Detección SIEM (Wazuh)
- **Ubicación:** [04-laboratorio-purple-team-artex-wazuh/](04-laboratorio-purple-team-artex-wazuh/)
- **Archivos:** [Documentación del Laboratorio](04-laboratorio-purple-team-artex-wazuh/README.md) | [Reglas SIEM (local_rules.xml)](04-laboratorio-purple-team-artex-wazuh/local_rules.xml)
- **Áreas y Competencias:** `Arquitectura de Contenedores Docker` | `Seguridad de Red y Segmentación` | `Seguridad en APIs & AppSec` | `SOC / SIEM Detection Engineering`
- **Herramientas:** Wazuh SIEM (v4.8.0), ARTEX, LiteLLM AI Gateway, Docker, MITRE ATT&CK.
- **Descripción:** Simulación de ataques web automatizados (XSS y RCE) correlacionados en tiempo real con Wazuh SIEM. Desarrollo de reglas personalizadas de detección crítica (niveles 12 y 13) mapeadas a técnicas MITRE ATT&CK (`T1190`, `T1059`).


### 5. Gestión de Amenazas: Hardening y Presencia en Internet (ASM)
- **Ubicación:** [05-hardening-y-superficie-ataque/](05-hardening-y-superficie-ataque/)
- **Áreas y Competencias:** `Attack Surface Management (ASM)` | `Web & Cloud Hardening` | `Linux Security Auditing`
- **Herramientas:** Lynis, cURL, Django Security Middleware, TLS/HSTS.
- **Descripción:** Evaluación de superficie de ataque externa mediante análisis de cabeceras HTTP y auditoría de sistema con Lynis. Implementación de controles de endurecimiento en producción (HSTS de 1 año con preload, cookies `Secure`/`HttpOnly` y políticas anti-clickjacking).

*Desarrollado como evidencia de competencias técnicas en ingeniería de seguridad e infraestructura.*
