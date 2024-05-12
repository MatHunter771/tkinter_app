import customtkinter as ctk
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.saved = 0
        self.root = ctk.CTk()
        self.root.title('Settings')
        self.root.geometry('256x243')

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")

        self.size = ctk.IntVar()
        self.valueOfCheck = ctk.IntVar()

        self.checkbox = ctk.CTkCheckBox(self.root, text='close without question', variable=self.valueOfCheck)
        self.pb = ctk.CTkSlider(self.root, from_=8, to=36, variable=self.size)
        self.label = ctk.CTkLabel(self.root, text='size of font')
        self.button = ctk.CTkButton(self.root, text='Apply', command=self.save)

        self.checkbox.pack(padx=10, pady=10)
        self.label.pack(padx=10, pady=10)
        self.pb.pack()
        self.button.pack(padx=25, pady=50)

        self.root.protocol("WM_DELETE_WINDOW", self.shut_down)
        self.root.mainloop()

    def shut_down(self):
        if self.saved:
            self.root.destroy()
        elif messagebox.askyesno(title='save?', message="Are you want to leave setting?"):
            self.root.destroy()

    def save(self):
        pd = open("calculatorSettings0001", "w")
        pd.write(f'sizeFont: {self.size.get()}\ncheck: {self.valueOfCheck.get()}')
        pd.close()
        self.saved = 1

GUI()