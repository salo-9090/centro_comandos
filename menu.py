import os
import socket
import subprocess
import hashlib
import secrets
import string
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def limpiar():
    os.system('clear')

def obtener_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def modulo_sistema():
    limpiar()
    console.print(Panel("[bold cyan]📊 Módulo de Sistema[/bold cyan]\n[dim]Diagnóstico y estado del entorno actual[/dim]", expand=False))
    res = subprocess.run(["uname", "-a"], capture_output=True, text=True)
    console.print(f"\n[green]Información del Sistema:[/green]\n{res.stdout}")
    console.print("\n[yellow]Presiona Enter para volver...[/yellow]", end="")
    input()

def modulo_ciberseguridad():
    while True:
        limpiar()
        console.print(Panel("[bold red]🛡️ Ciberseguridad & Redes[/bold red]\n[dim]Herramientas de auditoría local, puertos y cámaras[/dim]", expand=False))
        
        tabla = Table(title="Panel de Auditoría Avanzada")
        tabla.add_column("Opción", style="cyan", justify="center")
        tabla.add_column("Herramienta / Acción", style="green")
        tabla.add_column("Descripción", style="dim white")
        
        tabla.add_row("1", "Ver IP local y red", "Muestra tu dirección IP y configuración.")
        tabla.add_row("2", "Ping a Google (Internet)", "Verifica conectividad y salida a la web.")
        tabla.add_row("3", "Escanear red local (Ping 1-250)", "Mapea los dispositivos activos en el Wi-Fi.")
        tabla.add_row("4", "Tabla ARP de dispositivos", "Lista las conexiones recientes de la red.")
        tabla.add_row("5", "Escanear puertos en una IP", "Revisa servicios abiertos (HTTP, SSH, etc.).")
        tabla.add_row("6", "Generador de Contraseñas", "Crea claves seguras con alta entropía.")
        tabla.add_row("7", "Auditor MD5 por Diccionario", "Prueba hashes contra un wordlist.txt.")
        tabla.add_row("8", "Calculadora Multihash", "Convierte textos a MD5 y SHA256.")
        tabla.add_row("9", "Ejecutar comando Bash", "Lanza comandos del sistema operativo al instante.")
        tabla.add_row("10", "📷 Escáner de Cámaras IP", "Busca cámaras y dispositivos de video en la red.")
        tabla.add_row("0", "Volver al Menú Principal", "Regresa al panel general.")
        
        console.print(tabla)
        
        op = input("\nSelecciona una opción [0-10]: ").strip()
        
        if op == "1":
            limpiar()
            console.print(f"[green]Tu IP local:[/green] [cyan]{obtener_ip()}[/cyan]\n")
            os.system("ip addr")
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()
            
        elif op == "2":
            limpiar()
            os.system("ping -c 4 8.8.8.8")
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()
            
        elif op == "3":
            limpiar()
            ip_l = obtener_ip()
            seg = ".".join(ip_l.split(".")[:-1]) + "."
            console.print(f"[yellow]Escaneando segmento {seg}1-250...[/yellow]\n")
            for i in range(1, 251):
                res = os.system(f"ping -c 1 -W 1 {seg}{i} > /dev/null 2>&1")
                if res == 0:
                    console.print(f"[green][+] Dispositivo activo:[/green] {seg}{i}")
            console.print("\n[yellow]Escaneo finalizado. Presiona Enter...[/yellow]", end="")
            input()

        elif op == "4":
            limpiar()
            os.system("arp -a")
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()

        elif op == "5":
            limpiar()
            target = input("Ingresa la IP a escanear (Ej. 127.0.0.1): ").strip() or "127.0.0.1"
            puertos = [21, 22, 80, 443, 3306, 8080]
            for p in puertos:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                if s.connect_ex((target, p)) == 0:
                    console.print(f"Puerto {p}: [green]ABIERTO 🟢[/green]")
                else:
                    console.print(f"Puerto {p}: [red]Cerrado 🔴[/red]")
                s.close()
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()

        elif op == "6":
            limpiar()
            chars = string.ascii_letters + string.digits + string.punctuation
            pwd = ''.join(secrets.choice(chars) for _ in range(16))
            console.print(f"\n[green]Contraseña generada:[/green] [yellow]{pwd}[/yellow]")
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()

        elif op == "7":
            limpiar()
            console.print(Panel("[bold cyan]🔓 Auditor MD5 por Diccionario[/bold cyan]", expand=False))
            wl = os.path.expanduser("~/wordlist.txt")
            if not os.path.exists(wl):
                with open(wl, "w") as f:
                    f.write("123456\npassword\nadmin\nsalomon1030\n")
            h_obj = input("Ingresa el Hash MD5 a auditar: ").strip()
            if h_obj:
                encontrado = False
                with open(wl, "r", encoding="utf-8", errors="ignore") as f:
                    for linea in f:
                        palabra = linea.strip()
                        if hashlib.md5(palabra.encode()).hexdigest().lower() == h_obj.lower():
                            console.print(f"\n[green]¡CONTRASEÑA ENCONTRADA!:[/green] [bold yellow]{palabra}[/bold yellow]")
                            encontrado = True
                            break
                if not encontrado:
                    console.print("\n[red]❌ No se encontró coincidencia en el diccionario.[/red]")
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()

        elif op == "8":
            limpiar()
            console.print(Panel("[bold cyan]🔑 Calculadora Multihash[/bold cyan]", expand=False))
            texto = input("Texto a transformar: ").strip() or "CentroDeComandos"
            console.print(f"\n[green]MD5:[/green] {hashlib.md5(texto.encode()).hexdigest()}")
            console.print(f"[green]SHA256:[/green] {hashlib.sha256(texto.encode()).hexdigest()}")
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()

        elif op == "9":
            limpiar()
            cmd = input("Comando Bash: ")
            if cmd.strip():
                os.system(cmd)
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()

        elif op == "10":
            limpiar()
            console.print(Panel("[bold cyan]📷 Escáner de Cámaras IP y Dispositivos[/bold cyan]", expand=False))
            ip_l = obtener_ip()
            seg = ".".join(ip_l.split(".")[:-1]) + "."
            console.print(f"[yellow]Buscando cámaras en {seg}0/24 (Puertos 80, 554, 8080, 8000, 37777)...[/yellow]\n")
            puertos_camara = [80, 554, 8080, 8000, 37777]
            
            def scan(i):
                t = f"{seg}{i}"
                for p in puertos_camara:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(0.2)
                        if s.connect_ex((t, p)) == 0:
                            console.print(f"[green]🟢 Dispositivo/Cámara detectado![/green] IP: [cyan]{t}[/cyan] | Puerto: [yellow]{p}[/yellow]")
                        s.close()
                    except:
                        pass

            with ThreadPoolExecutor(max_workers=30) as ex:
                ex.map(scan, range(1, 255))
            
            console.print(f"\n[bold green]Escaneo finalizado.[/bold green]")
            console.print("\n[yellow]Presiona Enter para continuar...[/yellow]", end="")
            input()

        elif op == "0":
            break

def modulo_multimedia():
    limpiar()
    console.print(Panel("[bold magenta]🎬 Módulo Multimedia[/bold magenta]\n[dim]Herramientas multimedia y reproducción[/dim]", expand=False))
    console.print("\n[yellow]Presiona Enter para volver...[/yellow]", end="")
    input()

def modulo_pip():
    limpiar()
    console.print(Panel("[bold yellow]📦 Gestor de Librerías PIP[/bold yellow]\n[dim]Listado de paquetes instalados[/dim]", expand=False))
    subprocess.run(["pip", "list"])
    console.print("\n[yellow]Presiona Enter para volver...[/yellow]", end="")
    input()

def modulo_git():
    while True:
        limpiar()
        console.print(Panel("[bold blue]☁️ Sincronización Git[/bold blue]", expand=False))
        tabla_git = Table(title="Control de Versiones Git")
        tabla_git.add_column("Opción", style="cyan", justify="center")
        tabla_git.add_column("Acción", style="green")
        tabla_git.add_row("1", "📥 Git Pull (Actualizar)")
        tabla_git.add_row("2", "📤 Git Push (Guardar cambios)")
        tabla_git.add_row("3", "📊 Git Status (Estado)")
        tabla_git.add_row("0", "⬅️ Volver")
        console.print(tabla_git)
        
        op = input("\nSelecciona una opción: ").strip()
        if op == "1":
            subprocess.run(["git", "pull", "origin", "main"])
            console.print("\n[yellow]Enter para continuar...[/yellow]", end="")
            input()
        elif op == "2":
            subprocess.run(["git", "add", "."])
            msg = input("Mensaje del commit: ") or "Actualización menú completo"
            subprocess.run(["git", "commit", "-m", msg])
            subprocess.run(["git", "push"])
            console.print("\n[yellow]Enter para continuar...[/yellow]", end="")
            input()
        elif op == "3":
            subprocess.run(["git", "status"])
            console.print("\n[yellow]Enter para continuar...[/yellow]", end="")
            input()
        elif op == "0":
            break

def main():
    while True:
        limpiar()
        console.print(Panel("[bold yellow]✨ CENTRO DE COMANDOS MAESTRO ✨[/bold yellow]", expand=False))
        
        tabla_ppal = Table(title="Menú Principal")
        tabla_ppal.add_column("Opción", style="cyan", justify="center")
        tabla_ppal.add_column("Módulo", style="green")
        
        tabla_ppal.add_row("1", "📊 Módulo de Sistema")
        tabla_ppal.add_row("2", "🛡️ Ciberseguridad & Redes (Cámaras / Hashes)")
        tabla_ppal.add_row("3", "🎬 Módulo Multimedia")
        tabla_ppal.add_row("4", "📦 Gestor PIP")
        tabla_ppal.add_row("5", "☁️ Sincronización Git")
        tabla_ppal.add_row("0", "❌ Salir")
        
        console.print(tabla_ppal)
        
        op = input("\nSelecciona opción [0-5]: ").strip()
        if op == "1":
            modulo_sistema()
        elif op == "2":
            modulo_ciberseguridad()
        elif op == "3":
            modulo_multimedia()
        elif op == "4":
            modulo_pip()
        elif op == "5":
            modulo_git()
        elif op == "0":
            console.print("[red]Saliendo del Centro de Comandos...[/red]")
            break

if __name__ == "__main__":
    main()
