# Gestión de Amenazas: Hardening y Presencia en Internet (ASM)

## 1. Diagnóstico Inicial de Superficie Pública (Attack Surface Management)
Mediante análisis de cabeceras HTTP y auditoría de configuración en despliegue en la nube se identificaron las siguientes brechas de exposición:
- Ausencia de política **HSTS** (`Strict-Transport-Security`), permitiendo posibles ataques de degradación SSL/TLS.
- Cookies de sesión y protección CSRF sin atributos `Secure` ni `HttpOnly`.

## 2. Controles de Endurecimiento Aplicados (Hardening)
Se implementó una capa de endurecimiento en producción:
- **Transporte Estricto (`HSTS`):** `SECURE_HSTS_SECONDS = 31536000` con `includeSubDomains` y `preload`.
- **Protección de Cookies:** Activación de `SESSION_COOKIE_SECURE`, `SESSION_COOKIE_HTTPONLY`, `CSRF_COOKIE_SECURE` y `CSRF_COOKIE_HTTPONLY`.
- **Defensa contra XSS y Clickjacking:** `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff` y `Referrer-Policy: same-origin`.
- **Auditoría de Host Linux (`Lynis`):** Evaluación continua de parámetros del kernel, permisos `UMASK` y superficie de servicios locales.
