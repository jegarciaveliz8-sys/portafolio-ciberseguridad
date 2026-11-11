import json

def auditar_usuarios():
    print("🔍 Iniciando auditoría de accesos e identidades en la nube...")
    
    # Simulación de datos de políticas IAM
    usuarios_nube = [
        {"usuario": "admin-sistema", "permiso": "AdministratorAccess", "riesgo": "CRÍTICO"},
        {"usuario": "juan-dev", "permiso": "ReadOnlyAccess", "riesgo": "BAJO"}
    ]
    
    hallazgos = [u for u in usuarios_nube if u["riesgo"] == "CRÍTICO"]
    
    # Generar reporte JSON
    with open("reporte_riesgos.json", "w") as f:
        json.dump(hallazgos, f, indent=4)
        
    print(f"✅ Auditoría finalizada. Hallazgos críticos detectados: {len(hallazgos)}")

if __name__ == "__main__":
    auditar_usuarios()
