import requests
import socket
from concurrent.futures import ThreadPoolExecutor

# Configuração de cabeçalhos de segurança desejados
SECURITY_HEADERS = [
    'Strict-Transport-Security',
    'Content-Security-Policy',
    'X-Frame-Options',
    'X-Content-Type-Options',
    'X-XSS-Protection',
    'Referrer-Policy'
]

# Portas comuns para verificar em um teste de penetração básico
COMMON_PORTS = [21, 22, 23, 80, 443, 8080]

def check_security_headers(url):
    """Verifica a presença de cabeçalhos de segurança HTTP em uma URL."""
    try:
        response = requests.get(url)
        headers = response.headers
        missing_headers = [h for h in SECURITY_HEADERS if h not in headers]
        if missing_headers:
            print(f"Faltam os seguintes cabeçalhos de segurança em {url}: {missing_headers}")
        else:
            print(f"Todos os cabeçalhos de segurança necessários estão presentes em {url}.")
    except requests.RequestException as e:
        print(f"Erro ao fazer requisição HTTP para {url}: {e}")

def scan_ports(host):
    """Realiza uma varredura básica de portas TCP no host fornecido."""
    open_ports = []
    def scan_port(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Timeout de 1 segundo
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(scan_port, COMMON_PORTS)

    if open_ports:
        print(f"Portas abertas encontradas em {host}: {open_ports}")
    else:
        print(f"Nenhuma porta aberta encontrada em {host}.")

def main():
    url = "https://www.example.com"
    host = "www.example.com"

    # Checagem de cabeçalhos de segurança
    check_security_headers(url)

    # Varredura de portas
    scan_ports(host)

if __name__ == "__main__":
    main()
