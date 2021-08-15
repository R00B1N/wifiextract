#!/usr/bin/env python3

#Creando un script que extraiga todas las contraseñas wifi almacenadas en linux.
#By Blackster. All Rights Reserved 2021.

#importamos los modulos necesarios.
import subprocess
import time
import os

def extraer():
    os.system('clear')
    time.sleep(1)
    print("Extrayendo...")
    ruta = "/etc/NetworkManager/system-connections/"
    subprocess.run("cd {}".format(ruta), shell=True, check=False)
    subprocess.run("sudo cat {}*.nmconnection >> wifi.txt".format(ruta), shell=True, check=False)
    subprocess.run("ls", shell=True, check=False)
    pass

if __name__ == '__main__':
    """ llamamos a nuestra funcion para extraer las contraseñas """
    extraer()
    pass
