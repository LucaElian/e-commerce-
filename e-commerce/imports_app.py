from os import path
import sqlite3
import subprocess
import json

try:
    from PIL import Image
except ImportError:
    subprocess.call(["pip", "install", "pillow"])

try:
    import customtkinter as ctk
except ImportError:
    subprocess.call(["pip", "install", "customtkinter"])

# Clases
from tienda_principal import Tienda
from usuario import Usuario
#from users_file.session import Session
import crear_base_datos

