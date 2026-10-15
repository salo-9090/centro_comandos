import socket
import os
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


# ==========================================
# 1. FUNCIÓN: Enviar mensaje por red local
# ==========================================
def enviar_mensaje_menu():
  console.print(
      "\n[bold magenta]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold"
      " magenta]"
  )
  console.print(
      "[bold cyan]📡 ENVIAR MENSAJE POR RED LOCAL[/bold cyan]",
      justify="center",
  )
  console.print(
      "[bold magenta]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold"
      " magenta]\n"
  )

  ip_destino = input("🌐 Ingresá la IP de destino (ej. 127.0.0.1): ")
  puerto_destino = int(input("🔌 Ingresá el puerto (ej. 5000): "))
  mensaje = input("💬 Escribí el mensaje que querés enviar: ")

  try:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ip_destino, puerto_destino))
    cliente.send(mensaje.encode("utf-8"))
    console.print(
        "\n[bold green]✔ [+] ¡Mensaje enviado con éxito a la"
        " red![/bold green]"
    )
    cliente.close()
  except Exception as e:
    console.print(
        f"\n[bold red]❌ [-] Error de conexión: {e}[/bold red]"
    )

  console.print(
      "\n[bold yellow]👉 Presiona Enter para continuar...[/bold yellow]", end=""
  )
  input()


# ==========================================
# 2. FUNCIÓN: Chat con IA en la terminal
# ==========================================
def chat_con_ia_menu():
  try:
    client = genai.Client()
  except Exception:
    console.print(
        "[bold red]❌ Error: Asegurate de configurar tu GEMINI_API_KEY en las"
        " variables de entorno.[/bold red]"
    )
    console.print(
        "\n[bold yellow]👉 Presiona Enter para continuar...[/bold yellow]",
        end="",
    )
    input()
    return

  console.print(
      "\n[bold magenta]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold"
      " magenta]"
  )
  console.print(
      "[bold bright_cyan]🤖 CHAT CON IA - GEMINI[/bold bright_cyan]",
      justify="center",
  )
  console.print(
      "[dim](Escribí 'salir' para volver al menú principal)[/dim]",
      justify="center",
  )
  console.print(
      "[bold magenta]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold"
      " magenta]\n"
  )

  try:
    chat = client.chats.create(model="gemini-2.5-flash")
  except Exception as e:
    console.print(
        f"[bold red]❌ Error al iniciar el chat: {e}[/bold red]"
    )
    console.print(
        "\n[bold yellow]👉 Presiona Enter para continuar...[/bold yellow]",
        end="",
    )
    input()
    return

  while True:
    pregunta = input("\n👤 Tú: ")
    if pregunta.lower() in ["salir", "exit", "q"]:
      break

    try:
      console.print("[bold yellow]⚡ Pensando...[/bold yellow]")
      respuesta = chat.send_message(pregunta)
      console.print(
          f"\n[bold bright_green]🤖 Gemini:[/bold bright_green] {respuesta.text}"
      )
    except Exception as e:
      console.print(
          f"[bold red]❌ Error al comunicarse con la IA: {e}[/bold red]"
      )


# ==========================================
# 3. SUBMENÚ DE GIT (Opción 5)
# ==========================================
def menu_git():
  while True:
    console.clear()
    console.print(
        Panel.fit(
            "[bold cyan]☁️ GESTOR DE SINCRONIZACIÓN GIT ☁️[/bold cyan]",
            border_style="cyan",
        )
    )
    console.print("[1] ⬆️ Subir cambios a GitHub (Add, Commit, Push)")
    console.print("[2] ⬇️ Actualizar repositorio (Git Pull)")
    console.print("[0] ↩️ Volver al Menú Principal")

    sub_op = input("\n👉 Selecciona opción [0-2]: ").strip()

    if sub_op == "1":
      console.print(
          "[yellow]Subiendo cambios al repositorio...[/yellow]"
      )
      os.system("git add .")
      mensaje_commit = input("Ingresá el mensaje para el commit: ")
      os.system(f'git commit -m "{mensaje_commit}"')
      os.system("git push")
      input("\n[green]✔ Proceso finalizado. Presiona Enter...[/green]")
    elif sub_op == "2":
      console.print("[yellow]Actualizando desde el repositorio...[/yellow]")
      os.system("git pull")
      input("\n[green]✔ Proceso finalizado. Presiona Enter...[/green]")
    elif sub_op == "0":
      break
    else:
      console.print("[red]Opción inválida.[/red]")
      input("Presiona Enter...")


# ==========================================
# 4. BUCLE PRINCIPAL DEL MENÚ
# ==========================================
def mostrar_menu():
  while True:
    console.clear()

    titulo_panel = Panel(
        "[bold bright_yellow]⚡ CENTRO DE COMANDOS MAESTRO"
        " ⚡[/bold bright_yellow]\n[italic bright_cyan]Panel Operativo v2.0 |"
        " Terminal de Control[/italic bright_cyan]",
        border_style="bright_magenta",
        padding=(1, 4),
    )
    console.print(titulo_panel, justify="center")

    table = Table(
        show_header=True,
        header_style="bold bright_white on blue",
        border_style="bright_cyan",
        title_style="bold bright_yellow",
        expand=False,
    )

    table.add_column("Opción", style="bold bright_green", justify="center")
    table.add_column("Módulo / Herramienta", style="bold white")
    table.add_column("Estado", style="dim cyan", justify="center")

    table.add_row(
        "[1]", "💻  Módulo de Sistema", "[green]● Activo[/green]"
    )
    table.add_row(
        "[2]",
        "🛡️   Ciberseguridad & Redes (Cámaras / Hashes)",
        "[green]● Activo[/green]",
    )
    table.add_row(
        "[3]", "🎬  Módulo Multimedia", "[green]● Activo[/green]"
    )
    table.add_row(
        "[4]", "📦  Gestor PIP", "[green]● Activo[/green]"
    )
    table.add_row(
        "[5]", "☁️   Sincronización Git (Subir / Actualizar)", "[bright_cyan]🔄 Git[/bright_cyan]"
    )
    table.add_row(
        "[6]",
        "💬  Enviar Mensaje por Red Local (Sockets)",
        "[bright_yellow]⚡ Red[/bright_yellow]",
    )
    table.add_row(
        "[7]",
        "🤖  Chat con IA (Gemini 2.5 Flash)",
        "[bright_magenta]✨ IA[/bright_magenta]",
    )
    table.add_row(
        "[0]", "❌  Salir del Sistema", "[red]○ Off[/red]"
    )

    console.print(table)
    console.print(
        "\n[dim bright_white]────────────── Status: Sistema listo para recibir"
        " instrucciones ──────────────[/dim bright_white]"
    )

    opcion = input("\n👉 Selecciona una opción [0-7]: ").strip()

    if opcion == "1":
      console.print("[yellow]Ejecutando Módulo de Sistema...[/yellow]")
      input("Presiona Enter para continuar...")
    elif opcion == "2":
      console.print(
          "[yellow]Ejecutando Ciberseguridad & Redes...[/yellow]"
      )
      input("Presiona Enter para continuar...")
    elif opcion == "3":
      console.print("[yellow]Ejecutando Módulo Multimedia...[/yellow]")
      input("Presiona Enter para continuar...")
    elif opcion == "4":
      console.print("[yellow]Ejecutando Gestor PIP...[/yellow]")
      input("Presiona Enter para continuar...")
    elif opcion == "5":
      menu_git()
    elif opcion == "6":
      enviar_mensaje_menu()
    elif opcion == "7":
      chat_con_ia_menu()
    elif opcion == "0":
      console.print(
          "[bold bright_red]Saliendo del Centro de Comandos... ¡Hasta"
          " luego![/bold bright_red]"
      )
      break
    else:
      console.print(
          "[bold red]❌ Opción inválida. Intenta nuevamente.[/bold red]"
      )
      input("Presiona Enter para continuar...")


if __name__ == "__main__":
  mostrar_menu()