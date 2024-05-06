import customtkinter as ctk

class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Settings')
        self.root.geometry('256x243')

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")

        self.size = ctk.IntVar()
        self.valueOfCheck = ctk.IntVar()

        self.checkbox = ctk.CTkCheckBox(self.root, text='close without question', variable=self.valueOfCheck)
        self.pb = ctk.CTkSlider(self.root, from_=1, to=20, variable=self.size)
        self.label = ctk.CTkLabel(self.root, text='size of font')
        self.button = ctk.CTkButton(self.root, text='Apply', command=self.shut_down())

        self.checkbox.pack(padx=10, pady=10)
        self.label.pack(padx=10, pady=10)
        self.pb.pack()
        self.button.pack(padx=25, pady=50)

        self.root.protocol("WM_DELETE_WINDOW", self.shut_down)
        self.root.mainloop()

    def shut_down(self):
        pass

GUI()