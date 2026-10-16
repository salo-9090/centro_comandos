import subprocess
import json
import sqlite3
import sys
import os
from datetime import datetime

# Colores ANSI para la terminal
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def inicializar_bd():
    conn = sqlite3.connect('asistencia.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            entrada TEXT,
            salida TEXT,
            total_horas TEXT
        )
    ''')
    conn.commit()
    conn.close()

def exportar_respaldo():
    """Genera un archivo de respaldo en texto con todo el historial"""
    conn = sqlite3.connect('asistencia.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, fecha, entrada, salida, total_horas FROM registros ORDER BY id ASC")
    filas = cursor.fetchall()
    conn.close()

    # Guarda el archivo de respaldo en la carpeta del usuario
    ruta_respaldo = os.path.expanduser("~/parte_diario_respaldo.txt")
    with open(ruta_respaldo, "w", encoding="utf-8") as f:
        f.write("=========================================\n")
        f.write("      REPORTE Y RESPALDO DE ASISTENCIA   \n")
        f.write("=========================================\n\n")
        for row in filas:
            rid, fecha, entrada, salida, total = row
            f.write(f"ID: {rid} | Fecha: {fecha}\n")
            f.write(f"  - Entrada : {entrada}\n")
            f.write(f"  - Salida  : {salida if salida else 'Pendiente'}\n")
            f.write(f"  - Total   : {total if total else 'En curso'}\n")
            f.write("-" * 41 + "\n")

def verificar_huella():
    print(f"\n{AMARILLO}{BOLD}🔒 Autorización requerida:{RESET} Por favor, apoyá tu dedo en el sensor...")
    resultado = subprocess.run(
        ['termux-fingerprint'], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True
    )
    
    if resultado.returncode != 0:
        print(f"{ROJO}❌ Error al invocar el sensor biométrico. Verificá Termux:API.{RESET}")
        return False
        
    try:
        datos = json.loads(resultado.stdout)
        if datos.get("auth_result") == "AUTH_RESULT_SUCCESS":
            print(f"{VERDE}✅ ¡Huella verificada con éxito!{RESET}")
            return True
        else:
            print(f"{ROJO}❌ Huella no reconocida.{RESET}")
            return False
    except json.JSONDecodeError:
        print(f"{ROJO}❌ No se pudo procesar la respuesta del sensor.{RESET}")
        return False

def mostrar_parte_diario():
    conn = sqlite3.connect('asistencia.db')
    cursor = conn.cursor()
    cursor.execute("SELECT fecha, entrada, salida, total_horas FROM registros ORDER BY id DESC LIMIT 5")
    filas = cursor.fetchall()
    conn.close()

    print(f"\n{CYAN}{BOLD}=========================================={RESET}")
    print(f"{CYAN}{BOLD} 📋 PARTE DIARIO Y REGISTRO DE ASISTENCIA{RESET}")
    print(f"{CYAN}{BOLD}=========================================={RESET}")
    for row in filas:
        fecha, entrada, salida, total = row
        salida_txt = salida if salida else f"{AMARILLO}En curso / Pendiente{RESET}"
        total_txt = total if total else f"{MAGENTA}Calculando...{RESET}"
        print(f"{BOLD}📅 Fecha:{RESET} {fecha}")
        print(f"   {VERDE}🟢 Entrada :{RESET} {entrada}")
        print(f"   {ROJO}🔴 Salida  :{RESET} {salida_txt}")
        print(f"   {AZUL}⏱️  Total   :{RESET} {total_txt}")
        print(f"{CYAN}" + "-" * 42 + f"{RESET}")
    
    print(f"{MAGENTA}📁 Archivo de respaldo actualizado: ~/parte_diario_respaldo.txt{RESET}")

def gestionar_fichaje(accion):
    inicializar_bd()
    ahora = datetime.now()
    fecha_hoy = ahora.strftime("%Y-%m-%d")
    hora_actual = ahora.strftime("%H:%M:%S")

    conn = sqlite3.connect('asistencia.db')
    cursor = conn.cursor()

    if accion == "entrada":
        cursor.execute("SELECT id FROM registros WHERE fecha = ? AND salida IS NULL", (fecha_hoy,))
        if cursor.fetchone():
            print(f"\n{AMARILLO}⚠️ Ya tenés una entrada registrada hoy sin cerrar. ¡Fichá tu salida primero!{RESET}")
            conn.close()
            return

        if not verificar_huella():
            conn.close()
            return

        cursor.execute("INSERT INTO registros (fecha, entrada, salida, total_horas) VALUES (?, ?, NULL, NULL)", (fecha_hoy, hora_actual))
        conn.commit()
        print(f"\n{VERDE}[ENTRADA REGISTRADA]{RESET} Fecha: {fecha_hoy} | Hora: {hora_actual}")

    elif accion == "salida":
        cursor.execute("SELECT id, entrada FROM registros WHERE fecha = ? AND salida IS NULL", (fecha_hoy,))
        registro_abierto = cursor.fetchone()

        if not registro_abierto:
            print(f"\n{AMARILLO}⚠️ No se encontró una entrada abierta para el día de hoy.{RESET}")
            conn.close()
            return

        if not verificar_huella():
            conn.close()
            return

        reg_id, hora_entrada_str = registro_abierto
        
        # Cálculo exacto con horas, minutos y segundos
        formato = "%H:%M:%S"
        t_entrada = datetime.strptime(hora_entrada_str, formato)
        t_salida = datetime.strptime(hora_actual, formato)
        
        diferencia = t_salida - t_entrada
        total_segundos = diferencia.seconds
        
        horas = total_segundos // 3600
        minutos = (total_segundos % 3600) // 60
        segundos = total_segundos % 60
        
        total_str = f"{horas}h {minutos}m {segundos}s"
        
        cursor.execute("""
            UPDATE registros 
            SET salida = ?, total_horas = ? 
            WHERE id = ?
        """, (hora_actual, total_str, reg_id))
        conn.commit()
        
        print(f"\n{ROJO}[SALIDA REGISTRADA]{RESET} Hora: {hora_actual}")
        print(f"{AZUL}⏱️ Tiempo total trabajado hoy: {total_str}{RESET}")

    conn.close()
    exportar_respaldo()
    mostrar_parte_diario()

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ["entrada", "salida"]:
        print(f"\n{AMARILLO}📌 Uso incorrecto. Comandos disponibles:{RESET}")
        print("   fichar entrada")
        print("   fichar salida")
    else:
        gestionar_fichaje(sys.argv[1])

