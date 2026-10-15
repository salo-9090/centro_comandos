import socket

# IP de la PC (127.0.0.1 si es en la misma máquina, o la IP local si es desde el celu)
IP_PC = "127.0.0.1"
PUERTO = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_PC, PUERTO))

# Pedir el texto por pantalla en el momento
mensaje = input("Escribí el mensaje que querés enviar: ")
cliente.send(mensaje.encode("utf-8"))

print("[+] Mensaje enviado exitosamente.")
cliente.close()