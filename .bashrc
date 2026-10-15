# Función para mostrar el saludo con Rich
mostrar_saludo() {
    clear
    python3 -c '
try:
    from rich import print
    from rich.panel import Panel
    import datetime
    hora = datetime.datetime.now().strftime("%H:%M")
    print(Panel(f"[bold cyan]✨ ¡HOLA MARTÍN! ✨[/bold cyan]\n[italic dim]🕒 Hora actual: {hora}[/italic dim]\n\n[yellow]💡 Escribe [bold]menu[/bold] para abrir el Centro de Comandos[/yellow]", border_style="cyan"))
except:
    print("=== ✨ HOLA MARTÍN ✨ ===")
    print("Escribe '\''menu'\'' para abrir el Centro de Comandos")
'
}

# Alias inteligente que abre el menú y al salir vuelve a mostrar el saludo

# Ejecutamos el saludo al abrir la terminal
mostrar_saludo
alias menu='python ~/menu.py'
alias menú='python ~/menu.py'
