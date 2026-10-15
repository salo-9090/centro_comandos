import os
import datetime

# Intentamos importar rich para darle diseño avanzado, si no está, usamos prints normales
try:
    from rich import print
    from rich.panel import Panel
    from rich.table import Table
    USAR_RICH = True
except ImportError:
    USAR_RICH = False

def limpiar_pantalla():
    os.system("clear")

def submenu_ciberseguridad():
    while True:
        limpiar_pantalla()
        if USAR_RICH:
            print(Panel("[bold cyan]🛡️ SUBMENÚ: CIBERSEGURIDAD Y RED[/bold cyan]", border_style="cyan"))
        else:
            print("=================================")
            print("   🛡️ SUBMENÚ: CIBERSEGURIDAD Y RED")
            print("=================================")
            
        print("1. Escaneo rápido de red local (Nmap)")
        print("2. Ver interfaces y dirección IP actual")
        print("3. Volver al menú principal")
        print("-" * 33)
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
        else:
            input("\n[❌] Opción inválida. Presiona Enter...")

def submenu_multimedia():
    while True:
        limpiar_pantalla()
        if USAR_RICH:
            print(Panel("[bold magenta]📥 SUBMENÚ: MULTIMEDIA Y DESCARGAS[/bold magenta]", border_style="magenta"))
        else:
            print("=================================")
            print("   📥 SUBMENÚ: MULTIMEDIA Y DESCARGAS")
            print("=================================")
            
        print("1. Descargar video de YouTube (yt-dlp)")
        print("2. Descargar solo audio MP3 (yt-dlp)")
        print("3. Volver al menú principal")
        print("-" * 33)
        op = input("Elige una opción (1-3): ").strip()
        
        if op == "1":
            url = input("Ingresa el enlace del video: ").strip()
            if url:
                os.system(f"yt-dlp {url}")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            url = input("Ingresa el enlace para extraer audio: ").strip()
            if url:
                os.system(f"yt-dlp -x --audio-format mp3 {url}")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            break
        else:
            input("\n[❌] Opción inválida. Presiona Enter...")

def submenu_sistema():
    while True:
        limpiar_pantalla()
        if USAR_RICH:
            print(Panel("[bold yellow]⚙️ SUBMENÚ: SISTEMA Y SERVIDORES[/bold yellow]", border_style="yellow"))
        else:
            print("=================================")
            print("   ⚙️ SUBMENÚ: SISTEMA Y SERVIDORES")
            print("
