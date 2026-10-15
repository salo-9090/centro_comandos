import os
import socket
import subprocess
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

console = Console()


# ==========================================
# 1. SUBMENÚ: Módulo de Sistema (Opción 1)
# ==========================================
def menu_sistema():
    while True:
        console.clear()
        panel = Panel(
            Align.center("[bold bright_green]💻 MÓDULO DE SISTEMA 💻[/bold bright_green]\n[dim]Información y herramientas del sistema operativo[/dim]"),
            border_style="bright_green",
            padding=(1, 2)
        )
        console.print(panel)
        console.print()
        
        console.print("[bold green][1][/bold green] 📊 Ver uso de memoria y procesos (htop / top)")
        console.print("[bold green][2][/bold green] 💾 Ver espacio en disco (df -h)")
        console.print("[bold green][3][/bold green] 🌐 Ver configuración de red (ip a / ifconfig)")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        sub_op = input("\n[bold bright_yellow]👉 Selecciona opción [0-3]:[/bold bright_yellow] ").strip()

        if sub_op == "1":
            console.print("\n[yellow]Ejecutando monitor de procesos...[/yellow]")
            os.system("top -n 1" if os.name != "nt" else "tasklist")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "2":
            console.print("\n[yellow]Consultando espacio en disco...[/yellow]")
            os.system("df -h" if os.name != "nt" else "wmic logicaldisk get size,freespace,caption")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "3":
            console.print("\n[yellow]Consultando interfaces de red...[/yellow]")
            os.system("ip a" if os.name != "nt" else "ipconfig")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "0":
            break
        else:
            console.print("\n[bold red]❌ Opción inválida.[/bold red]")
            input("Presiona Enter...")


# ==========================================
# 2. SUBMENÚ: Ciberseguridad & Redes (Opción 2)
# ==========================================
def menu_ciberseguridad():
    while True:
        console.clear()
        panel = Panel(
            Align.center("[bold bright_red]🛡️ CIBERSEGURIDAD & REDES 🛡️[/bold bright_red]\n[dim]Herramientas de análisis, escaneo y hashes[/dim]"),
            border_style="bright_red",
            padding=(1, 2)
        )
        console.print(panel)
        console.print()
        
        console.print("[bold red][1][/bold red] 🔍 Escaneo de puertos rápido (ping / nmap)")
        console.print("[bold red][2][/bold red] 🔑 Generar Hash (MD5 / SHA256)")
        console.print("[bold red][3][/bold red] 📹 Verificar estado de cámaras / RTSP")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        sub_op = input("\n[bold bright_yellow]👉 Selecciona opción [0-3]:[/bold bright_yellow] ").strip()

        if sub_op == "1":
            target = input("\nIngresá la IP o Host a verificar: ")
            os.system(f"ping -c 4 {target}" if os.name != "nt" else f"ping {target}")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "2":
            import hashlib
            texto = input("\nIngresá el texto a hashear: ")
            print(f"MD5:    {hashlib.md5(texto.encode()).hexdigest()}")
            print(f"SHA256: {hashlib.sha256(texto.encode()).hexdigest()}")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "3":
            console.print("\n[yellow]Verificando herramientas multimedia/red para cámaras...[/yellow]")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "0":
            break
        else:
            console.print("\n[bold red]❌ Opción inválida.[/bold red]")
            input("Presiona Enter...")


# ==========================================
# 3. SUBMENÚ: Módulo Multimedia (Opción 3)
# ==========================================
def menu_multimedia():
    while True:
        console.clear()
        panel = Panel(
            Align.center("[bold bright_magenta]🎬 MÓDULO MULTIMEDIA 🎬[/bold bright_magenta]\n[dim]Utilidades de audio, video e imágenes[/dim]"),
            border_style="bright_magenta",
            padding=(1, 2)
        )
        console.print(panel)
        console.print()
        
        console.print("[bold magenta][1][/bold magenta] 🎵 Reproducir audio / streaming")
        console.print("[bold magenta][2][/bold magenta] 🎥 Información de codec de video (FFmpeg)")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        sub_op = input("\n[bold bright_yellow]👉 Selecciona opción [0-2]:[/bold bright_yellow] ").strip()

        if sub_op == "1":
            console.print("\n[yellow]Iniciando gestor de audio...[/yellow]")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "2":
            os.system("ffmpeg -version")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "0":
            break
        else:
            console.print("\n[bold red]❌ Opción inválida.[/bold red]")
            input("Presiona Enter...")


# ==========================================
# 4. SUBMENÚ: Gestor PIP (Opción 4)
# ==========================================
def menu_pip():
    while True:
        console.clear()
        panel = Panel(
            Align.center("[bold bright_yellow]📦 GESTOR PIP DE PYTHON 📦[/bold bright_yellow]\n[dim]Administración de paquetes y librerías[/dim]"),
            border_style="bright_yellow",
            padding=(1, 2)
        )
        console.print(panel)
        console.print()
        
        console.print("[bold yellow][1][/bold yellow] 📋 Listar paquetes instalados (pip list)")
        console.print("[bold yellow][2][/bold yellow] 📥 Instalar un nuevo paquete (pip install)")
        console.print("[bold yellow][3][/bold yellow] 🔄 Actualizar paquete")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        sub_op = input("\n[bold bright_yellow]👉 Selecciona opción [0-3]:[/bold bright_yellow] ").strip()

        if sub_op == "1":
            os.system("pip list")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "2":
            pkg = input("\nIngresá el nombre del paquete a instalar: ")
            os.system(f"pip install {pkg}")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "3":
            pkg = input("\nIngresá el paquete a actualizar: ")
            os.system(f"pip install --upgrade {pkg}")
            input("\n[green]Presiona Enter para continuar...[/green]")
        elif sub_op == "0":
            break
        else:
            console.print("\n[bold red]❌ Opción inválida.[/bold red]")
            input("Presiona Enter...")


# ==========================================
# 5. SUBMENÚ DE GIT (Opción 5)
# ==========================================
def menu_git():
    while True:
        console.clear()
        panel_git = Panel(
            Align.center("[bold bright_blue]☁️ GESTOR DE SINCRONIZACIÓN GIT ☁️[/bold bright_blue]\n[dim]Control de versiones y repositorios[/dim]"),
            border_style="bright_blue",
            padding=(1, 2)
        )
        console.print(panel_git)
        console.print()
        
        console.print("[bold cyan][1][/bold cyan] ⬆️ Subir cambios a GitHub (Add, Commit, Push)")
        console.print("[bold cyan][2][/bold cyan] ⬇️ Actualizar repositorio (Git Pull)")
        console.print("[bold red][0][/bold red] ↩️ Volver al Menú Principal")

        sub_op = input("\n[bold bright_yellow]👉 Selecciona opción [0-2]:[/bold bright_yellow] ").strip()

        if sub_op == "1":
            console.print("\n[bold yellow]⚡ Subiendo cambios al repositorio...[/bold yellow]")
            os.system("git add .")
            mensaje_commit = input("📝 Ingresá el mensaje para el commit: ")
            os.system(f'git commit -m "{mensaje_commit}"')
            os.system("git push")
            input("\n[bold green]✔ Proceso finalizado. Presiona Enter...[/bold green]")
        elif sub_op == "2":
            console.print("\n[bold yellow]⚡ Actualizando desde el repositorio...[/bold yellow]")
            os.system("git pull")
            input("\n[bold green]✔ Proceso finalizado. Presiona Enter...[/bold green]")
        elif sub_op == "0":
            break
        else:
            console.print("\n[bold red]❌ Opción inválida.[/bold red]")
            input("Presiona Enter...")


# ==========================================
# 6. ENVIAR MENSAJE POR RED
# ==========================================
def enviar_mensaje_menu():
    console.clear()
    panel_red = Panel(
        Align.center("[bold bright_cyan]📡 MÓDULO DE REDES - SOCKETS 📡[/bold bright_cyan]\n[dim]Comunicación directa por red local[/dim]"),
        border_style="bright_cyan",
        padding=(1, 2)
    )
    console.print(panel_red)
    console.print()

    ip_destino = input("🌐 Ingresá la IP de destino (ej. 127.0.0.1): ")
    puerto_destino = int(input("🔌 Ingresá el puerto (ej. 5000): "))
    mensaje = input("💬 Escribí el mensaje que querés enviar: ")

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip_destino, puerto_destino))
        cliente.send(mensaje.encode("utf-8"))
        console.print("\n[bold green]✔ [+] ¡Mensaje enviado con éxito a la red![/bold green]")
        cliente.close()
    except Exception as e:
        console.print(f"\n[bold red]❌ [-] Error de conexión: {e}[/bold red]")

    console.print("\n[bold yellow]👉 Presiona Enter para volver al menú...[/bold yellow]", end="")
    input()


# ==========================================
# 7. CHAT CON IA (GEMINI)
# ==========================================
def chat_con_ia_menu():
    try:
        client = genai.Client()
    except Exception:
        console.clear()
        console.print(Panel("[bold red]❌ Error: Asegurate de configurar tu GEMINI_API_KEY en las variables de entorno.[/bold red]", border_style="red"))
        input("\n[bold yellow]Presiona Enter para continuar...[/bold yellow]")
        return

    console.clear()
    panel_ia = Panel(
        Align.center("[bold bright_magenta]🤖 ASISTENTE VIRTUAL - GEMINI 2.5 FLASH[/bold bright_magenta]\n[dim]Escribí 'salir' para volver al menú principal[/dim]"),
        border_style="bright_magenta",
        padding=(1, 2)
    )
    console.print(panel_ia)

    try:
        chat = client.chats.create(model="gemini-2.5-flash")
    except Exception as e:
        console.print(f"\n[bold red]❌ Error al iniciar el chat: {e}[/bold red]")
        input("\n[bold yellow]Presiona Enter para continuar...[/bold yellow]")
        return

    while True:
        pregunta = input("\n[bold bright_cyan]👤 Tú:[/bold bright_cyan] ")
        if pregunta.lower() in ["salir", "exit", "q"]:
            break
        
        try:
            console.print("[bold yellow]⚡ Pensando respuesta...[/bold yellow]")
            respuesta = chat.send_message(pregunta)
            console.print(f"\n[bold bright_green]🤖 Gemini:[/bold bright_green] {respuesta.text}")
        except Exception as e:
            console.print(f"\n[bold red]❌ Error al comunicarse con la IA: {e}[/bold red]")


# ==========================================
# BUCLE PRINCIPAL DEL MENÚ
# ==========================================
def mostrar_menu():
    while True:
        console.clear()

        titulo_panel = Panel(
            Align.center("[bold bright_yellow]⚡ CENTRO DE COMANDOS MAESTRO ⚡[/bold bright_yellow]\n[italic bright_cyan]Panel Operativo v2.0 | Terminal de Control[/italic bright_cyan]"),
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
        table.add_column("Módulo / Herramienta", style="bold white")
        table.add_column("Estado", style="dim cyan", justify="center")

        table.add_row("[bold]1[/bold]", "💻  Módulo de Sistema", "[green]● Activo[/green]")
        table.add_row("[bold]2[/bold]", "🛡️   Ciberseguridad & Redes (Cámaras / Hashes)", "[green]● Activo[/green]")
        table.add_row("[bold]3[/bold]", "🎬  Módulo Multimedia", "[green]● Activo[/green]")
        table.add_row("[bold]4[/bold]", "📦  Gestor PIP", "[green]● Activo[/green]")
        table.add_row("[bold]5[/bold]", "☁️   Sincronización Git (Subir / Actualizar)", "[bright_cyan]🔄 Git[/bright_cyan]")
        table.add_row("[bold]6[/bold]", "💬  Enviar Mensaje por Red Local (Sockets)", "[bright_yellow]⚡ Red[/bright_yellow]")
        table.add_row("[bold]7[/bold]", "🤖  Chat con IA (Gemini 2.5 Flash)", "[bright_magenta]✨ IA[/bright_magenta]")
        table.add_row("[bold]0[/bold]", "❌  Salir del Sistema", "[red]○ Off[/red]")

        console.print(Align.center(table))
        console.print(Align.center("\n[dim bright_white]────────────── Status: Sistema listo para recibir instrucciones ──────────────[/dim bright_white]"))

        opcion = input("\n[bold bright_yellow]👉 Selecciona una opción [0-7]:[/bold bright_yellow] ").strip()

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
        elif opcion == "0":
            console.print("\n[bold bright_red]Saliendo del Centro de Comandos... ¡Hasta luego![/bold bright_red]")
            break
        else:
            console.print("[bold red]❌ Opción inválida. Intenta nuevamente.[/bold red]")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    mostrar_menu()