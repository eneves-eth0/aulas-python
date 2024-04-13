import subprocess

def add_user(username, password):

   try:
      subprocess.run(['sudo', 'useradd', '-m', username], check=True)
      proc = subprocess.Popen(['sudo', 'passwd', username], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
      proc.communicate(input=f"{password}\n{password}\n".encode('utf-8'))
      print(f"Usuário {username} adicionado com sucesso")
   except subprocess.CalledProcessError as e:
      print(f"Erro ao adicionar o usuario: {username} {e}")


def remove_user(usarname):
   try:
      subprocess.run(['sudo','userdel', '-r', username], check=True)
      print(f"Usuario {username} removido com sucesso")
   except subprocess.CalledProcessError as e: 
      print(f"Erro ao remover o usuário")

def main():
   add_user('aula', 'senha123')
   remove_user('aula')

if __name__ == "__main__":
   main()
