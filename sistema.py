import os
from rich import print
from rich.panel import Panel

def ejecutar():
    while True:
        os.system("clear")
        print(Panel("[bold yellow]⚙️ MÓDULO SISTEMA Y SERVIDORES[/bold yellow]", border_style="yellow"))
        print("1. Ver espacio en disco y hardware")
        print("2. Levantar servidor web local (Puerto 8080)")
        print("3. Volver al menú principal")
        print("-" * 35)
        op = input("Elige una opción (1-3): ").strip()
        
        if op == "1":
            os.system("uname -a && df -h")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            print("\n[+] Iniciando servidor web. Presiona Ctrl+C para salir.")
            os.system("python -m http.server 8080")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            break
