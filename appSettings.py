import customtkinter as ctk

class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Settings')
        self.root.geometry('256x243')
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.valueOfCheck = ctk.IntVar()
        self.checkbox = ctk.CTkCheckBox(self.root, text='close without question', variable=self.valueOfCheck)
        self.checkbox.pack()
        self.size = ctk.IntVar()
        self.pb = ctk.CTkSlider(self.root, from_=1, to=20, variable=self.size)
        self.pb.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.shut_down)
        self.root.mainloop()
    def shut_down(self):
        self.root.destroy()


GUI()