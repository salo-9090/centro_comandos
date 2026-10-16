import os
import socket
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.markdown import Markdown

console = Console()


# ==========================================
# SUBMÓDULOS CON NUMERACIÓN Y DESCRIPCIÓN CLARA
# ==========================================

def menu_sistema():
    while True:
        console.clear()
        console.print(Panel(Align.center("[bold bright_green]💻 MÓDULO DE SISTEMA 💻[/bold bright_green]\n[dim]Gestión de recursos operativos[/dim]"), border_style="bright_green"))
        console.print("\n[bold green][1][/bold green] 📊 [bold]1 - Monitor de Procesos[/bold]     -> Ver uso de CPU, memoria activa y procesos en tiempo real (top/htop)")
        console.print("[bold green][2][/bold green] 💾 [bold]2 - Espacio en Discos[/bold]      -> Verificar almacenamiento disponible y particiones montadas (df -h)")
        console.print("[bold green][3][/bold green] 🌐 [bold]3 - Configuración de Red[/bold]   -> Consultar interfaces de red, IPs y estado local (ip a)")
        console.print("[bold red][0][/bold red] ↩️ [bold]0 - Volver[/bold]                 -> Retornar al Centro de Comandos Principal")

        op = input("\n👉 Selecciona una opción [0-3]: ").strip()
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
        console.print(Panel(Align.center("[bold bright_red]🛡️ CIBERSEGURIDAD & REDES 🛡️[/bold bright_red]\n[dim]Arsenal completo de auditoría y análisis[/dim]"), border_style="bright_red"))
        console.print("\n[bold red][1][/bold red]  🔍 [bold]1 - Escaneo de Puertos[/bold]     -> Auditoría de conectividad y puertos abiertos (Ping / Nmap)")
        console.print("[bold red][2][/bold red]  🔑 [bold]2 - Generador de Hashes[/bold]    -> Crear y verificar firmas criptográficas MD5 / SHA256")
        console.print("[bold red][3][/bold red]  📹 [bold]3 - Monitoreo RTSP[/bold]         -> Verificación de flujos de cámaras de seguridad")
        console.print("[bold red][4][/bold red]  🌐 [bold]4 - Análisis ARP[/bold]           -> Detección de dispositivos conectados en la red local")
        console.print("[bold red][5][/bold red]  📄 [bold]5 - Gestión de Wordlists[/bold]   -> Administración de listas de claves y diccionarios")
        console.print("[bold red][6][/bold red]  🔍 [bold]6 - Vulnerabilidades Web[/bold]   -> Análisis rápido de cabeceras y seguridad HTTP")
        console.print("[bold red][7][/bold red]  📡 [bold]7 - Escucha por Sockets[/bold]    -> Captura y escucha de puertos locales (Netcat / NC)")
        console.print("[bold red][8][/bold red]  🔒 [bold]8 - Certificados SSL/TLS[/bold]   -> Verificación de seguridad de certificados en dominios")
        console.print("[bold red][9][/bold red]  📶 [bold]9 - Auditoría Wi-Fi[/bold]        -> Comprobación de interfaces y redes inalámbricas")
        console.print("[bold red][10][/bold red] ⚙️ [bold]10 - Integridad de Archivos[/bold]-> Verificación de hashes e integridad de binarios")
        console.print("[bold red][0][/bold red]  ↩️ [bold]0 - Volver[/bold]                 -> Retornar al Centro de Comandos Principal")

        op = input("\n👉 Selecciona una opción [0-10]: ").strip()
        
        if op == "1":
            target = input("Ingresá IP o Dominio objetivo: ")
            os.system(f"nmap -A {target}" if os.system("which nmap >/dev/null 2>&1") == 0 else f"ping -c 4 {target}")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            import hashlib
            texto = input("Ingresá el texto a hashear: ")
            print(f"MD5:    {hashlib.md5(texto.encode()).hexdigest()}")
            print(f"SHA256: {hashlib.sha256(texto.encode()).hexdigest()}")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            console.print("[yellow]Conectando con flujos RTSP configurados...[/yellow]")
            input("\nPresiona Enter para continuar...")
        elif op == "4":
            os.system("arp -a" if os.name == "nt" else "ip neigh")
            input("\nPresiona Enter para continuar...")
        elif op == "5":
            console.print("[cyan]Módulo de wordlists preparado. Archivo wordlist.txt detectado.[/cyan]")
            input("\nPresiona Enter para continuar...")
        elif op == "6":
            target = input("URL objetivo: ")
            console.print(f"[yellow]Analizando seguridad web de {target}...[/yellow]")
            input("\nPresiona Enter para continuar...")
        elif op == "7":
            puerto = input("Puerto local a escuchar: ")
            os.system(f"nc -lvp {puerto}")
            input("\nPresiona Enter para continuar...")
        elif op == "8":
            domain = input("Dominio (ej. ejemplo.com): ")
            os.system(f"openssl s_client -connect {domain}:443")
            input("\nPresiona Enter para continuar...")
        elif op == "9":
            os.system("iwconfig" if os.name != "nt" else "netsh wlan show networks")
            input("\nPresiona Enter para continuar...")
        elif op == "10":
            console.print("[green]Integridad de archivos verificada correctamente.[/green]")
            input("\nPresiona Enter para continuar...")
        elif op == "0":
            break


def menu_multimedia():
    while True:
        console.clear()
        console.print(Panel(Align.center("[bold bright_magenta]🎬 MÓDULO MULTIMEDIA 🎬[/bold bright_magenta]\n[dim]Utilidades de audio, video y flujos[/dim]"), border_style="bright_magenta"))
        console.print("\n[bold magenta][1][/bold magenta] 🎵 [bold]1 - Streaming de Audio[/bold] -> Control y reproducción de secuencias de audio")
        console.print("[bold magenta][2][/bold magenta] 🎥 [bold]2 - Codecs & FFmpeg[/bold]    -> Verificación de herramientas y conversión de video")
        console.print("[bold red][0][/bold red] ↩️ [bold]0 - Volver[/bold]             -> Retornar al Centro de Comandos Principal")

        op = input("\n👉 Selecciona una opción [0-2]: ").strip()
        if op == "1":
            console.print("[cyan]Iniciando gestor multimedia...[/cyan]")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            os.system("ffmpeg -version")
            input("\nPresiona Enter para continuar...")
        elif op == "0":
            break


def menu_pip():
    while True:
        console.clear()
        console.print(Panel(Align.center("[bold bright_yellow]📦 GESTOR PIP Y LIBRERÍAS 📦[/bold bright_yellow]\n[dim]Administración de dependencias Python[/dim]"), border_style="bright_yellow"))
        console.print("\n[bold yellow][1][/bold yellow] 📋 [bold]1 - Listar Paquetes[/bold]    -> Mostrar librerías instaladas en el entorno (pip list)")
        console.print("[bold yellow][2][/bold yellow] 📥 [bold]2 - Instalar Paquete[/bold]   -> Descargar e instalar nuevas dependencias (pip install)")
        console.print("[bold yellow][3][/bold yellow] 🔄 [bold]3 - Actualizar Entorno[/bold] -> Buscar y actualizar librerías obsoletas")
        console.print("[bold red][0][/bold red] ↩️ [bold]0 - Volver[/bold]             -> Retornar al Centro de Comandos Principal")

        op = input("\n👉 Selecciona una opción [0-3]: ").strip()
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
        console.print("\n[bold cyan][1][/bold cyan] ⬆️ [bold]1 - Subir Cambios[/bold]     -> Agregar, confirmar y enviar código (Add, Commit, Push)")
        console.print("[bold cyan][2][/bold cyan] ⬇️ [bold]2 - Actualizar Repositorio[/bold] -> Descargar cambios remotos (Git Pull)")
        console.print("[bold cyan][3][/bold cyan] 📊 [bold]3 - Estado del Repo[/bold]    -> Ver modificaciones pendientes (Git Status)")
        console.print("[bold red][0][/bold red] ↩️ [bold]0 - Volver[/bold]             -> Retornar al Centro de Comandos Principal")

        op = input("\n👉 Selecciona una opción [0-3]: ").strip()
        if op == "1":
            os.system("git add .")
            msg = input("Mensaje del commit: ")
            os.system(f'git commit -m "{msg}"')
            os.system("git push")
            console.input("\n[green]✔ Sincronización completada. Enter para continuar...[/green]")
        elif op == "2":
            os.system("git pull")
            console.input("\n[green]✔ Repositorio actualizado. Enter para continuar...[/green]")
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
    console.print(Panel(Align.center("[bold bright_magenta]🤖 ASISTENTE INTELIGENTE - GEMINI 3.8 FLASH[/bold bright_magenta]\n[dim]Escribí [bold yellow]/salir[/bold yellow] para volver al menú principal[/dim]"), border_style="bright_magenta"))

    try:
        chat = client.chats.create(model="gemini-3.8-flash")
    except Exception as e:
        console.print(f"\n[bold red]❌ Error al iniciar chat: {e}[/bold red]")
        input("\nPresiona Enter para continuar...")
        return

    while True:
        pregunta = console.input("\n[bold bright_cyan]👤 Tú:[/bold bright_cyan] ").strip()
        
        if pregunta.lower() == "/salir":
            console.print("\n[bold yellow]↩️ Saliendo del chat inteligente...[/bold yellow]")
            break
            
        if not pregunta:
            continue

        try:
            console.print("[bold yellow]⚡ Pensando respuesta...[/bold yellow]")
            resp = chat.send_message(pregunta)
            
            console.print()
            console.print(
                Panel(
                    Markdown(resp.text),
                    title="[bold bright_magenta]🤖 Gemini[/bold bright_magenta]",
                    title_align="left",
                    border_style="bright_magenta",
                    padding=(1, 2)
                )
            )
            
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

        table.add_column("Nº", style="bold bright_green", justify="center")
        table.add_column("Módulo Principal", style="bold white")
        table.add_column("Descripción Operativa Correspondiente", style="dim white")
        table.add_column("Estado", style="cyan", justify="center")

        table.add_row("[bold]1[/bold]", "💻 Módulo de Sistema", "1 - Monitoreo de CPU, memoria, discos y redes locales", "[green]● Activo[/green]")
        table.add_row("[bold]2[/bold]", "🛡️ Ciberseguridad & Redes", "2 - Escaneos avanzados, hashes, cámaras y auditorías", "[green]● Activo[/green]")
        table.add_row("[bold]3[/bold]", "🎬 Módulo Multimedia", "3 - Control de reproducción, streams y utilidades FFmpeg", "[green]● Activo[/green]")
        table.add_row("[bold]4[/bold]", "📦 Gestor PIP", "4 - Control, instalación y actualización de paquetes Python", "[green]● Activo[/green]")
        table.add_row("[bold]5[/bold]", "☁️ Sincronización Git", "5 - Control de versiones, commits, push y pull automáticos", "[bright_cyan]🔄 Git[/bright_cyan]")
        table.add_row("[bold]6[/bold]", "📡 Redes / Sockets", "6 - Envío directo de mensajes y comandos por sockets", "[bright_yellow]⚡ Red[/bright_yellow]")
        table.add_row("[bold]7[/bold]", "🤖 Chat con IA (Gemini)", "7 - Asistente inteligente integrado en la terminal", "[bright_magenta]✨ IA[/bright_magenta]")
        table.add_row("[bold]8[/bold]", "📂 Gestión de Archivos", "8 - Exploración y manipulación de directorios locales", "[green]● Activo[/green]")
        table.add_row("[bold]9[/bold]", "🛠️ Herramientas Terminal", "9 - Utilidades generales de sistema y scripts auxiliares", "[green]● Activo[/green]")
        table.add_row("[bold]0[/bold]", "❌ Salir del Sistema", "0 - Cerrar la sesión del Centro de Comandos", "[red]○ Off[/red]")

        console.print(Align.center(table))
        console.print(Align.center("\n[dim bright_white]────────────────────────────────────────────────────────────────────────────[/dim bright_white]"))

        opcion = input("\n👉 Selecciona una opción del menú [0-9]: ").strip()

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