import socket
import time
from ping3 import ping

class NetworkDiagnostics:
    """
    Módulo encargado de ejecutar pruebas de rendimiento de red
    como medición de Latencia RTT, verificación de puertos e inspección DNS.
    """

    @staticmethod
    def measure_latency(host="8.8.8.8", count=4):
        successful_pings = 0
        total_rtt = 0

        for _ in range(count):
            try:
                response_time = ping(host, timeout=1)
                if response_time is not None and response_time is not False:
                    successful_pings += 1
                    total_rtt += (response_time * 1000)
            except Exception:
                pass
            time.sleep(0.2)

        packet_loss = ((count - successful_pings) / count) * 100
        avg_latency = (total_rtt / successful_pings) if successful_pings > 0 else 0.0

        return {
            "target": host,
            "packets_sent": count,
            "packets_received": successful_pings,
            "packet_loss_percent": round(packet_loss, 2),
            "avg_latency_ms": round(avg_latency, 2),
            "status": "ONLINE" if successful_pings > 0 else "OFFLINE"
        }

    @staticmethod
    def check_dns_resolution(domain="google.com"):
        start_time = time.time()
        try:
            ip_address = socket.gethostbyname(domain)
            elapsed_time = (time.time() - start_time) * 1000
            return {
                "domain": domain,
                "resolved_ip": ip_address,
                "resolution_time_ms": round(elapsed_time, 2),
                "status": "SUCCESS"
            }
        except socket.gaierror:
            return {
                "domain": domain,
                "resolved_ip": "N/A",
                "resolution_time_ms": 0.0,
                "status": "FAILED"
            }