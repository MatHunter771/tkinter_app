import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Plot')
        self.root.geometry('200x100')

        self.label = tk.Label(self.root, text='formula of function:')
        self.entry = tk.Entry(self.root)
        self.entry.bind("<KeyPress>", self.shortcut)
        self.button = tk.Button(self.root, text='enter', command=self.plot)

        self.label.pack(padx=10, pady=10)
        self.entry.pack(padx=10, pady=10)
        self.button.pack()

        self.root.mainloop()

    def plot(self):
        self.equality = self.entry.get()
        self.str = ''
        for x in self.equality:
            if ' ' == x:
                continue
            elif 'x' == x:
                self.slope = float(self.str)
                self.str = ''
                continue
            self.str += x
        self.intercept = float(self.str)
        self.xAxis = np.array([0, 100])
        def func(x):
            return self.slope * x + self.intercept
        self.model = list(map(func, self.xAxis))
        plt.plot(self.xAxis, self.model)
        plt.grid()
        plt.show()

    def shortcut(self, event):
        if event.state == 0 and event.keysym == 'Return':
            self.plot()


GUI()