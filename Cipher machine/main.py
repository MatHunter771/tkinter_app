import string
import customtkinter as ctk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Cipher Machine')
        self.root.geometry('800x500')

        ctk.set_default_color_theme('dark-blue')
        ctk.set_appearance_mode('dark')

        self.mainFrame = ctk.CTkFrame(self.root)
        self.buttonsFrame = ctk.CTkFrame(self.root)
        self.historyFrame = ctk.CTkFrame(self.root, height=100)

        self.text = ctk.CTkLabel(self.mainFrame, text='Enter text:')
        self.entry = ctk.CTkEntry(self.mainFrame, width=600)
        self.entry.bind('<KeyPress>', self.shortcut)
        self.t = 1

        self.clear = ctk.CTkButton(self.buttonsFrame, text='Clear Entry', command=self.clearEntry)
        self.clearHistory = ctk.CTkButton(self.buttonsFrame, text='Clear History', command=self.historyClear)

        self.bin = ctk.CTkButton(self.buttonsFrame, text='Bin', command=self.binaryCode)
        self.ceasar = ctk.CTkButton(self.buttonsFrame, text='Ceasar', command=self.cypherCeasar)
        self.hex = ctk.CTkButton(self.buttonsFrame, text='Hex', command=self.hexCode)

        self.deBin = ctk.CTkButton(self.buttonsFrame, text='de-Bin', command=self.deBinaryCode)
        self.deCeasar = ctk.CTkButton(self.buttonsFrame, text='de-Ceasar', command=self.deCypherCeasar)
        self.deHex = ctk.CTkButton(self.buttonsFrame, text='de-Hex', command=self.deHexCode)

        self.history = ctk.CTkLabel(self.historyFrame, text='History:')

        self.mainFrame.pack(padx=25, pady=20)
        self.buttonsFrame.pack(pady=5)
        self.historyFrame.pack()

        self.text.grid(row=0)
        self.entry.grid(row=1)

        self.clear.grid(row=0, column=3, padx=5, pady=5)
        self.clearHistory.grid(row=1, column=3, padx=5, pady=5)
        self.bin.grid(row=0, column=0, padx=5, pady=5)
        self.ceasar.grid(row=0, column=1, padx=5, pady=5)
        self.hex.grid(row=0, column=2, padx=5, pady=5)
        self.deBin.grid(row=1, column=0, padx=5, pady=5)
        self.deCeasar.grid(row=1, column=1, padx=5, pady=5)
        self.deHex.grid(row=1, column=2, padx=5, pady=5)

        self.history.grid()

        self.root.protocol('WM_DELETE_WINDOW', self.shut_down)

        self.root.mainloop()
        
    def historyOut(self, x, p, k, inp, out, methd):
        self.historyElement = ctk.CTkLabel(self.historyFrame, text=f'{inp} -> {out} ({methd})', font=('Arial', 10))
        x += 1
        if x > k:
            x = p
        self.historyElement.grid(row=x, pady=5)

    def historyClear(self):
        self.t = 0
        self.historyFrame.destroy()
        self.historyFrame = ctk.CTkFrame(self.root)
        self.historyFrame.pack()
        self.history = ctk.CTkLabel(self.historyFrame, text='History:')
        self.history.grid()

    def clearEntry(self):
        self.entry.delete(0, ctk.END)
    def cypherCeasar(self):
        signs = list(string.ascii_letters)
        inputSentence = self.entry.get()
        outputSentence = ''

        for i in range(len(inputSentence)):
            p = signs.index(inputSentence[i])
            if p + 3 < len(signs):
                outputSentence += str(signs[p+3])
            else:
                outputSentence += str(signs[p+3-(len(signs)-1)])

        messagebox.showinfo(message=outputSentence, title='Output')
        self.historyOut(self.t, 1, 4, inputSentence, outputSentence, methd='Ceasar')
        self.clearEntry()
        self.output = outputSentence


    def deCypherCeasar(self):
        signs = list(string.ascii_letters)
        inputSentence = self.entry.get()
        outputSentence = ''

        for i in range(len(inputSentence)):
            p = signs.index(inputSentence[i])
            if p - 3 < len(signs):
                outputSentence += str(signs[p - 3])
            else:
                outputSentence += str(signs[p - 3 - (len(signs) - 1)])

        messagebox.showinfo(message=outputSentence, title='Output')
        self.historyOut(self.t, 1, 4, inputSentence, outputSentence, methd='de-Ceasar')
        self.clearEntry()
        self.output = outputSentence


    def binaryCode(self):
        inputString = self.entry.get()
        outputString = ''
        for x in inputString:
            outputString += f'{bin(ord(x))[2:]} '
        messagebox.showinfo(message=outputString, title='Output')
        self.historyOut(self.t, 1, 4, inputString, outputString, methd='Bin')
        self.clearEntry()
        self.output = outputString


    def deBinaryCode(self):
        inputString = self.entry.get()
        outputString = str(int(inputString, 2))
        self.historyOut(self.t, 1, 4, inputString, outputString, methd='de-Bin')
        self.clearEntry()
        self.output = outputString


    def hexCode(self):
        inputString = self.entry.get()
        outputString = ''
        for x in inputString:
            outputString += f'{hex(ord(x))[2:]} '
        messagebox.showinfo(message=outputString, title='Output')
        self.historyOut(self.t, 1, 4, inputString, outputString, methd='Hex')
        self.clearEntry()
        self.output = outputString


    def deHexCode(self):
        inputString = self.entry.get()
        outputString = str(int(inputString, 16))
        self.historyOut(self.t, 1, 4, inputString, outputString, methd='de-Hex')
        self.clearEntry()
        self.output = outputString

    def shortcut(self, event):
        if event.keysym == 'A' and event.state == 5:
            self.clearEntry()
            self.entry.insert(ctk.END, self.output)

    def shut_down(self):
        if messagebox.askyesno(title="Quit", message="Do you want to quit?"):
            self.root.destroy()


GUI()