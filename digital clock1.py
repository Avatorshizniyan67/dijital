import sys
from tkinter import * 
import time
import calendar
def times ():
 current_time = time.strftime("%H:%M:%S")
 clock.config(text=current_time)
 now = time.localtime()
 current_date = f"{now.tm_year}-{now.tm_mon:02d}-{now.tm_mday:02d}"
 cal.config(text=current_date)
 clock.after(200, times)
 root = Tk()
 root.geometry("500x250")
 clock = Label(root, font=("times", 50, "bold"),bg="white")
 clock.grid(row=2, column=2, pady=25, padx=100)
 cal = Label(root, font=("times", 20, "bold"),bg="white")
 cal.grid(row=3, column=2, pady=10)
 times()
 digi = Label(root, text="Digital Clock", font="times24 bold")
 digi.grid(row=0, column=2)
 nota = Label(root, text="hours minutes seconds", font="times 15 bold")
 nota.grid(row=4, column=2)
 root.mainloop()