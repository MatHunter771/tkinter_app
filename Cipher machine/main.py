import customtkinter as ctk

class GUI():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Cipher Machine')
        self.root.geometry('800x500')

        ctk.set_default_color_theme('dark-blue')
        ctk.set_appearance_mode('dark')

        self.root.mainloop()

GUI()