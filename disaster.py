import subprocess 
import os

backup_directory = '/path/to/backup'
data_directory = '/path/to/data'
services_to_restart = ['nginx', 'mysql']

def restore_backup(backup_file, targe_directory):
  try:
    subprocess.run(['tar','-xzf', backup_file, '-C', target_directory], check=True)
    print(f"Backup {backup_file} restaurado com sucesso para {target_directory} ")
  except subprocess.CalledProcessError as e: 
    print(f"Erro ao restaurar backup {backup_file}: {e}")

def restart_services(services):
   for service in services:
      try: 
         subprocess.run(['systemctl', 'restart', service], check=True)
         print(f"Serivço {service} reiniciado com sucesso")
      except subprocessCallledProcessError as e:
         print(f"Erro ao iniciar o serviço {service}: {e}")
def check_system():
   try:
      for service in services_to_restart:
         result = subprocess.run(['systemctl', 'is-active', service], check=True, capture_output=True)
         if result.stdout.decode().strip() == 'active':
            print(f"Serviço {service} está rodando")
         else:
            print(f"Serviço {service} não está rodando")
   except subprocess.CalledProcessError as e:
      print(f"Error ao verificar estado do serviço: {e}")

def main()
   latest_backup = max([os.path.join(backup_directory, f) for f in os.listdir(bakcup_directory)], key=os.path.getctime)
   restore_backup(latest_backup, data_directory)
   restart_services(services_to_restart)

   check_system()

if __name__ == "__main__":
  main() 







