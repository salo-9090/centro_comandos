import os
import datetime
from rich import print
from rich.panel import Panel
import ciber, multimedia, sistema, librerias

def menu_principal():
    while True:
        os.system("clear")
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        print(Panel(f"[bold blue]🚀 SUPER CENTRO DE COMANDOS[/bold blue]\n[italic dim]🕒 {fecha}[/italic dim]", border_style="blue"))
        print("1. 🛡️ Ciberseguridad y Redes")
        print("2. 📥 Multimedia (yt-dlp)")
        print("3. ⚙️ Sistema y Servidores")
        print("4. 📦 Gestor de Librerías (pip)")
        print("5. 🚪 Volver al saludo / Salir al inicio")
        print("-" * 33)
        op = input("Selecciona una opción (1-5): ").strip()
        
        if op == "1":
            ciber.ejecutar()
        elif op == "2":
            multimedia.ejecutar()
        elif op == "3":
            sistema.ejecutar()
        elif op == "4":
            librerias.ejecutar()
        elif op == "5":
            print("[bold yellow]Volviendo al inicio...[/bold yellow]")
            break

if __name__ == "__main__":
    menu_principal()
