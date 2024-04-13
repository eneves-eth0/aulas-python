import requests
from ping3 import ping, verbose_ping
from datetime import datetime

#Lista de hosts
hosts = {
    'google': 'www.g2esoogle.com',
    'uol': 'www33.uol.com.br'
}

def check_ping(host):
   response = ping(host, timeout=2)
   if response is None: 
      print(f"[{datetime.now()}] ping para {host} falhou")
   else:  
      print(f"[{datetime.now()}] ping para {host} bem sucedido: {response:.2f} ms")

def check_http(url):
   try: 
     response = requests.get(url,timeout=5)
     if response.status_code == 200:
        print(f"[{datetime.now()}] HTTP GET para {url} bem sucedido status 200")
     else: 
        print(f"[{datetime.now()}] HTTP Get para {url} falhou (status {response.status_code})")
   except requests.RequestException as e:
      print(f"[{datetime.now()}] HTTP GET falhou para {url} motivo: {e}")

def main():
   for name, host in hosts.items():
      check_http(host)
      check_ping(host)

if __name__ == "__main__":
   main()  
