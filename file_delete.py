import os
import shutil
from datetime import datetime, timedelta

#configurações
days_old = 30
folder_path = '/path/to/cleanup'

def delete_old_files(folder):
   current_time = datetime.now()
   for filename in os.listdir(folder):
      file_path = os.path.join(folder, filename)
      if os.path.isfile(file_path):
         file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
         if current_time - file_modified_time > timedelta(days=days_old):
            os.remove(file_path)
            print(f"Arquivo removido: {file_path}")

def delete_empty_dirs(folder):
   for dirpath, dirnames, filenames in os.walk(folder, topdown=False):
      if not dirnames and not filenames:
         os.rmdir(dirpath)
         print(f"Diretorio vazio removido: {dirpath}")

def main():
   delete_old_files(folder_path)
   delete_empty_dirs(folder_path)
   print("Limpeza do disco concluida")

if __name__ == "__main__":
   main()
