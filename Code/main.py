import os
import platform
import subprocess
import uuid


my_system = platform.uname()


print(f"System: {my_system.system}")
print(f"Release: {my_system.release}")
print(f"Node Name: {my_system.node}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")

def get_hdd_serial():
 result = subprocess.run(
  ['powershell', '-Command',
  'Get-WmiObject win32_diskdrive | Select-Object -ExpandProperty SerialNumber'],
  capture_output=True, text=True)
 output = result.stdout.strip().split('\n')
 if len(output) > 0: return output[0].strip()
 else: return "Серийный номер не найден!"

print("Серийный номер жёсткого диска:", get_hdd_serial())

def get_mac_address():
 mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
 return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

print("MAC-адрес сетевой карты:", get_mac_address())

def get_cpu_id():
 result = subprocess.run(
  ['powershell',
  'Get-WmiObject Win32_Processor | Select-Object -ExpandProperty ProcessorId'],
  capture_output=True, text=True)
 return result.stdout.strip()

print("Серийный номер процессора:", get_cpu_id())

print("\nНажмите любую клавишу для продолжения...")
os.system("pause > nul" if os.name == "nt" else "read > /dev/null")