from imports_app import *
import crear_base_datos

class Tienda(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.configure(width=1250, height=400, fg_color="transparent")
        self.values = crear_base_datos.datos_videojuegos_consulta()

        self.dos = False

        for i, value in enumerate(self.values):
            self.contenedor_juego = ctk.CTkFrame(self, height=350, width=230, corner_radius=30, border_width=3, border_color=("#FF3936","#670010"))
            
            self.col = i % 4
            self.row = i // 4

            self.contenedor_juego.grid(row=self.row, column=self.col, padx=40, pady=40, sticky="w")

            self.precio_juego_label = ctk.CTkLabel(self.contenedor_juego, text=f"{value[3]} $", fg_color="transparent", text_color=("#000000","#FFFFFF"), width=0, font=("Proxima Soft", 20), corner_radius=10)
            self.precio_juego_label.place(relx=0.2, rely=0.65, anchor="center")

            self.nombre = ctk.CTkLabel(self.contenedor_juego, text=value[0], width=200, corner_radius=10, fg_color=("#FF3936","#670010"), font=("Proxima Soft", 13))
            self.nombre.place(relx=0.5, rely= 0.75, anchor="center")

            self.añadir_juego = ctk.CTkButton(self.contenedor_juego, text="AÑADIR", text_color=("#000000","#FFFFFF"), width=150, corner_radius=10, fg_color="transparent", border_color=("#FF3936","#670010"), border_width=2, hover_color=("#FF7673","#4A0010"), font=("Proxima Soft", 15), cursor="hand2")
            self.añadir_juego.place(relx=0.61, rely= 0.89, anchor="center")

            self.estrella1_img = ctk.CTkImage(light_image=Image.open("./imagenes/estrella_sin_blanco.png"), dark_image=(Image.open("./imagenes/estrella_sin_negro.png")), size=(27, 25))
            self.estrella1_juego = ctk.CTkButton(self.contenedor_juego, text="", image=self.estrella1_img, width=0, fg_color="transparent", cursor="hand2", hover="disable", command=lambda: self.estrella_favorito())
            
            self.estrella2_img = ctk.CTkImage(light_image=Image.open("./imagenes/estrella_con_blanco.png"), dark_image=(Image.open("./imagenes/estrella_con_negro.png")), size=(27, 25))
            self.estrella2_juego = ctk.CTkButton(self.contenedor_juego, text="", image=self.estrella2_img, width=0, fg_color="transparent", cursor="hand2", hover="disable", command=lambda: self.estrella_favorito())
            
            self.estrella1_juego.place(relx=0.12, rely= 0.88, anchor="center")


            self.pc_icon_img = ctk.CTkImage(light_image=Image.open("./imagenes/plataformas/pc_blanco.png"), dark_image=Image.open("./imagenes/plataformas/pc_negro.png"), size=(15,15))
            self.pc_icon = ctk.CTkLabel(self.contenedor_juego, text="", fg_color="transparent", image=self.pc_icon_img, width=0)
            self.pc_icon.place(relx=0.49, rely= 0.65, anchor="center")
            
            self.nintendo_icon_img = ctk.CTkImage(light_image=Image.open("./imagenes/plataformas/nintendo_blanco.png"), dark_image=Image.open("./imagenes/plataformas/nintendo_negro.png"), size=(15,15))
            self.nintendo_icon = ctk.CTkLabel(self.contenedor_juego, text="", fg_color="transparent", image=self.nintendo_icon_img, width=0)
            self.nintendo_icon.place(relx=0.61, rely= 0.65, anchor="center")
            
            self.xbox_icon_img = ctk.CTkImage(light_image=Image.open("./imagenes/plataformas/xbox_blanco.png"), dark_image=Image.open("./imagenes/plataformas/xbox_negro.png"), size=(15,15))
            self.xbox_icon = ctk.CTkLabel(self.contenedor_juego, text="", fg_color="transparent", image=self.xbox_icon_img, width=0)
            self.xbox_icon.place(relx=0.73, rely= 0.65, anchor="center")
            
            self.psn_icon_img = ctk.CTkImage(light_image=Image.open("./imagenes/plataformas/psn_blanco.png"), dark_image=Image.open("./imagenes/plataformas/psn_negro.png"), size=(15,15))
            self.psn_icon = ctk.CTkLabel(self.contenedor_juego, text="", fg_color="transparent", image=self.psn_icon_img, width=0)
            self.psn_icon.place(relx=0.85, rely= 0.65, anchor="center")


    def estrella_favorito(self):
        if self.estrella1_juego.winfo_ismapped():
            self.estrella1_juego.place_forget()
            self.estrella2_juego.place(relx=0.12, rely=0.88, anchor="center")
        else:
            self.estrella2_juego.place_forget()
            self.estrella1_juego.place(relx=0.12, rely=0.88, anchor="center")
