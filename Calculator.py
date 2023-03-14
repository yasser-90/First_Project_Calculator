from datetime import date
import time
import tkinter as tk

Bg_color = "#FFF3E2"
B_color = "#5e8d49"
font ="Helvetica 10"
win = tk.Tk()
win.title('Calculator')
win.iconphoto(False, tk.PhotoImage(file = "./calculator.png"))
win.resizable(False, False) 
win.geometry('%dx%d+%d+%d' %(290,333,600,200))
win.configure(bg = Bg_color)

entry = tk.Entry(win, borderwidth=3,font=font, width=40)
entry.grid(row=1, column=0, columnspan=5, ipady=2, pady=2)
today = date.today()
seconds = time.time()
local_time = time.ctime(seconds)
print("Seconds since epoch =", seconds)  
print("Today's date:", today)


def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
          y = str(eval(entry.get()))
          entry.delete(0, tk.END)
          entry.insert(0, y)
    except:
          entry.delete(0, tk.END)
          entry.insert(0, "ERROR")

def clear():
    entry.delete(0, tk.END)

def delete():
    entry.delete(len(entry.get())-1, tk.END)

B_1 = tk.Button(win, text='1', padx=15,
     pady=5, bg= B_color ,width=3,font=font, command=lambda: myclick(1))
B_1.grid(row=2, column=0, pady=1)
B_2 = tk.Button(win, text='2', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(2))
B_2.grid(row=2, column=1, pady=2)
B_3 = tk.Button(win, text='3', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(3))
B_3.grid(row=2, column=2, pady=2)

B_d= tk.Button(win, text='del', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: delete())
B_d.grid(row=2, column=3, pady=2)

B_4 = tk.Button(win, text='4', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(4))
B_4.grid(row=3, column=0, pady=2)
B_5 = tk.Button(win, text='5', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(5))
B_5.grid(row=3, column=1, pady=2)
B_6 = tk.Button(win, text='6', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(6))
B_6.grid(row=3, column=2, pady=2)

B_c= tk.Button(win, text='(', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick("("))
B_c.grid(row=3, column=3, pady=2)


B_7 = tk.Button(win, text='7', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(7))
B_7.grid(row=4, column=0, pady=2)
B_8 = tk.Button(win, text='8', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(8))
B_8.grid(row=4, column=1, pady=2)
B_9 = tk.Button(win, text='9', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(9))
B_9.grid(row=4, column=2, pady=2)

B_c2= tk.Button(win, text=')', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(")"))
B_c2.grid(row=4, column=3, pady=2)


B_0 = tk.Button(win, text='0', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick(0))
B_0.grid(row=5, column=1, pady=2)

B_power = tk.Button(win, text='x^', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick("**"))
B_power.grid(row=5, column=3, pady=2)

B_add = tk.Button(win, text="+", padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick('+'))
B_add.grid(row=6, column=0, pady=2)

B_subtract = tk.Button(
 win, text="-", padx=15, pady=5,bg= B_color, width=3,font=font, command=lambda: myclick('-'))
B_subtract.grid(row=6, column=1, pady=2)

B_multiply = tk.Button(
 win, text="*", padx=15, pady=5,bg= B_color, width=3,font=font, command=lambda: myclick('*'))
B_multiply.grid(row=6, column=2, pady=2)

B_power2 = tk.Button(win, text='x^2', padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick("**2"))
B_power2.grid(row=6, column=3, pady=2)

B_equal = tk.Button(win, text="=", padx=15,
      pady=5,bg= B_color, width=3,font=font, command=equal)
B_equal.grid(row=7, column=0, columnspan=1, pady=2)

B_div = tk.Button(win, text="/", padx=15,
     pady=5,bg= B_color, width=3,font=font, command=lambda: myclick('/'))
B_div.grid(row=7, column=1, columnspan=1, pady=2)

B_remainder = tk.Button(
 win, text="%", padx=15, pady=5,bg= B_color, width=3,font=font, command=lambda: myclick('%'))
B_remainder.grid(row=7, column=2, columnspan=1, pady=2)

B_clear = tk.Button(win, text="clear",
      padx=15, pady=5,bg= B_color, width=3,font=font, command=clear)
B_clear.grid(row=7, column=3, columnspan=1, pady=3)

frame = tk.Frame(win,width=250,height=90,bg="#78866B")
frame.grid(row=9,column=0, columnspan=6)
l_date=tk.Label(frame,text=f'Date :  {today}',font=font,bg="#78866B")
l_date.grid(row=0, column=0, columnspan=6, pady=3)
l_time=tk.Label(frame,text=f'Time :  {local_time}',font=font,bg="#78866B")
l_time.grid(row=1, column=0, columnspan=6, pady=3)

win.mainloop()