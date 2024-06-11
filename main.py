import os
import pyautogui
import schedule
import time
import datetime
import socket
import psutil
from PIL import Image

# Función para obtener la IP
def get_ip():
    return socket.gethostbyname(socket.gethostname())

# Función para obtener el nombre del equipo
def get_computer_name():
    return socket.gethostname()

# Función para obtener la lista de procesos en ejecución
def get_running_processes():
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        processes.append(f"PID: {process.info['pid']}, Name: {process.info['name']}")
    return processes

# Función para tomar la captura de todas las pantallas y guardar la información en un archivo de texto
def take_screenshot():
    # Obtener el timestamp actual
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f'screenshot_{timestamp}.png'

    # Tomar la captura de todas las pantallas
    screens = pyautogui.screenshot()
    screens.save(screenshot_path)

    # Obtener la IP
    ip = get_ip()

    # Guardar la información en un archivo de texto
    with open('info.txt', 'a') as f:
        f.write(f"{timestamp}, IP: {ip}\n")

    # Obtener el nombre del equipo
    computer_name = get_computer_name()

    # Obtener la lista de procesos en ejecución
    processes = get_running_processes()

    # Guardar la información de los procesos y el nombre del equipo en un archivo de texto, sobrescribiendo el contenido anterior
    with open('processes.txt', 'w') as f:
        f.write(f"{timestamp}, Computer Name: {computer_name}\n")
        f.write("\n".join(processes))
        f.write("\n\n")

    print(f"Screenshot guardada: {screenshot_path}, IP: {ip}, Computer Name: {computer_name}")

# Programar la tarea para que se ejecute cada minuto
schedule.every(1).minute.do(take_screenshot)

# Mantener el script en ejecución
while True:
    schedule.run_pending()
    time.sleep(1)
