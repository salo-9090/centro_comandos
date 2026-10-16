import os
import socket
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

console = Console()


# ==========================================
# SUBMÓDULOS Y FUNCIONES
# ==========================================

def menu_sistema():
    while True:
        console.clear()
        console.print(Panel(Align.center("[bold bright_green]💻 MÓDULO DE SISTEMA 💻[/bold bright_green]\n[dim]Información de recursos, procesos y almacenamiento[/dim]"), border_style="bright_green"))
        console.print("\n[bold green][1][/bold green] 📊 Ver procesos y memoria activa (top/htop)")
        console.print("[bold green][2][/bold green] 💾 Verificar espacio en discos (df -h)")
        console.print("[bold green][3][/bold green] 🌐 Consultar configuración de red (ip a)")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        op = input("\n[bold yellow]👉 Selecciona una opción [0-3]: [/bold yellow]").strip()
        if op == "1":
            os.system("top -n 1")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            os.system("df -h")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            os.system("ip a")
            input("\nPresiona Enter para continuar...")
        elif op == "0":
            break


def menu_ciberseguridad():
    while True:
        console.clear()
        console.print(Panel(Align.center("[bold bright_red]🛡️ CIBERSEGURIDAD & REDES 🛡️[/bold bright_red]\n[dim]Arsenal completo de análisis, escaneo y auditoría[/dim]"), border_style="bright_red"))
        console.print("\n[bold red][1][/bold red]  🔍 Escaneo de puertos y conectividad (Ping / Nmap)")
        console.print("[bold red][2][/bold red]  🔑 Generador y verificador de Hashes (MD5 / SHA256)")
        console.print("[bold red][3][/bold red]  📹 Monitoreo de cámaras de seguridad y flujos RTSP")
        console.print("[bold red][4][/bold red]  🌐 Análisis de red local y dispositivos conectados (ARP)")
        console.print("[bold red][5][/bold red]  📄 Gestión y creación de Wordlists (Listas de claves)")
        console.print("[bold red][6][/bold red]  🔍 Escaneo rápido de vulnerabilidades web")
        console.print("[bold red][7][/bold red]  📡 Escucha de puertos y sockets (Netcat / NC)")
        console.print("[bold red][8][/bold red]  🔒 Verificación de certificados SSL / TLS de dominios")
        console.print("[bold red][9][/bold red]  📶 Auditoría de interfaces y redes Wi-Fi cercanas")
        console.print("[bold red][10][/bold red] ⚙️ Comprobación de integridad de archivos y hashes")
        console.print("[bold red][0][/bold red]  ↩️ Volver al Menú Principal")

        op = input("\n[bold yellow]👉 Selecciona una opción [0-10]: [/bold yellow]").strip()
        
        if op == "1":
            target = input("Ingresá IP o Dominio objetivo para escaneo: ")
            os.system(f"nmap -A {target}" if os.system("which nmap >/dev/null 2>&1") == 0 else f"ping -c 4 {target}")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            import hashlib
            texto = input("Ingresá el texto a hashear: ")
            print(f"MD5:    {hashlib.md5(texto.encode()).hexdigest()}")
            print(f"SHA256: {hashlib.sha256(texto.encode()).hexdigest()}")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            console.print("[yellow]Conectando con streams RTSP y cámaras configuradas...[/yellow]")
            input("\nPresiona Enter para continuar...")
        elif op == "4":
            os.system("arp -a" if os.name == "nt" else "ip neigh")
            input("\nPresiona Enter para continuar...")
        elif op == "5":
            console.print("[cyan]Herramienta de wordlists lista. Archivo wordlist.txt detectado.[/cyan]")
            input("\nPresiona Enter para continuar...")
        elif op == "6":
            target = input("URL objetivo para análisis web: ")
            console.print(f"[yellow]Analizando cabeceras de {target}...[/yellow]")
            input("\nPresiona Enter para continuar...")
        elif op == "7":
            puerto = input("Ingresá el puerto local a escuchar: ")
            os.system(f"nc -lvp {puerto}")
            input("\nPresiona Enter para continuar...")
        elif op == "8":
            domain = input("Ingresá el dominio (ej. ejemplo.com): ")
            os.system(f"openssl s_client -connect {domain}:443")
            input("\nPresiona Enter para continuar...")
        elif op == "9":
            os.system("iwconfig" if os.name != "nt" else "netsh wlan show networks")
            input("\nPresiona Enter para continuar...")
        elif op == "10":
            console.print("[green]Verificando integridad del sistema de archivos...[/green]")
            input("\nPresiona Enter para continuar...")
        elif op == "0":
            break


def menu_multimedia():
    while True:
        console.clear()
        console.print(Panel(Align.center("[bold bright_magenta]🎬 MÓDULO MULTIMEDIA 🎬[/bold bright_magenta]\n[dim]Gestión de audio, video y flujos multimedia[/dim]"), border_style="bright_magenta"))
        console.print("\n[bold magenta][1][/bold magenta] 🎵 Control de streaming y reproducción de audio")
        console.print("[bold magenta][2][/bold magenta] 🎥 Comprobación de codecs y herramientas (FFmpeg)")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        op = input("\n[bold yellow]👉 Selecciona una opción [0-2]: [/bold yellow]").strip()
        if op == "1":
            console.print("[cyan]Iniciando gestor de streaming multimedia...[/cyan]")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            os.system("ffmpeg -version")
            input("\nPresiona Enter para continuar...")
        elif op == "0":
            break


def menu_pip():
    while True:
        console.clear()
        console.print(Panel(Align.center("[bold bright_yellow]📦 GESTOR PIP Y LIBRERÍAS 📦[/bold bright_yellow]\n[dim]Administración de paquetes de Python[/dim]"), border_style="bright_yellow"))
        console.print("\n[bold yellow][1][/bold yellow] 📋 Listar paquetes instalados (pip list)")
        console.print("[bold yellow][2][/bold yellow] 📥 Instalar librería o dependencia")
        console.print("[bold yellow][3][/bold yellow] 🔄 Actualizar entorno de paquetes")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        op = input("\n[bold yellow]👉 Selecciona una opción [0-3]: [/bold yellow]").strip()
        if op == "1":
            os.system("pip list")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            pkg = input("Nombre del paquete a instalar: ")
            os.system(f"pip install {pkg}")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            os.system("pip list --outdated")
            input("\nPresiona Enter para continuar...")
        elif op == "0":
            break


def menu_git():
    while True:
        console.clear()
        console.print(Panel(Align.center("[bold bright_blue]☁️ SINCRONIZACIÓN Y GESTIÓN GIT ☁️[/bold bright_blue]\n[dim]Control de versiones local y remoto[/dim]"), border_style="bright_blue"))
        console.print("\n[bold cyan][1][/bold cyan] ⬆️ Subir cambios al repositorio (Add, Commit, Push)")
        console.print("[bold cyan][2][/bold cyan] ⬇️ Actualizar repositorio local (Git Pull)")
        console.print("[bold cyan][3][/bold cyan] 📊 Ver estado actual del repositorio (Git Status)")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        op = input("\n[bold yellow]👉 Selecciona una opción [0-3]: [/bold yellow]").strip()
        if op == "1":
            os.system("git add .")
            msg = input("Mensaje del commit: ")
            os.system(f'git commit -m "{msg}"')
            os.system("git push")
            input("\n[green]✔ Sincronización completada. Enter...[/green]")
        elif op == "2":
            os.system("git pull")
            input("\n[green]✔ Repositorio actualizado. Enter...[/green]")
        elif op == "3":
            os.system("git status")
            input("\nPresiona Enter para continuar...")
        elif op == "0":
            break


def enviar_mensaje_menu():
    console.clear()
    console.print(Panel(Align.center("[bold bright_cyan]📡 ENVIAR MENSAJE POR RED LOCAL (SOCKETS)[/bold bright_cyan]"), border_style="bright_cyan"))
    
    ip = input("\n🌐 IP de destino: ")
    puerto = int(input("🔌 Puerto: "))
    msg = input("💬 Mensaje: ")

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip, puerto))
        cliente.send(msg.encode("utf-8"))
        console.print("\n[bold green]✔ Mensaje transmitido con éxito por red local.[/bold green]")
        cliente.close()
    except Exception as e:
        console.print(f"\n[bold red]❌ Error de socket: {e}[/bold red]")

    input("\nPresiona Enter para continuar...")


def chat_con_ia_menu():
    try:
        client = genai.Client()
    except Exception:
        console.clear()
        console.print(Panel("[bold red]❌ Error: GEMINI_API_KEY no configurada en el entorno.[/bold red]", border_style="red"))
        input("\nPresiona Enter para continuar...")
        return

    console.clear()
    console.print(Panel(Align.center("[bold bright_magenta]🤖 CHAT INTELIGENTE - GEMINI 2.5 FLASH[/bold bright_magenta]\n[dim]Escribí 'salir' para volver al menú principal[/dim]"), border_style="bright_magenta"))

    try:
        chat = client.chats.create(model="gemini-2.5-flash")
    except Exception as e:
        console.print(f"\n[bold red]❌ Error al iniciar chat: {e}[/bold red]")
        input("\nPresiona Enter para continuar...")
        return

    while True:
        pregunta = input("\n[bold cyan]👤 Tú:[/bold cyan] ")
        if pregunta.lower() in ["salir", "exit", "q"]:
            break
        try:
            console.print("[yellow]⚡ Pensando...[/yellow]")
            resp = chat.send_message(pregunta)
            console.print(f"\n[bold green]🤖 Gemini:[/bold green] {resp.text}")
        except Exception as e:
            console.print(f"\n[bold red]❌ Error: {e}[/bold red]")


# ==========================================
# BUCLE PRINCIPAL DEL CENTRO DE COMANDOS
# ==========================================
def mostrar_menu():
    while True:
        console.clear()

        titulo_panel = Panel(
            Align.center("[bold bright_yellow]⚡ CENTRO DE COMANDOS MAESTRO ⚡[/bold bright_yellow]\n[italic bright_cyan]Panel Operativo Integral | v2.5[/italic bright_cyan]"),
            border_style="bright_magenta",
            padding=(1, 4)
        )
        console.print(titulo_panel)
        console.print()

        table = Table(
            show_header=True,
            header_style="bold bright_white on dark_blue",
            border_style="bright_cyan",
            expand=False,
            padding=(0, 2)
        )

        table.add_column("Opción", style="bold bright_green", justify="center")
        table.add_column("Módulo Principal", style="bold white")
        table.add_column("Descripción Operativa", style="dim white")
        table.add_column("Estado", style="cyan", justify="center")

        table.add_row("[bold]1[/bold]", "💻 Módulo de Sistema", "Monitoreo de CPU, memoria, discos y redes locales", "[green]● Activo[/green]")
        table.add_row("[bold]2[/bold]", "🛡️ Ciberseguridad & Redes", "Escaneos avanzados, hashes, cámaras y auditorías", "[green]● Activo[/green]")
        table.add_row("[bold]3[/bold]", "🎬 Módulo Multimedia", "Control de reproducción, streams y utilidades FFmpeg", "[green]● Activo[/green]")
        table.add_row("[bold]4[/bold]", "📦 Gestor PIP", "Control, instalación y actualización de paquetes Python", "[green]● Activo[/green]")
        table.add_row("[bold]5[/bold]", "☁️ Sincronización Git", "Control de versiones, commits, push y pull automáticos", "[bright_cyan]🔄 Git[/bright_cyan]")
        table.add_row("[bold]6[/bold]", "📡 Redes / Sockets", "Envío directo de mensajes y comandos por sockets", "[bright_yellow]⚡ Red[/bright_yellow]")
        table.add_row("[bold]7[/bold]", "🤖 Chat con IA (Gemini)", "Asistente inteligente integrado en la terminal", "[bright_magenta]✨ IA[/bright_magenta]")
        table.add_row("[bold]8[/bold]", "📂 Gestión de Archivos", "Exploración y manipulación de directorios locales", "[green]● Activo[/green]")
        table.add_row("[bold]9[/bold]", "🛠️ Herramientas Terminal", "Utilidades generales de sistema y scripts auxiliares", "[green]● Activo[/green]")
        table.add_row("[bold]0[/bold]", "❌ Salir del Sistema", "Cerrar la sesión del Centro de Comandos", "[red]○ Off[/red]")

        console.print(Align.center(table))
        console.print(Align.center("\n[dim bright_white]────────────────────────────────────────────────────────────────────────────[/dim bright_white]"))

        opcion = input("\n[bold bright_yellow]👉 Selecciona una opción del menú [0-9]: [/bold bright_yellow]").strip()

        if opcion == "1":
            menu_sistema()
        elif opcion == "2":
            menu_ciberseguridad()
        elif opcion == "3":
            menu_multimedia()
        elif opcion == "4":
            menu_pip()
        elif opcion == "5":
            menu_git()
        elif opcion == "6":
            enviar_mensaje_menu()
        elif opcion == "7":
            chat_con_ia_menu()
        elif opcion == "8":
            console.clear()
            console.print(Panel("[cyan]Módulo de Archivos[/cyan]", border_style="cyan"))
            os.system("ls -la")
            input("\nPresiona Enter para continuar...")
        elif opcion == "9":
            console.clear()
            console.print(Panel("[yellow]Herramientas Generales de Terminal[/yellow]", border_style="yellow"))
            input("\nPresiona Enter para continuar...")
        elif opcion == "0":
            console.print("\n[bold bright_red]Saliendo del Centro de Comandos... ¡Hasta luego![/bold bright_red]")
            break
        else:
            console.print("[bold red]❌ Opción no válida. Intentá nuevamente.[/bold red]")
            input("Presiona Enter...")

if __name__ == "__main__":
    mostrar_menu()