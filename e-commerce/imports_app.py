from os import system, path
import sqlite3
import subprocess

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

