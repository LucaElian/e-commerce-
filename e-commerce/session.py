from imports_app import *

class Session:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def cargar_sesion(self):
        with open("user_data.json", "r+") as f:
            data = json.load(f)
            return data["usuario"]["username"], data["usuario"]["password"] 

    def agregar_sesion(self):
        if not path.exists("user_data.json"):
            with open('user_data.json', 'w') as f:
                json.dump({}, f)

        with open("user_data.json", "r+") as f:
            contenido_archivo = json.load(f)
            contenido_archivo["usuario"] = {"username":self.user, "password": self.password}
            f.seek(0)
            json.dump(contenido_archivo, f, indent=4)
            f.truncate()