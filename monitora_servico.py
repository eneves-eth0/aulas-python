import subprocess

SERVICES = {
   'ssh': 'ssh',
   'apache2': 'apache2',
   'mysql': 'mysql'
}

def check_service(service_name):
   try:
      status_result = subprocess.run(['systemctl','is-active',service_name], check=True, text=True, capture_output=True)
      if status_result.stdout.strip() == 'active':
         print(f"Serviço {service_name} está ativo")
      else:
         raise Exception(f"Serviço {service_name} está inativo")
   except subprocess.CalledProcessError:
      print(f"Reiniciando o serviço {service_name}...")
      restart_result = subprocess.run(['systemctl','restart',service_name], text=True, capture_output=True)
      if restart_result.returncode == 0: 
         print(f"Serviço reiniciado com sucesso {service_name}")
      else:
         print(f"Falha ao iniciar o serviço {service_name}")


def main():
   for service in SERVICES.values():
      check_service(service)

if __name__ == '__main__':
   main()
