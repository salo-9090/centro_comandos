import os
import socket
import subprocess
import hashlib
import secrets
import string
import urllib.request
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
        console.print(Panel("[bold red]🛡️ Ciberseguridad & Redes[/bold red]\n[dim]Propósito: Auditoría de redes locales, análisis de puertos, criptografía y evaluación defensiva.[/dim]", expand=False))
        
        tabla = Table(title="Herramientas de Red y Auditoría Avanzada")
        tabla.add_column("Opción", style="cyan", justify="center")
        tabla.add_column("Herramienta / Acción", style="green")
        tabla.add_column("Descripción / Uso Práctico", style="dim white")
        
        tabla.add_row("1", "Ver IP local e interfaces de red", "[1] Muestra la dirección IP actual y configuración de red de la máquina.")
        tabla.add_row("2", "Prueba de conectividad (Ping a Google)", "[2] Verifica la salida a internet y mide latencia hacia servidores externos.")
        tabla.add_row("3", "Escanear dispositivos activos (Ping 1-250)", "[3] Busca dispositivos activos en todo el segmento local (con límite de 2 min).")
        tabla.add_row("4", "Escáner ARP de Dispositivos Locales", "[4] Lista los dispositivos en red mediante la tabla ARP del sistema.")
        tabla.add_row("5", "Escanear puertos comunes en una IP", "[5] Revisa qué servicios (HTTP, SSH, MySQL, MU Online) están escuchando.")
        tabla.add_row("6", "Inspección de Banner (Banner Grabbing)", "[6] Se conecta a un puerto para capturar la versión del software remoto.")
        tabla.add_row("7", "Resolver Dominio a Dirección IP", "[7] Traduce nombres de sitios web a sus direcciones IP mediante DNS.")
        tabla.add_row("8", "🔐 Generador de Claves y Entropía", "[8] Crea contraseñas ultraseguras y analiza su aleatoriedad.")
        tabla.add_row("9", "🔓 Auditor de Hashes (Fuerza Bruta)", "[9] Pon a prueba tus propias claves contra un diccionario de ataque.")
        tabla.add_row("10", "🔑 Calculadora Multihash (MD5/SHA256/SHA512)", "[10] Convierte cualquier texto en múltiples formatos de huella hash.")
        tabla.add_row("11", "💻 Ejecutar comando Bash personalizado", "[11] Permite lanzar comandos rápidos del sistema operativo al instante.")
        tabla.add_row("0", "Volver al Menú Principal", "[0] Retorna al panel de control general.")
        tabla.add_row("SALIR", "🚪 Cierre total", "[SALIR] Escribe esta palabra para cerrar el programa desde cualquier submenú.")
        
        console.print(tabla)
        
        opcion = input("\nSelecciona una opción [1-11/0/SALIR]: ").strip().upper()
        
        if opcion == "1":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🌐 Configuración de Red[/bold cyan]\n[dim]Uso: Identificar tu dirección IP asignada para saber desde dónde te comunicas en la red.[/dim]", expand=False))
            ip_local = obtener_ip_local()
            console.print(f"Tu IP local detectada: [green]{ip_local}[/green]\n")
            res = subprocess.run(["ip", "addr"], capture_output=True, text=True)
            console.print(res.stdout)
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()
            
        elif opcion == "2":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🏓 Prueba de Conectividad (Ping)[/bold cyan]\n[dim]Uso: Comprobar el intercambio de paquetes ICMP y medir tiempos de respuesta de la red.[/dim]", expand=False))
            console.print("[bold yellow]Ejecutando: ping -c 4 8.8.8.8[/bold yellow]\n")
            subprocess.run(["ping", "-c", "4", "8.8.8.8"])
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()
            
        elif opcion == "3":
            limpiar_pantalla()
            ip_local = obtener_ip_local()
            console.print(Panel("[bold cyan]🔍 Escáner Masivo de Red (Ping 1-250)[/bold cyan]\n[dim]Uso: Mapear la red local completa buscando equipos activos con control de tiempo de 2 min.[/dim]", expand=False))
            
            console.print(f"[bold cyan]🔍 IP Detectada:[/bold cyan] [green]{ip_local}[/green]")
            console.print("[1] Escanear el segmento de tu IP actual (Ej: 192.168.X.X)")
            console.print("[2] Escanear red doméstica típica (192.168.1.X)")
            sub_op = input("\nElige una opción de red [1/2] (Default 2): ")
            
            if sub_op == "1":
                segmento = ".".join(ip_local.split(".")[:-1]) + "."
            else:
                segmento = "192.168.1."
                
            console.print(f"\n[bold yellow]Iniciando escaneo masivo en el rango {segmento}1 al {segmento}250... (Límite: 2 minutos)[/bold yellow]\n")

            tabla_red = Table(title=f"Dispositivos Activos en Red ({segmento}X)")
            tabla_red.add_column("Dirección IP", style="cyan", justify="center")
            tabla_red.add_column("Estado", style="bold green", justify="center")

            inicio_tiempo = time.time()
            limite_tiempo = 120  # 120 segundos = 2 minutos
            encontrados = 0

            for i in range(1, 251):
                # Control de tiempo máximo (2 minutos)
                if time.time() - inicio_tiempo > limite_tiempo:
                    console.print("\n[bold red]⚠️ Se alcanzó el límite de tiempo de 2 minutos. Deteniendo escaneo por seguridad.[/bold red]")
                    break

                ip_destino = f"{segmento}{i}"
                # Timeout de 0.5s por IP para que sea ágil
                comando = ["ping", "-c", "1", "-W", "1", ip_destino]
                resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                if resultado.returncode == 0:
                    tabla_red.add_row(ip_destino, "ACTIVO 🟢")
                    encontrados += 1

            console.print(tabla_red)
            console.print(f"\n[green]Escaneo finalizado. Dispositivos activos encontrados: {encontrados}[/green]")
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()

        elif opcion == "4":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]📋 Escáner ARP de Dispositivos Locales[/bold cyan]\n[dim]Uso: Extrae la tabla de caché ARP del sistema para listar dispositivos conectados recientemente.[/dim]", expand=False))
            console.print("[bold yellow]Ejecutando comando ARP del sistema...[/bold yellow]\n")
            
            res = subprocess.run(["arp", "-a"], capture_output=True, text=True)
            if res.stdout.strip():
                console.print(f"[green]{res.stdout}[/green]")
            else:
                console.print("[yellow]No se encontraron entradas ARP activas o el comando no está disponible en este entorno.[/yellow]")
                
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()
            
        elif opcion == "5":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🔌 Escáner de Puertos TCP (Python Sockets)[/bold cyan]\n[dim]Uso: Verificar puertos abiertos en servidores o juegos (como servidores de MU Online).[/dim]", expand=False))
            target = input("Ingresa la IP o dominio a escanear (Ej. 127.0.0.1): ") or "127.0.0.1"
            
            puertos = {
                21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 
                53: "DNS", 80: "HTTP", 443: "HTTPS", 3306: "MySQL", 
                44405: "MU-ConnectServer", 55901: "MU-GameServer", 8080: "HTTP-Alt"
            }
            
            console.print(f"\n[bold yellow]Escaneando puertos comunes en {target}...[/bold yellow]\n")
            tabla_puertos = Table(title=f"Resultados de Puertos para {target}")
            tabla_puertos.add_column("Puerto", style="cyan", justify="center")
            tabla_puertos.add_column("Servicio", style="magenta")
            tabla_puertos.add_column("Estado", style="bold", justify="center")

            for puerto, servicio in puertos.items():
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.4)
                resultado = s.connect_ex((target, puerto))
                if resultado == 0:
                    tabla_puertos.add_row(str(puerto), servicio, "[green]ABIERTO 🟢[/green]")
                else:
                    tabla_puertos.add_row(str(puerto), servicio, "[red]Cerrado 🔴[/red]")
                s.close()

            console.print(tabla_puertos)
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()

        elif opcion == "6":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🔍 Inspección de Banner (Banner Grabbing)[/bold cyan]\n[dim]Uso: Conectarse a un puerto abierto para capturar información del software y versiones expuestas.[/dim]", expand=False))
            target_bg = input("Ingresa la IP o dominio (Ej. 127.0.0.1 o scanme.nmap.org): ").strip() or "127.0.0.1"
            port_bg = int(input("Ingresa el puerto a auditar (Ej. 80, 21, 22): ") or "80")
            
            console.print(f"\n[bold yellow]Intentando conectar a {target_bg}:{port_bg} para capturar banner...[/bold yellow]\n")
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2.0)
                s.connect((target_bg, port_bg))
                
                banner = s.recv(1024).decode('utf-8', errors='ignore')
                if banner.strip():
                    console.print(f"[bold green]¡Banner Capturado! 🟢[/bold green]\n{banner}")
                else:
                    console.print("[yellow]El puerto respondió a la conexión TCP, pero no envió datos de bienvenida automáticos.[/yellow]")
                s.close()
            except Exception as e:
                console.print(f"[bold red]No se pudo capturar banner o el puerto está cerrado/filtrado: {e}[/bold red]")
                
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()
            
        elif opcion == "7":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🔍 Resolución de Dominios / IPs[/bold cyan]\n[dim]Uso: Consultar los registros DNS para averiguar la dirección IP detrás de una web.[/dim]", expand=False))
            dominio = input("Ingresa el sitio o dominio (Ej. google.com): ")
            if dominio.strip():
                try:
                    ip_resuelta = socket.gethostbyname(dominio)
                    console.print(f"\n[green]Dominio:[/green] {dominio}")
                    console.print(f"[green]Dirección IP asociada:[/green] [bold cyan]{ip_resuelta}[/bold cyan]")
                except Exception as e:
                    console.print(f"[bold red]No se pudo resolver el dominio: {e}[/bold red]")
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()

        elif opcion == "8":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🔐 Generador de Claves y Entropía[/bold cyan]\n[dim]Uso: Crear contraseñas complejas utilizando aleatoriedad criptográfica segura.[/dim]", expand=False))
            longitud = int(input("Ingresa la longitud de la contraseña (recomendado 16+): ") or "16")
            
            caracteres = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
            
            console.print(f"\n[green]Contraseña Generada:[/green] [bold yellow]{password}[/bold yellow]")
            console.print(f"[cyan]Longitud:[/cyan] {longitud} caracteres")
            console.print("[dim]Nota: Una alta aleatoriedad previene ataques de fuerza bruta basados en patrones.[/dim]")
            
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()

        elif opcion == "9":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🔓 Auditor de Hashes (Fuerza Bruta Interactiva)[/bold cyan]\n[dim]Uso: Pon a prueba tus propias claves secretas contra un diccionario de ataque.[/dim]", expand=False))
            
            clave_usuario = input("Escribí una contraseña secreta para probar (ej. '123456', 'secreto', 'password'): ").strip()
            if not clave_usuario:
                clave_usuario = "123456"
                
            hash_generado = hashlib.md5(clave_usuario.encode()).hexdigest()
            console.print(f"\n[cyan]Contraseña elegida:[/cyan] [yellow]{clave_usuario}[/yellow]")
            console.print(f"[cyan]Hash MD5 generado (lo que vería un atacante en una base de datos robada):[/cyan] [bold magenta]{hash_generado}[/bold magenta]\n")
            
            diccionario = [
                "123456", "password", "admin", "admin123", "root", 
                "muonline", "12345678", "welcome", "secreto", "clave123", 
                "hola123", "dragon", "futbol", "12345", "shadow"
            ]
            
            console.print(f"[bold yellow]Iniciando ataque de diccionario con {len(diccionario)} palabras comunes...[/bold yellow]\n")
            
            encontrado = False
            for palabra in diccionario:
                hash_prueba = hashlib.md5(palabra.encode()).hexdigest()
                if hash_prueba == hash_generado:
                    console.print(f"[bold green]¡CONTRASEÑA DESCIFRADA! 🔓 -> '{palabra}'[/bold green]")
                    console.print("[red]⚠️ Conclusión: Tu clave era demasiado débil y estaba en el diccionario.[/red]")
                    encontrado = True
                    break
            
            if not encontrado:
                console.print(f"[bold green]🛡️ ¡CONTRASEÑA SEGURA! El script no pudo adivinar '{clave_usuario}'.[/bold green]")
                console.print("[cyan]Explicación: Como tu clave no está en el diccionario de palabras comunes, el ataque falló.[/cyan]")
                
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()

        elif opcion == "10":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]🔑 Calculadora Multihash[/bold cyan]\n[dim]Uso: Convierte cualquier texto en sus formatos criptográficos MD5, SHA-256 y SHA-512.[/dim]", expand=False))
            
            texto_ingresado = input("Ingresa el texto o contraseña a transformar: ").strip() or "CentroDeComandos"
            
            h_md5 = hashlib.md5(texto_ingresado.encode()).hexdigest()
            h_sha256 = hashlib.sha256(texto_ingresado.encode()).hexdigest()
            h_sha512 = hashlib.sha512(texto_ingresado.encode()).hexdigest()
            
            console.print(f"\n[green]Texto analizado:[/green] [yellow]{texto_ingresado}[/yellow]\n")
            
            tabla_hash = Table(title="Formatos Hash Generados")
            tabla_hash.add_column("Algoritmo", style="cyan")
            tabla_hash.add_column("Valor Hash Criptográfico", style="magenta")
            
            tabla_hash.add_row("MD5 (32 hex)", h_md5)
            tabla_hash.add_row("SHA-256 (64 hex)", h_sha256)
            tabla_hash.add_row("SHA-512 (128 hex)", h_sha512)
            
            console.print(tabla_hash)
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()

        elif opcion == "11":
            limpiar_pantalla()
            console.print(Panel("[bold cyan]💻 Ejecutor de Comandos Bash[/bold cyan]\n[dim]Uso: Lanzar utilidades directas del sistema operativo desde el script.[/dim]", expand=False))
            cmd = input("Ingresa el comando de Bash a ejecutar: ")
            if cmd.strip():
                os.system(cmd)
            console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
            input()
            
        elif opcion == "0":
            break
            
        elif opcion == "SALIR":
            return "SALIR_TOTAL"
            
        else:
            console.print("[bold red]Opción inválida. Intenta de nuevo.[/bold red]")
            console.print("\n[bold yellow]Presiona Enter para continuar...[/bold yellow]", end="")
            input()

def modulo_multimedia():
    limpiar_pantalla()
    console.print(Panel("[bold magenta]🎬 Módulo Multimedia[/bold magenta]\n[dim]Propósito: Gestión y reproducción de contenido multimedia.[/dim]", expand=False))
    console.print("Herramientas multimedia en desarrollo.")
    console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
    input()

def modulo_pip():
    limpiar_pantalla()
    console.print(Panel("[bold yellow]📦 Gestor de Librerías PIP[/bold yellow]\n[dim]Propósito: Control y listado de paquetes instalados en Python.[/dim]", expand=False))
    res = subprocess.run(["pip", "list"], capture_output=True, text=True)
    console.print(res.stdout[:1000] + "\n... [Listado truncado]")
    console.print("\n[bold yellow]Presiona Enter para volver...[/bold yellow]", end="")
    input()

def modulo_git():
    while True:
        limpiar_pantalla()
        console.print(Panel("[bold blue]☁️ Sincronización Git (PC / Celu)[/bold blue]\n[dim]Propósito: Control de versiones y sincronización de código entre dispositivos.[/dim]", expand=False))
        console.print("[1] 📥 Git Pull (Actualizar desde la nube)")
        console.print("[2] 📤 Git Push (Subir cambios)")
        console.print("[3] 📊 Git Status")
        console.print("[0] ⬅️ Volver al menú principal")
        console.print("[SALIR] 🚪 Cierre total\n")
        
        op = input("Selecciona una opción [1/2/3/0/SALIR]: ").strip().upper()
        if op == "1":
            subprocess.run(["git", "pull"])
            console.print("\n[bold yellow]Presiona Enter para continuar...[/bold yellow]", end="")
            input()
        elif op == "2":
            subprocess.run(["git", "add", "."])
            commit_msg = input("Mensaje del commit (Enter para predeterminado): ") or "Actualización desde Centro de Comandos"
            subprocess.run(["git", "commit", "-m", commit_msg])
            subprocess.run(["git", "push"])
            console.print("\n[bold yellow]Presiona Enter para continuar...[/bold yellow]", end="")
            input()
        elif op == "3":
            subprocess.run(["git", "status"])
            console.print("\n[bold yellow]Presiona Enter para continuar...[/bold yellow]", end="")
            input()
        elif op == "0":
            break
        elif op == "SALIR":
            return "SALIR_TOTAL"

def main():
    while True:
        limpiar_pantalla()
        console.print(Panel("[bold yellow]✨ CENTRO DE COMANDOS MAESTRO ✨[/bold yellow]\n[cyan]Entorno Unificado (PC / Termux)[/cyan]", expand=False))
        
        tabla = Table(title="Menú Principal")
        tabla.add_column("Opción", style="cyan", justify="center")
        tabla.add_column("Módulo Principal", style="green")
        tabla.add_column("Descripción General", style="dim white")
        
        tabla.add_row("1", "📊 Módulo de Sistema", "[1] Estado general y diagnóstico de la computadora o entorno.")
        tabla.add_row("2", "🛡️ Ciberseguridad & Redes", "[2] Herramientas de auditoría, escaneo de red, puertos y criptografía.")
        tabla.add_row("3", "🎬 Módulo Multimedia", "[3] Utilidades y reproducción multimedia.")
        tabla.add_row("4", "📦 Gestor de Librerías PIP", "[4] Administración de dependencias y paquetes de Python.")
        tabla.add_row("5", "☁️ Sincronización Git", "[5] Control de versiones para mantener tu código sincronizado.")
        tabla.add_row("0", "❌ Salir", "[0] Cierra el Centro de Comandos.")
        
        console.print(tabla)
        
        opcion = input("\nSelecciona una opción [1/2/3/4/5/0]: ").strip().upper()
        
        resultado = None
        if opcion == "1":
            modulo_sistema()
        elif opcion == "2":
            resultado = modulo_ciberseguridad()
        elif opcion == "3":
            modulo_multimedia()
        elif opcion == "4":
            modulo_pip()
        elif opcion == "5":
            resultado = modulo_git()
        elif opcion == "0":
            console.print("[bold red]¡Hasta luego, Martín![/bold red]")
            break
        else:
            console.print("[bold red]Opción inválida. Intenta de nuevo.[/bold red]")
            console.print("\n[bold yellow]Presiona Enter para continuar...[/bold yellow]", end="")
            input()
            
        if resultado == "SALIR_TOTAL":
            console.print("[bold red]¡Hasta luego, Martín![/bold red]")
            break

if __name__ == "__main__":
    main()
