from imports_app import *

ctk.set_appearance_mode("dark")
cantidad_carrito = 0

with open("baseDatos.txt", "r") as file:
    query = file.readlines()

# with sqlite3.connect("tienda_videojuegos.db") as conn:
#    conn.execute(query)

class Juegos(ctk.CTk):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        x = (self.winfo_screenwidth() // 2) - (1300 // 2)
        y = (self.winfo_screenheight() // 2) - (700 // 2)
        self.geometry(f"1300x640+{x}+{y}")
        self.title("NEXOGAMES")
        self.iniciar_widgets()
        self.usuario_top_level = None
    
    def iniciar_widgets(self):
        header2 = ctk.CTkFrame(self, height=40, width=600, corner_radius=10, fg_color=("#FFFFFF","#0D0D0D"), border_width=2, border_color=("#FF3936","#670010"))
        header2.place(relx=0.5, rely=0.12, anchor="center")

        header1 = ctk.CTkFrame(self, height=70, width=1300, corner_radius=0, fg_color=("#FFFFFF","#0D0D0D"))
        header1.place(relx=0.5, rely=0.05, anchor="center")

        logo_img = ctk.CTkImage(Image.open("./imagenes/logo.png"), size=(70,80))
        logo_label = ctk.CTkButton(header1, fg_color="transparent", 
                                   image=logo_img, text="NEXOGAMES", 
                                   width=100, height=0, hover="disable", 
                                   font=("Ferret Face", 30), text_color=("#FF3936","#670010"),
                                   cursor="hand2")
        logo_label.place(relx=0.1, rely=0.5, anchor="center")

        barra_de_busqueda = ctk.CTkEntry(header1, border_color=("#FF3936","#670010"), text_color=("#000000","#FFFFFF"), fg_color=("#BFBFBF","#2B2B2B"), corner_radius=30, height=35, width=500)
        barra_de_busqueda.place(relx=0.5, rely=0.5, anchor="center")

        foto_user_img = ctk.CTkImage(light_image=Image.open("./imagenes/user_blanco.png"), dark_image=Image.open("./imagenes/user_negro.png"), size=(32,30))
        foto_user = ctk.CTkButton(header1, fg_color=("#FFFFFF","#0D0D0D"), 
                                text_color=("#000000","#FFFFFF"), 
                                image=foto_user_img, text="INICIAR SESIÓN", 
                                corner_radius=10, border_width=2, border_spacing=0, 
                                border_color=("#FF3936","#670010"), width=0, 
                                hover_color=("#FF7673","#4A0010"), font=("Roboto", 12), 
                                cursor="hand2",command=lambda: abrir_usuarios(self))
        foto_user.place(relx=0.94, rely=0.5, anchor="center")

        carrito_img = ctk.CTkImage(light_image=Image.open("./imagenes/carrito_blanco.png"), dark_image=Image.open("./imagenes/carrito_negro.png"), size=(40,35))
        carrito = ctk.CTkButton(header1, image=carrito_img, fg_color="transparent", width=0, hover="disable", text="", cursor="hand2")
        carrito.place(relx=0.79, rely=0.5, anchor="center")

        texto_carrito = ctk.CTkLabel(carrito, text=cantidad_carrito, fg_color=("#0D0D0D","#FFFFFF"), text_color=("#FFFFFF","#000000"), width=0, height=0, font=("Roboto", 9))
        texto_carrito.place(relx=0.7053 if int(texto_carrito.cget("text")) <= 10 else 0.70536, rely=0.29, anchor="center")
        
        # Opciones botones
        destacados_boton = ctk.CTkButton(header2, text="JUEGOS DESTACADOS", fg_color="transparent", text_color="#FFFFFF", corner_radius=30,  hover_color="#424242")
        destacados_boton.place(relx=0.18, rely=0.5, anchor="center")
        
        categorias_boton = ctk.CTkButton(header2, text="CATEGORIAS", fg_color="transparent", text_color="#FFFFFF", corner_radius=30, hover_color="#424242")
        categorias_boton.place(relx=0.42, rely=0.5, anchor="center")

        promos_ofertas_boton = ctk.CTkButton(header2, text="PROMOS/OFERTAS", fg_color="transparent", text_color="#FFFFFF", corner_radius=30,  hover_color="#424242")
        promos_ofertas_boton.place(relx=0.65, rely=0.5, anchor="center")

        consolas_boton = ctk.CTkButton(header2, text="CONSOLAS", fg_color="transparent", text_color="#FFFFFF", corner_radius=30,  hover_color="#424242")
        consolas_boton.place(relx=0.87, rely=0.5, anchor="center")

        # tienda_principal = Tienda()
        # tienda_principal.iniciar_widgets(juegos.root)

        def abrir_usuarios(self):
            if self.usuario_top_level is None or not self.usuario_top_level.winfo_exists():
                self.usuario_top_level = Usuario(self) 
            else:
                self.usuario_top_level.focus()

if __name__ == "__main__":
    juegos = Juegos()
    juegos.mainloop()
