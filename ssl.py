import ssl
import socket
from datetime import datetime
from OpenSSL import crypto
import smtplib
from email.mime.text import MIMEText

#Configurando variaveis e-mail
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_user = 'meuemail@example.com'
smtp_password = '123'
email_sender = 'meuemail@example.com'
email_receiver = 'seuemail@outrosite.com'

def check_ssl_expiry(domain, port=443):
  ssl_context = ssl.create_default_context()
  conn = ssl_context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
  conn.settimeout(10.0)

  try:
     conn.connect((domain,port))
     ssl_info = conn.getpeercert()
     expiry_date = datetime.srtptime(ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
     return expiry_date
  except Exception as e:
     print(f"Erro ao conectar no servidor {domain}: {e}")
  finally:
     conn.close()

def main():
   domains = ['obsevability.works', 'uol.com.br', 'google.com.br']
   for domain in domains:
      expiry_date = check_ssl_expiry(domain)
      print(expiry_date)

if __name__ == "__main__":
   main()











