import subprocess

def update_system():
  try:
     print("Atualizando a lista de pacotes...")
     subprocess.run(['sudo','apt', 'update'], check=True)
     print("Lista de pacotes atualizada")
     
     print("Aplicando atualizações disponiveis...")
     subprocess.run(['sudo','apt','upgrade','-y'], check=True)
     print("Atualizações feitas com sucesso")

  except subprocess.CalledProcessError as e:
     print(f"Erro ao executar atualização: {e}")

def main():
   update_system()

if __name__ == "__main__":
   main()
