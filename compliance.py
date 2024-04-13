import subprocess
import os

# Função para verificar permissões de arquivos importantes
def check_file_permissions(files):
    """Verifica se as permissões de arquivos críticos estão corretas."""
    for file in files:
        try:
            stat = os.stat(file)
            permissions = oct(stat.st_mode)[-3:]
            if permissions not in ['600', '644']:
                print(f"Permissões incorretas para {file}: {permissions}")
            else:
                print(f"Permissões corretas para {file}: {permissions}")
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {file}")

# Função para verificar políticas de senha
def check_password_policy():
    """Verifica as políticas de senha do sistema."""
    result = subprocess.run(['chage', '--list', 'root'], capture_output=True, text=True)
    if "password must be changed" in result.stdout.lower():
        print("Política de senha está configurada corretamente.")
    else:
        print("Política de senha NÃO está configurada corretamente.")

# Função para verificar configurações de firewall
def check_firewall_status():
    """Verifica se o firewall está ativo e configurado corretamente."""
    try:
        result = subprocess.run(['systemctl', 'status', 'ufw'], capture_output=True, text=True)
        if 'active (running)' in result.stdout:
            print("Firewall está ativo e rodando.")
        else:
            print("Firewall NÃO está ativo.")
    except subprocess.CalledProcessError:
        print("Erro ao verificar o status do firewall.")

def main():
    # Lista de arquivos críticos para verificar as permissões
    critical_files = ['/etc/shadow', '/etc/gshadow', '/etc/passwd']
    
    # Verifica permissões de arquivos críticos
    check_file_permissions(critical_files)

    # Verifica a política de senha
    check_password_policy()

    # Verifica o status do firewall
    check_firewall_status()

if __name__ == "__main__":
    main()

