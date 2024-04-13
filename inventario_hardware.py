import psutil
import csv
from datetime import datetime

#Função para coletar dados da cpu

def get_cpu_info():
   return {
      "Physical Cores": psutil.cpu_count(logical=False),
      "Total Cores": psutil.cpu_count(logical=True),
      "Max Frequency": f"{psutil.cpu_freq().max:.2f}Mhz"
   }


def get_memory_info():
   mem = psutil.virtual_memory()
   return {
      "Total": f"{mem.total / (1024 ** 3):.2f} GB", 
      "Available": f"{mem.available / (1024 ** 3):.2f} GB",
      "Used": f"{mem.used / (1024 ** 3):.2f} GB",
      "Percentage": f"{mem.percent}%"
   }

def get_disk_info():
   disks = psutil.disk_partitions()
   disk_info = {}
   for i, disk in enumerate(disks):
      usage = psutil.disk_usage(disk.mountpoint)
      disk_info[f"Disk {i+1} ({disk.device})"] = {
         "Total": f"{usage.total / (1024 ** 3):.2f} GB",
         "Used": f"{usage.used / (1024 ** 3):.2f} GB",
         "Free": f"{usage.free / (1024 ** 3):.2f} GB",
         "Percentage": f"{usage.percent}%"
      }
   return disk_info

def get_network_info():
  network_stats = psutil.net_if_addrs()
  network_info = {}
  for interface_name, interface_addresses in network_stats.items():
     for address in interface_addresses:
       if str(address.family) == 'AddresFamily.AF_INET':
          network_info[interface_name] = {
             "IP Address": address.address,
             "Netmask":  address.netmask,
             "Broadcast":  address.broadcast
          }    
       
  return network_info


def generate_csv_report(data,filename="hardware_inventory.csv"):
   with open(filename, mode='w', newline='') as file:
      writer = csv.writer(file)
      for key, value in data.items():
        writer.writerow([key])
        if isinstance(value,dict):
           for sub_key, sub_value in value.items():
              writer.writerow([sub_key, sub_value])
        writer.writerow([])
   print(f"Relatorio gerada com sucesso: {filename}")



def main():
   data = {
      "CPU Info": get_cpu_info(),
      "Memory Info": get_memory_info(),
      "Disk Info":  get_disk_info(),
      "Network Info":  get_network_info()
   }
   generate_csv_report(data)

if __name__ == "__main__":
  main()
