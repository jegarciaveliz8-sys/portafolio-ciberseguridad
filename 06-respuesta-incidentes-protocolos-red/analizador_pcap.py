import sys
from scapy.all import rdpcap, TCP, DNS, DNSQR

def analizar_incidente(archivo_pcap):
    paquetes = rdpcap(archivo_pcap)
    print(f"Total de paquetes analizados: {len(paquetes)}")

    syn_ports = []
    dns_queries = []

    for p in paquetes:
        if p.haslayer(TCP) and p[TCP].flags == "S":
            syn_ports.append(p[TCP].dport)
        if p.haslayer(DNS) and p.haslayer(DNSQR):
            q = p[DNSQR].qname.decode(errors="ignore").rstrip(".")
            if len(q) > 25:
                dns_queries.append(q)

    print("1. Puertos sondeados (TCP SYN Scan):", sorted(set(syn_ports)))
    print("2. Consultas DNS anomalas / posible exfiltracion:")
    for q in sorted(set(dns_queries)):
        print("   -> IoC DNS:", q)

if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "captura_incidente.pcap"
    analizar_incidente(ruta)
