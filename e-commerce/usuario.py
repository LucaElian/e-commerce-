from imports_app import *

class Usuario(ctk.CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        x = (self.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.winfo_screenheight() // 2) - (600 // 2)
        self.geometry(f"500x600+{x}+{y}")
        self.title("usuario")
        self.iniciar_widgets()

    def iniciar_widgets(self):
        self.opciones = ctk.CTkFrame(self, height=600, width=200,  
                                    fg_color=("#FFFFFF","#0D0D0D"), 
                                    border_width=2, border_color=("#FF3936","#670010"))
        self.opciones.place(relx=0, rely=0)

        self.informacion_usuario = ctk.CTkButton(self.opciones, text="MI CUENTA", fg_color=("#FFFFFF","#0D0D0D"), text_color="#FFFFFF",font=("Ferret Face", 25), corner_radius=30,  hover_color="#424242")
        self.informacion_usuario.place(relx= 0.50, rely= 0.07, anchor="center")

        self.juegos_usuario = ctk.CTkButton(self.opciones, text="MIS JUEGOS", fg_color=("#FFFFFF","#0D0D0D"), text_color="#FFFFFF", font=("Ferret Face", 25), corner_radius=30,  hover_color="#424242")
        self.juegos_usuario.place(relx= 0.50, rely= 0.14, anchor="center")

        self.favoritos_usuario = ctk.CTkButton(self.opciones, text="FAVORITOS", fg_color=("#FFFFFF","#0D0D0D"), text_color="#FFFFFF",font=("Ferret Face", 25), corner_radius=30,  hover_color="#424242")
        self.favoritos_usuario.place(relx= 0.50, rely= 0.21, anchor="center")

        self.apariencia_usuario = ctk.CTkButton(self.opciones, text="APARIENCIA", fg_color=("#FFFFFF","#0D0D0D"), text_color="#FFFFFF",font=("Ferret Face", 25), corner_radius=30,  hover_color="#424242")
        self.apariencia_usuario.place(relx= 0.50, rely= 0.28, anchor="center")

        self.administrar_cuenta_usuario = ctk.CTkButton(self.opciones, text="ADMINISTRA\nCUENTA", fg_color=("#FFFFFF","#0D0D0D"), text_color="#FFFFFF",font=("Ferret Face", 25), corner_radius=30,  hover_color="#424242")
        self.administrar_cuenta_usuario.place(relx= 0.50, rely= 0.35, anchor="center")
