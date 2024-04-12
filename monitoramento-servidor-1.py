import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Configuração do servidor de e-mail
email_sender = 'seu_email@exemplo.com.br'
email_password = 'minha_senha'
email_receiver = 'destino@exemplo.com.br'

# Limites de alerta
CPU_THRESHOLD = 85
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 85

def send_alert(message):
   msg = MIMEMultipart()
   msg['From']  = email_sender
   msg['To'] = email_receiver
   msg['Subject']  = 'Alerta de monitoramento do servidor'

   msg.attach(MIMEText(message,'plain'))

   try:
     server = smtplib.SMTP('smtp.example.com', 587)
     server.starttls()
     server.login(email_sender,email_password)
     text = msg.as_string()
     server.sendmail(email_sender,email_receiver,text)
     server.quit()
     print("Alerta enviado com sucesso por e-mail")
   
   except Exception as e:
     print(f"Falha ao enviar o alerta por email: {e}")

def check_system():
   cpu_usage = psutil.cpu_percent(interval=1)
   memory = psutil.virtual_memory()
   disk = psutil.disk_usage('/')
   
   messages = []
   if cpu_usage > CPU_THRESHOLD:
      messages.append(f"Uso de cpu elevado: {cpu_usage}%")
   if memory.percent > MEMORY_THRESHOLD: 
      messages.append(f"Uso de memoria elevado: {memory.percent}")
   if disk.percent > DISK_THRESHOLD:
      messages.append(f"Uso de disco elevado: {disk.percent}")

   if messages:
      alert_message = "\n".join(messages)
      print(alert_message)
      #send_alert(alert_message)
   else:
      print("Todos os parametros estão ok")

if __name__ == "__main__":
   check_system()





























