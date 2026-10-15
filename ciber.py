import os
from rich import print
from rich.panel import Panel

def ejecutar():
    while True:
        os.system("clear")
        print(Panel("[bold cyan]🛡️ MÓDULO CIBERSEGURIDAD Y RED[/bold cyan]", border_style="cyan"))
        print("1. Escaneo rápido de red local (Nmap)")
        print("2. Ver interfaces de red y IP actual")
        print("3. Volver al menú principal")
        print("-" * 35)
        op = input("Elige una opción (1-3): ").strip()
        
        if op == "1":
            print("\n[+] Ejecutando escaneo con Nmap...")
            os.system("nmap -sn 192.168.1.0/24")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            print("\n[+] Consultando configuración de red...")
            os.system("ifconfig || ip a")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            break
