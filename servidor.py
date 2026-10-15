import socket

# Configurar el servidor para escuchar en la red local
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 5000))
servidor.listen(1)

print("[*] Esperando conexión en el puerto 5000...")
conexion, addr = servidor.accept()
print(f"[+] Conexión establecida desde {addr}")

# Recibir los datos (el contenido del texto o script)
datos = conexion.recv(1024).decode("utf-8")
print(f"\n[Recibido]:\n{datos}")

conexion.close()
servidor.close()