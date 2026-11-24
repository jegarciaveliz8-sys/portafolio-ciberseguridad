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

*Desarrollado como evidencia de competencias técnicas en ingeniería de seguridad e infraestructura.*
