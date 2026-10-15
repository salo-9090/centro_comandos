import os
import importlib.util
def verificar(nombre):
    return importlib.util.find_spec(nombre) is not None

from rich import print
from rich.panel import Panel

def ejecutar():
    while True:
        os.system("clear")
        print(Panel("[bold green]📦 GESTOR INTELIGENTE DE LIBRERÍAS[/bold green]", border_style="green"))
        
        # Verificamos estado actual
        s_rich = "✅ Instalada" if verificar("rich") else "❌ Falta"
        s_req = "✅ Instalada" if verificar("requests") else "❌ Falta"
        s_bs4 = "✅ Instalada" if verificar("bs4") else "❌ Falta"
        s_pil = "✅ Instalada" if verificar("PIL") else "❌ Falta"

        print(f"1. [rich] ({s_rich}) -> Diseños pro, paneles y tablas en consola")
        print(f"2. [requests] ({s_req}) -> Conectarse a APIs y descargar páginas web")
        print(f"3. [beautifulsoup4] ({s_bs4}) -> Web scraping y extraer datos de internet")
        print(f"4. [pillow] ({s_pil}) -> Procesar, recortar y editar imágenes")
        print("5. Ver listado completo de pip list")
        print("6. Volver al menú principal")
        print("-" * 50)
        
        op = input("Elige una opción para instalar/consultar (1-6): ").strip()
        
        if op == "1":
            os.system("pip install rich")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            os.system("pip install requests")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            os.system("pip install beautifulsoup4")
            input("\nPresiona Enter para continuar...")
        elif op == "4":
            os.system("pip install pillow")
            input("\nPresiona Enter para continuar...")
        elif op == "5":
            os.system("pip list")
            input("\nPresiona Enter para continuar...")
        elif op == "6":
            break
