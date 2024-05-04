import tkinter as tk
from tkinter import messagebox

class gui():
  def __init__(self):
      self.root = tk.Tk()
      self.root.title("Calculator")
      self.root.geometry("800x500")
      self.label = tk.Label(self.root,text="Your calculation")
      self.label.pack(padx=10,pady=10)
      self.calculation = tk.Text(self.root,height=1)
      self.calculation.pack(padx=10,pady=10)
      self.button = tk.Button(self.root,text="enter",command=self.calc)
      self.button.pack(padx=10,pady=10)
      self.answer = tk.Button(self.root, text="ans", command=self.getAns)
      self.answer.pack(padx=10, pady=10)
      self.history = tk.Label(self.root, text="history:")
      self.history.pack(padx=10,pady=10)
      self.root.mainloop()
  def calc(self):
      self.calc = self.calculation.get('1.0',tk.END)
      self.str=""
      for i in self.calc:
        if i == " ":
          continue
        elif i == "+":
          self.value1 = int(self.str)
          self.cm = "+"
          self.str = ""
          continue
        elif i == "*":
          self.value1 = int(self.str)
          self.cm = "*"
          self.str = ""
          continue
        elif i == "-":
          self.value1 = int(self.str)
          self.cm = "-"
          self.str = ""
          continue
        elif i == "/":
          self.value1 = int(self.str)
          self.cm = "/"
          self.str=""
          continue
        self.str+=i
      self.value2 = int(self.str)
      if self.cm == "/":
        messagebox.showinfo(title="result",message=f"{int(self.value1/self.value2)}")
        self.answ = int(self.value1 / self.value2)
      elif self.cm == "*":
        messagebox.showinfo(title="result",message=f"{self.value1*self.value2}")
        self.answ = self.value1 * self.value2
      elif self.cm == "-":
        messagebox.showinfo(title="result",message=f"{self.value1-self.value2}")
        self.answ = self.value1 - self.value2
      elif self.cm == "+":
        messagebox.showinfo(title="result",message=f"{self.value1+self.value2}")
        self.answ = self.value1+self.value2
      self.calculation.delete("1.0",tk.END)
      self.calculation_history = tk.Label(self.root, text=f'{self.value1} {self.cm} {self.value2} = {self.answ}')
      self.calculation_history.pack(padx=10,pady=10)
  def getAns(self):
      self.calculation.insert(tk.END,str(self.answ))

gui()
