from imports_app import *
import crear_base_datos

class Tienda(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.configure(width=1250, height=400, fg_color="transparent")
        self.values = crear_base_datos.datos_videojuegos_consulta()

        self.dos = 2

        for i, value in enumerate(self.values):
            self.contenedor_juego = ctk.CTkFrame(self, height=350, width=230, corner_radius=30, border_width=3, border_color=("#FF3936","#670010"))
            
            self.col = i % 4
            self.row = i // 4

            self.contenedor_juego.grid(row=self.row, column=self.col, padx=40, pady=40, sticky="w")

            self.precio_juego_label = ctk.CTkLabel(self.contenedor_juego, text=f"{value[3]} $", fg_color="transparent", text_color=("#000000","#FFFFFF"), width=0, font=("Roboto", 20), corner_radius=10)
            self.precio_juego_label.place(relx=0.2, rely=0.65, anchor="center")

            self.nombre = ctk.CTkLabel(self.contenedor_juego, text=value[0], width=200, corner_radius=10, fg_color=("#FF3936","#670010"), font=("Proxima Soft", 15))
            self.nombre.place(relx=0.5, rely= 0.75, anchor="center")

            self.añadir_juego = ctk.CTkButton(self.contenedor_juego, text="AÑADIR", width=150, corner_radius=10, fg_color="transparent", border_color=("#FF3936","#670010"), border_width=2, hover_color=("#FF7673","#4A0010"), font=("Proxima Soft", 15), cursor="hand2")
            self.añadir_juego.place(relx=0.61, rely= 0.89, anchor="center")

            self.estrella1_img = ctk.CTkImage(Image.open("./imagenes/estrella_sin.png"), size=(27, 25))
            self.estrella2_img = ctk.CTkImage(Image.open("./imagenes/estrella_sin.png"), size=(23, 25))
            self.estrella_juego = ctk.CTkButton(self.contenedor_juego, text="", image=self.estrella1_img, width=0, fg_color="transparent", cursor="hand2", hover="disable", command=lambda: self.estrella_favorito())
            self.estrella_juego.place(relx=0.12, rely= 0.88, anchor="center")

    def estrella_favorito(self):
        if self.dos == 2:
                self.estrella_juego.configure(image=self.estrella2_img)
        else:
            self.estrella_juego.configure(image=self.estrella1_img)
