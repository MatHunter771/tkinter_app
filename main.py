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
      self.root.mainloop()
  def calc(self):
      self.calc = self.calculation.get('1.0',tk.END)
      str=""
      for i in self.calc:
        if i == " ":
          continue
        elif i == "+":
          value1 = int(str)
          cm = "+"
          str = ""
          continue
        elif i == "*":
          value1 = int(str)
          cm = "*"
          str = ""
          continue
        elif i == "-":
          value1 = int(str)
          cm = "-"
          str = ""
          continue
        elif i == "/":
          value1 = int(str)
          cm = "/"
          str=""
          continue
        str+=i
      value2 = int(str)
      if cm == "/":
        messagebox.showinfo(title="result",message=f"{value1/value2}")
      elif cm == "*":
        messagebox.showinfo(title="result",message=f"{value1*value2}")
      elif cm == "-":
        messagebox.showinfo(title="result",message=f"{value1-value2}")
      elif cm == "+":
        messagebox.showinfo(title="result",message=f"{value1+value2}")
  def getAns(self):
      pass

gui()
