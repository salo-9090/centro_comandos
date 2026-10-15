import os
import sys
import platform
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def ejecutar_comando(comando):
    """Ejecuta un comando en la terminal de forma limpia."""
    os.system('clear')
    console.print(Panel(f"[bold cyan]Ejecutando:[/bold cyan] [yellow]{comando}[/yellow]"))
    subprocess.run(comando, shell=True)
    input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

# ==========================================
# 1. MÓDULO SISTEMA
# ==========================================
def modulo_sistema():
    while True:
        os.system('clear')
        table = Table(title="📊 MÓDULO DE SISTEMA", header_style="bold green")
        table.add_column("Opción", justify="center", style="cyan")
        table.add_column("Herramienta / Acción", style="white")

        table.add_row("1", "Información detallada del SO y Python")
        table.add_row("2", "Listar archivos de la carpeta actual")
        table.add_row("3", "Ver espacio disponible en disco")
        table.add_row("0", "Volver al Menú Principal")

        console.print(table)
        op = Prompt.ask("\n[bold green]Selecciona una opción[/bold green]", choices=["1", "2", "3", "0"], default="0")

        if op == "1":
            os.system('clear')
            info_sys = (
                f"[bold cyan]Sistema Operativo:[/bold cyan] {platform.system()} {platform.release()}\n"
                f"[bold cyan]Arquitectura:[/bold cyan] {platform.machine()}\n"
                f"[bold cyan]Usuario actual:[/bold cyan] salomon\n"
                f"[bold cyan]Ruta actual:[/bold cyan] {os.getcwd()}\n"
                f"[bold cyan]Versión de Python:[/bold cyan] {platform.python_version()}"
            )
            console.print(Panel(info_sys, title="[bold green]Estado del Sistema[/bold green]"))
            input("\nPresiona Enter para volver...")
        elif op == "2":
            os.system('clear')
            archivos = "\n".join(os.listdir('.'))
            console.print(Panel(archivos if archivos else "Carpeta vacía", title="[bold cyan]Archivos Actuales[/bold cyan]"))
            input("\nPresiona Enter para volver...")
        elif op == "3":
            ejecutar_comando("df -h")
        elif op == "0":
            break

# ==========================================
# 2. MÓDULO CIBERSEGURIDAD
# ==========================================
def modulo_ciberseguridad():
    while True:
        os.system('clear')
        table = Table(title="🛡️ MÓDULO DE CIBERSEGURIDAD Y REDES", header_style="bold red")
        table.add_column("Opción", justify="center", style="cyan")
        table.add_column("Herramienta / Acción", style="white")

        table.add_row("1", "Ver IP local e interfaces de red")
        table.add_row("2", "Prueba de conectividad (Ping a Google)")
        table.add_row("3", "Escanear puertos locales (Nmap / Netcat)")
        table.add_row("4", "Ejecutar comando Bash personalizado")
        table.add_row("0", "Volver al Menú Principal")

        console.print(table)
        op = Prompt.ask("\n[bold red]Selecciona una opción[/bold red]", choices=["1", "2", "3", "4", "0"], default="0")

        if op == "1":
            ejecutar_comando("ip a || ifconfig")
        elif op == "2":
            ejecutar_comando("ping -c 4 8.8.8.8")
        elif op == "3":
            ejecutar_comando("nmap localhost || nc -zv localhost 1-100")
        elif op == "4":
            cmd = Prompt.ask("[cyan]Escribe el comando bash a ejecutar[/cyan]")
            if cmd:
                ejecutar_comando(cmd)
        elif op == "0":
            break

# ==========================================
# 3. MÓDULO MULTIMEDIA
# ==========================================
def modulo_multimedia():
    while True:
        os.system('clear')
        table = Table(title="🎬 MÓDULO MULTIMEDIA", header_style="bold magenta")
        table.add_column("Opción", justify="center", style="cyan")
        table.add_column("Herramienta / Acción", style="white")

        table.add_row("1", "Descargar Video / Audio con yt-dlp")
        table.add_row("2", "Convertir Formato de Video/Audio con FFmpeg")
        table.add_row("3", "Verificar instalación de herramientas multimedia")
        table.add_row("0", "Volver al Menú Principal")

        console.print(table)
        op = Prompt.ask("\n[bold magenta]Selecciona una opción[/bold magenta]", choices=["1", "2", "3", "0"], default="0")

        if op == "1":
            url = Prompt.ask("[cyan]Ingresa la URL del video[/cyan]")
            if url:
                ejecutar_comando(f"yt-dlp {url}")
        elif op == "2":
            archivo_orig = Prompt.ask("[cyan]Nombre del archivo original[/cyan]")
            archivo_dest = Prompt.ask("[cyan]Nombre del archivo convertido (ej: salida.mp3)[/cyan]")
            if archivo_orig and archivo_dest:
                ejecutar_comando(f"ffmpeg -i {archivo_orig} {archivo_dest}")
        elif op == "3":
            ejecutar_comando("which yt-dlp ffmpeg")
        elif op == "0":
            break

# ==========================================
# 4. GESTOR DE LIBRERÍAS (PIP)
# ==========================================
def modulo_librerias():
    while True:
        os.system('clear')
        table = Table(title="📦 GESTOR DE LIBRERÍAS PYTHON (PIP)", header_style="bold yellow")
        table.add_column("Opción", justify="center", style="cyan")
        table.add_column("Herramienta / Acción", style="white")

        table.add_row("1", "Instalar una librería nueva")
        table.add_row("2", "Listar librerías instaladas")
        table.add_row("3", "Actualizar PIP")
        table.add_row("0", "Volver al Menú Principal")

        console.print(table)
        op = Prompt.ask("\n[bold yellow]Selecciona una opción[/bold yellow]", choices=["1", "2", "3", "0"], default="0")

        if op == "1":
            paquete = Prompt.ask("[cyan]Ingresa el nombre del paquete/librería[/cyan]")
            if paquete:
                ejecutar_comando(f"pip install {paquete} --break-system-packages")
        elif op == "2":
            ejecutar_comando("pip list")
        elif op == "3":
            ejecutar_comando("python3 -m pip install --upgrade pip --break-system-packages")
        elif op == "0":
            break

# ==========================================
# 5. MÓDULO SINCRONIZACIÓN GIT (PC / CELU)
# ==========================================
def modulo_git():
    while True:
        os.system('clear')
        table = Table(title="☁️ MÓDULO DE SINCRONIZACIÓN GIT", header_style="bold blue")
        table.add_column("Opción", justify="center", style="cyan")
        table.add_column("Acción Git", style="white")

        table.add_row("1", "Ver estado del repositorio (git status)")
        table.add_row("2", "Descargar cambios recientes (git pull)")
        table.add_row("3", "Guardar y subir cambios a la nube (git push)")
        table.add_row("0", "Volver al Menú Principal")

        console.print(table)
        op = Prompt.ask("\n[bold blue]Selecciona una opción[/bold blue]", choices=["1", "2", "3", "0"], default="0")

        if op == "1":
            ejecutar_comando("git status")
        elif op == "2":
            ejecutar_comando("git pull")
        elif op == "3":
            mensaje = Prompt.ask("[cyan]Mensaje para los cambios (commit)[/cyan]", default="Actualización de comandos")
            ejecutar_comando(f"git add . && git commit -m '{mensaje}' && git push")
        elif op == "0":
            break

# ==========================================
# MENÚ PRINCIPAL
# ==========================================
def mostrar_menu():
    while True:
        os.system('clear')
        
        console.print(Panel.fit(
            "[bold cyan]✨ CENTRO DE COMANDOS MAESTRO ✨[/bold cyan]\n"
            "[bold white]Entorno Unificado (PC / Termux)[/bold white]",
            border_style="magenta"
        ))
        
        table = Table(show_header=True, header_style="bold yellow")
        table.add_column("Opción", style="cyan", justify="center")
        table.add_column("Módulo Principal", style="green")
        
        table.add_row("1", "📊 Módulo de Sistema")
        table.add_row("2", "🛡️ Ciberseguridad & Redes")
        table.add_row("3", "🎬 Módulo Multimedia")
        table.add_row("4", "📦 Gestor de Librerías PIP")
        table.add_row("5", "☁️ Sincronización Git (PC / Celu)")
        table.add_row("0", "❌ Salir")
        
        console.print(table)
        
        opcion = Prompt.ask("\n[bold yellow]Selecciona una opción[/bold yellow]", choices=["1", "2", "3", "4", "5", "0"], default="0")
        
        if opcion == "1":
            modulo_sistema()
        elif opcion == "2":
            modulo_ciberseguridad()
        elif opcion == "3":
            modulo_multimedia()
        elif opcion == "4":
            modulo_librerias()
        elif opcion == "5":
            modulo_git()
        elif opcion == "0":
            console.print("\n[bold red]¡Hasta luego, Martín![/bold red]\n")
            sys.exit()

if __name__ == "__main__":
    mostrar_menu()
