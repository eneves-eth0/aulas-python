import os
from datetime import datetime
import tarfile

#diretorio a ser copiado
SOURCE_DIRECTORY = '/Users/eduardoneves/aulas'

#Diretorio onde o bakcup sera salvo
BACKUP_DIRECTORY = '/Users/eduardoneves/aulas-python/backup'

#nome base do arquivo de backup
BACKUP_NAME = 'backup'

def create_backup(source_dir,backup_dir,backup_name):
   data_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
   backup_filename = f"{backup_name}_{data_str}.tar.gz"
   backup_path = os.path.join(backup_dir,backup_filename)
 
   with tarfile.open(backup_path,"w:gz") as tar:
      tar.add(source_dir, arcname=os.path.basename(source_dir))
      print(f"Backup do arquivo: {backup_path}")

def main():
   if not os.path.exists(BACKUP_DIRECTORY):
      os.makedirs(BACKUP_DIRECTORY)
      print(f"Diretorio do backup criado: {BACKUP_DIRECTORY}")
   
   create_backup(SOURCE_DIRECTORY, BACKUP_DIRECTORY, BACKUP_NAME)

if __name__ == "__main__":
   main()
