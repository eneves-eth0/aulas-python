import re
from collections import defaultdict

#caminho pro meu log
log_file_path = '/Users/eduardoneves/aulas-python/logs_example.log'

#padroes de erro que queremos encontrar
error_patterns = [ 'Error', 'Exception', 'Critical', 'Failed']

#Dicionario para armazenar a contagem de cada tipo de erro
error_counts = defaultdict(int)

def analyze_logs(filepath):
   try: 
     with open(filepath, 'r') as file:
        for line in file:
           for pattern in error_patterns: 
              if re.search(pattern, line):
                 error_counts[pattern] += 1
                 break
   except FileNotFoundError:
      print("Arquivo de log não encontrado")
   except Exception as e:
      print(f"Erro ao ler o arquivo: {e}")

def report():
   if error_counts:
      print("Relatorio de erros enontrados: ")
      for error, count in error_counts.items():
         print(f"{error}: {count} ocorrencia(s)")
   else:
      print("Nenhum erro encontrado com os padrões especificados")

def main():
   analyze_logs(log_file_path)
   report()

if __name__ == "__main__":
   main()













