import customtkinter as ctk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Cipher Machine')
        self.root.geometry('800x500')

        ctk.set_default_color_theme('dark-blue')
        ctk.set_appearance_mode('dark')

        self.text = ctk.CTkLabel(self.root, text='Enter text:')
        self.entry = ctk.CTkEntry(self.root)
        self.enter = ctk.CTkButton(self.root, text='Enter', command=self.cypher)

        self.text.pack(padx=25, pady=20)
        self.entry.pack(padx=10, pady=10)
        self.enter.pack()

        self.root.protocol('WM_DELETE_WINDOW', self.shut_down)

        self.root.mainloop()

    def cypher(self):
        pass

    def shut_down(self):
        if messagebox.askyesno(title="Quit", message="Do you want to quit?"):
            self.root.destroy()


GUI()