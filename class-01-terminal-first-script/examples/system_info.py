import os
import platform
import shutil

print("System:", platform.system())
print("Release:", platform.release())
print("Machine:", platform.machine())
print("Python:", platform.python_version())
print("Current folder:", os.getcwd())

total, used, free = shutil.disk_usage(".")
print("Disk total GB:", round(total / (1024 ** 3), 2))
print("Disk free GB:", round(free / (1024 ** 3), 2))
