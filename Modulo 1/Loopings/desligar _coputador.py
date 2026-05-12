
import ctypes
import sys
import platform

def lock_windows():
    """
    Bloqueia a sessão do usuário no Windows (equivalente a Win + L).
    """
    try:
        if platform.system() != "Windows":
            print("Este script só funciona no Windows.")
            return
        
        # Chama a função LockWorkStation da API do Windows
        ctypes.windll.user32.LockWorkStation()
        print("Computador bloqueado com sucesso.")
    except Exception as e:
        print(f"Erro ao tentar bloquear o computador: {e}")

if __name__ == "__main__":
    lock_windows()


import os
import platform

def lock_linux():
    """
    Bloqueia a sessão no Linux usando comandos do sistema.
    """
    try:
        if platform.system() != "Linux":
            print("Este script só funciona no Linux.")
            return
        
        # Tenta usar o comando padrão do GNOME
        os.system("gnome-screensaver-command -l || loginctl lock-session")
        print("Computador bloqueado com sucesso.")
    except Exception as e:
        print(f"Erro ao tentar bloquear o computador: {e}")

if __name__ == "__main__":
    lock_linux()
