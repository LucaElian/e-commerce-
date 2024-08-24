from imports_app import *

class Usuario(ctk.CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        x = (self.winfo_screenwidth() // 2) - (474 // 2)
        y = (self.winfo_screenheight() // 2) - (606 // 2)
        self.geometry(f"474x606+{x}+{y}") #
        self.title("LOGIN")
        self.iniciar_widgets()

    def iniciar_widgets(self):
        self.uno = 1
        self.opciones_usuario = ctk.CTkFrame(self, width=413, height=535,
                                    fg_color=("#FFFFFF","#0D0D0D"), 
                                    border_width=2, border_color=("#FF3936","#670010"))
        self.opciones_usuario.place(relx=0.5, rely=0.5, anchor="center")

        self.login_usuario = ctk.CTkButton(self.opciones_usuario, text="LOGIN", text_color=("#000000","#FFFFFF"), font=("Proxima Soft", 25), fg_color="transparent", border_color=("#FF3936","#670010"), border_width=3, width=0, corner_radius=12, hover="disable", cursor="hand2", state="disabled", command=lambda: self.cambiar())
        self.login_usuario.place(relx=0.25, rely=0.1, anchor="center")

        self.register_usuario = ctk.CTkButton(self.opciones_usuario, text="REGISTER", text_color=("#000000","#FFFFFF"), font=("Proxima Soft", 25), fg_color="transparent", width=0, corner_radius=12, hover="disable", cursor="hand2", command=lambda: self.cambiar())
        self.register_usuario.place(relx=0.74, rely=0.1, anchor="center")

        foto_user_img = ctk.CTkImage(light_image=Image.open("./imagenes/user_blanco.png"), dark_image=Image.open("./imagenes/user_negro.png"), size=(155,150))
        self.imagen_usuario = ctk.CTkLabel(self.opciones_usuario, image=foto_user_img, text="")
        self.imagen_usuario.place(relx=0.5, rely=0.3, anchor="center")

        self.name_usuario = ctk.CTkLabel(self.opciones_usuario, text="NAME", text_color=("#000000","#FFFFFF"), font=("Proxima Soft", 12), fg_color="transparent", width=0)
        self.name_entry = ctk.CTkEntry(self.opciones_usuario, border_color=("#FF3936","#670010"), text_color=("#000000","#FFFFFF"), fg_color=("#BFBFBF","#2B2B2B"), corner_radius=30, height=35, width=300, font=("Proxima Soft", 15))

        self.username_usuario = ctk.CTkLabel(self.opciones_usuario, text="USERNAME", text_color=("#000000","#FFFFFF"), font=("Proxima Soft", 12), fg_color="transparent", width=0)
        self.username_entry = ctk.CTkEntry(self.opciones_usuario, border_color=("#FF3936","#670010"), text_color=("#000000","#FFFFFF"), fg_color=("#BFBFBF","#2B2B2B"), corner_radius=30, height=35, width=300, font=("Proxima Soft", 15)) 

        self.password_usuario = ctk.CTkLabel(self.opciones_usuario, text="PASSWORD", text_color=("#000000","#FFFFFF"), font=("Proxima Soft", 12), fg_color="transparent", width=0)
        self.password_entry = ctk.CTkEntry(self.opciones_usuario, border_color=("#FF3936","#670010"), text_color=("#000000","#FFFFFF"), fg_color=("#BFBFBF","#2B2B2B"), corner_radius=30, height=35, width=300, font=("Proxima Soft", 15))
        self.forget_password = ctk.CTkButton(self.opciones_usuario, text="Forgot password?", text_color=("#000000","#FFFFFF"), font=("Proxima Soft", 12), fg_color="transparent", width=0, hover="disable", cursor="hand2")

        self.enter_usuario = ctk.CTkButton(self.opciones_usuario, border_width=2, fg_color="transparent", border_color=("#FF3936","#670010"), hover_color=("#FF7673","#4A0010"), font=("Proxima Soft", 12), corner_radius=30, height=35, width=300, text="LOGIN", cursor="hand2")

        self.login_configs()


    def cambiar(self):
        if self.uno == 1: #REGISTER ACTIVADO
            self.login_usuario.configure(border_width=0, state="normal")
            self.register_usuario.configure(border_color=("#FF3936","#670010"), border_width=3, state="disabled")
            self.enter_usuario.configure(text="REGISTER")
            self.register_configs()
            self.uno = 0

        else: #LOGIN ACTIVADO
            self.register_usuario.configure(border_width=0, state="normal")
            self.login_usuario.configure(border_color=("#FF3936","#670010"), border_width=3, state="disabled")
            self.enter_usuario.configure(text="LOGIN")
            self.login_configs()
            self.uno = 1

    def login_configs(self):
            if self.uno == 0:
                self.name_usuario.place_forget()
                self.name_entry.place_forget()
                self.name_entry.delete(0, "end")
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.username_usuario.place(relx=0.25, rely=0.5, anchor="center")
            self.username_entry.place(relx=0.5, rely=0.56, anchor="center") 
            self.password_usuario.place(relx=0.25, rely=0.63, anchor="center") 
            self.password_entry.place(relx=0.5, rely=0.69, anchor="center") 
            self.forget_password.place(relx=0.73, rely=0.75, anchor="center")
            self.enter_usuario.place(relx=0.5, rely=0.85, anchor="center")

    def register_configs(self):
            self.forget_password.place_forget()
            self.name_entry.delete(0, "end")
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.name_usuario.place(relx=0.21, rely=0.5, anchor="center")
            self.name_entry.place(relx=0.5, rely=0.56, anchor="center") 
            self.username_usuario.place(relx=0.246, rely=0.63, anchor="center")
            self.username_entry.place(relx=0.5, rely=0.69, anchor="center") 
            self.password_usuario.place(relx=0.25, rely=0.76, anchor="center") 
            self.password_entry.place(relx=0.5, rely=0.82, anchor="center") 
            self.enter_usuario.place(relx=0.5, rely=0.92, anchor="center")