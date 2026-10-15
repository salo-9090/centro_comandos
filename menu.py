import os
import socket
import subprocess
import hashlib
import secrets
import string
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def modulo_sistema():
    limpiar_pantalla()
    console.print(Panel("[bold cyan]📊 Módulo de Sistema[/bold cyan]\n[dim]Propósito: Monitoreo y diagnóstico del sistema operativo y entorno actual.[/dim]", expand=False))
    res = subprocess.run(["uname", "-a"], capture_output=True, text=True)
    console.print(f"\nInformación del Sistema:\n[green]{res.stdout}[/green]")
    console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
    input()

def obtener_ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def modulo_ciberseguridad():
    while True:
        limpiar_pantalla()
        console.print(Panel("[bold red]🛡️ Ciberseguridad & Redes (Herramientas Reales)[/bold red]\n[dim]Propósito: Auditoría de redes, análisis de puertos y cracking real con John the Ripper.[/dim]", expand=False))
        
        tabla = Table(title="Herramientas de Auditoría Avanzada")
        tabla.add_column("Opción", style="cyan", justify="center")
        tabla.add_column("Herramienta / Acción", style="green")
        tabla.add_column("Descripción / Uso Práctico", style="dim white")
        
        tabla.add_row("1", "Ver IP local e interfaces de red", "[1] Muestra la dirección IP actual y configuración de red.")
        tabla.add_row("2", "Prueba de conectividad (Ping a Google)", "[2] Verifica salida a internet y latencia.")
        tabla.add_row("3", "Escanear dispositivos activos (Ping 1-250)", "[3] Mapea la red local completa (límite de 2 min).")
        tabla.add_row("4", "Escáner ARP de Dispositivos Locales", "[4] Lista dispositivos mediante la tabla ARP.")
        tabla.add_row("5", "Escanear puertos comunes en una IP", "[5] Revisa servicios abiertos (HTTP, SSH, MySQL, MU Online).")
        tabla.add_row("6", "Inspección de Banner (Banner Grabbing)", "[6] Captura la versión de software expuesta en un puerto.")
        tabla.add_row("7", "Resolver Dominio a Dirección IP", "[7] Traduce sitios web a IPs mediante DNS.")
        tabla.add_row("8", "🔐 Generador de Claves y Entropía", "[8] Crea contraseñas ultraseguras con alta aleatoriedad.")
        tabla.add_row("9", "🔓 Auditor Real de Hashes (John the Ripper)", "[9] Ataque de diccionario real sobre hashes MD5/SHA usando John.")
        tabla.add_row("10", "🔑 Calculadora Multihash (MD5/SHA256/SHA512)", "[10] Convierte texto en múltiples formatos hash.")
        tabla.add_row("11", "💻 Ejecutar comando Bash personalizado", "[11] Lanza comandos del sistema operativo al instante.")
        tabla.add_row("0", "Volver al Menú Principal", "[0] Retorna al panel general.")
        tabla.add_row("SALIR", "🚪 Cierre total", "[SALIR] Cierra la aplicación.")
        
        console.print(tabla)
        
        opcion = input("\nSelecciona una opción [1-11/0/SALIR]: ").strip().upper()
        
        if opcion == "1":
            limpiar_pantalla()
            ip_local = obtener_ip_local()
            console.print(f"Tu IP local detectada: [green]{ip_local}[/green]\n")
            subprocess.run(["ip", "addr"])
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")
            
        elif opcion == "2":
            limpiar_pantalla()
            subprocess.run(["ping", "-c", "4", "8.8.8.8"])
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")
            
        elif opcion == "3":
            limpiar_pantalla()
            ip_local = obtener_ip_local()
            segmento = ".".join(ip_local.split(".")[:-1]) + "."
            console.print(f"[bold yellow]Iniciando escaneo en {segmento}1-250 (Límite: 2 min)...[/bold yellow]\n")
            
            inicio_tiempo = time.time()
            for i in range(1, 251):
                if time.time() - inicio_tiempo > 120:
                    break
                subprocess.run(["ping", "-c", "1", "-W", "1", f"{segmento}{i}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            console.print("[green]Escaneo finalizado.[/green]")
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

        elif opcion == "4":
            limpiar_pantalla()
            subprocess.run(["arp", "-a"])
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")
            
        elif opcion == "5":
            limpiar_pantalla()
            target = input("Ingresa la IP a escanear (Ej. 127.0.0.1): ") or "127.0.0.1"
            puertos = {21: "FTP", 22: "SSH", 80: "HTTP", 3306: "MySQL", 55901: "MU-GameServer"}
            for p, serv in puertos.items():
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                res = s.connect_ex((target, p))
                estado = "[green]ABIERTO 🟢[/green]" if res == 0 else "[red]Cerrado 🔴[/red]"
                console.print(f"Puerto {p} ({serv}): {estado}")
                s.close()
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

        elif opcion == "6":
            limpiar_pantalla()
            target_bg = input("Ingresa la IP o dominio: ").strip() or "127.0.0.1"
            port_bg = int(input("Ingresa el puerto (Ej. 80, 21): ") or "80")
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2.0)
                s.connect((target_bg, port_bg))
                banner = s.recv(1024).decode('utf-8', errors='ignore')
                if banner.strip():
                    console.print(f"[bold green]Banner Capturado:[/bold green]\n{banner}")
                else:
                    console.print("[yellow]Puerto abierto pero sin banner automático.[/yellow]")
                s.close()
            except Exception as e:
                console.print(f"[bold red]Error: {e}[/bold red]")
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

        elif opcion == "7":
            limpiar_pantalla()
            dominio = input("Ingresa el sitio o dominio: ")
            if dominio.strip():
                try:
                    ip_res = socket.gethostbyname(dominio)
                    console.print(f"\n[green]IP asociada a {dominio}:[/green] [bold cyan]{ip_res}[/bold cyan]")
                except Exception as e:
                    console.print(f"[bold red]Error: {e}[/bold red]")
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

        elif opcion == "8":
            limpiar_pantalla()
            longitud = int(input("Longitud de la contraseña: ") or "16")
            caracteres = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
            console.print(f"\n[green]Contraseña Generada:[/green] [bold yellow]{password}[/bold yellow]")
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

        elif opcion == "9":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🔓 Auditor Real de Hashes (John the Ripper)[/bold cyan]\n[dim]Uso: Evalúa la resistencia de un hash MD5 utilizando diccionarios reales instalados en el sistema.[/dim]", expand=False))
            
            hash_objetivo = input("Ingresa el Hash MD5 a auditar (o Enter para usar uno de prueba): ").strip()
            if not hash_objetivo:
                hash_objetivo = "c70289d5a8057b569e01356c303ad98"
                console.print(f"[yellow]Usando hash de prueba: {hash_objetivo}[/yellow]")
            
            hash_file = "hash_target.txt"
            with open(hash_file, "w") as f:
                f.write(f"test_user:{hash_objetivo}\n")
                
            console.print(f"\n[bold yellow]Iniciando motor de John the Ripper...[/bold yellow]\n")
            subprocess.run(["john", "--format=raw-md5", hash_file])
            
            console.print("\n[bold green]Resultados de la auditoría:[/bold green]")
            subprocess.run(["john", "--show", hash_file])
            
            if os.path.exists(hash_file):
                os.remove(hash_file)
                
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

        elif opcion == "10":
            limpiar_pantalla()
            texto = input("Texto a transformar: ").strip() or "CentroDeComandos"
            console.print(f"\n[green]MD5:[/green] {hashlib.md5(texto.encode()).hexdigest()}")
            console.print(f"[green]SHA256:[/green] {hashlib.sha256(texto.encode()).hexdigest()}")
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

        elif opcion == "11":
            limpiar_pantalla()
            cmd = input("Comando Bash: ")
            if cmd.strip():
                os.system(cmd)
            input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

        elif opcion == "0":
            break
        elif opcion == "SALIR":
            return "SALIR_TOTAL"

def modulo_multimedia():
    limpiar_pantalla()
    console.print(Panel("[bold magenta]🎬 Módulo Multimedia[/bold magenta]", expand=False))
    input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

def modulo_pip():
    limpiar_pantalla()
    console.print(Panel("[bold yellow]📦 Gestor de Librerías PIP[/bold yellow]", expand=False))
    subprocess.run(["pip", "list"])
    input("\n[bold yellow]Presiona Enter para volver...[/bold yellow]")

def modulo_git():
    while True:
        limpiar_pantalla()
        console.print(Panel("[bold blue]☁️ Sincronización Git[/bold blue]", expand=False))
        tabla_git = Table(title="Control Git")
        tabla_git.add_column("Opción", style="cyan", justify="center")
        tabla_git.add_column("Acción", style="green")
        tabla_git.add_row("1", "📥 Git Pull")
        tabla_git.add_row("2", "📤 Git Push (Subir cambios a GitHub)")
        tabla_git.add_row("3", "📊 Git Status")
        tabla_git.add_row("0", "⬅️ Volver")
        console.print(tabla_git)
        
        op = input("\nSelecciona una opción: ").strip()
        if op == "1":
            subprocess.run(["git", "pull", "origin", "main"])
            input("\nEnter para continuar...")
        elif op == "2":
            subprocess.run(["git", "add", "."])
            msg = input("Mensaje del commit: ") or "Actualización desde Centro de Comandos"
            subprocess.run(["git", "commit", "-m", msg])
            subprocess.run(["git", "push"])
            input("\nEnter para continuar...")
        elif op == "3":
            subprocess.run(["git", "status"])
            input("\nEnter para continuar...")
        elif op == "0":
            break

def main():
    while True:
        limpiar_pantalla()
        console.print(Panel("[bold yellow]✨ CENTRO DE COMANDOS MAESTRO ✨[/bold yellow]", expand=False))
        tabla = Table(title="Menú Principal")
        tabla.add_column("Opción", style="cyan", justify="center")
        tabla.add_column("Módulo", style="green")
        tabla.add_row("1", "📊 Módulo de Sistema")
        tabla.add_row("2", "🛡️ Ciberseguridad & Redes (John the Ripper)")
        tabla.add_row("3", "🎬 Módulo Multimedia")
        tabla.add_row("4", "📦 Gestor PIP")
        tabla.add_row("5", "☁️ Sincronización Git")
        tabla.add_row("0", "❌ Salir")
        console.print(tabla)
        
        opcion = input("\nSelecciona una opción [1-5/0]: ").strip().upper()
        res = None
        if opcion == "1":
            modulo_sistema()
        elif opcion == "2":
            res = modulo_ciberseguridad()
        elif opcion == "3":
            modulo_multimedia()
        elif opcion == "4":
            modulo_pip()
        elif opcion == "5":
            modulo_git()
        elif opcion == "0":
            break
            
        if res == "SALIR_TOTAL":
            break

if __name__ == "__main__":
    main()
