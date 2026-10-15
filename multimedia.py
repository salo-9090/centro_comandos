import os
from rich import print
from rich.panel import Panel

def ejecutar():
    while True:
        os.system("clear")
        print(Panel("[bold magenta]📥 MÓDULO MULTIMEDIA & YT-DLP[/bold magenta]", border_style="magenta"))
        print("1. Descargar video de YouTube")
        print("2. Descargar solo audio MP3")
        print("3. Volver al menú principal")
        print("-" * 35)
        op = input("Elige una opción (1-3): ").strip()
        
        if op == "1":
            url = input("Ingresa el enlace del video: ").strip()
            if url: os.system(f"yt-dlp {url}")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            url = input("Ingresa el enlace para extraer audio: ").strip()
            if url: os.system(f"yt-dlp -x --audio-format mp3 {url}")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            break
