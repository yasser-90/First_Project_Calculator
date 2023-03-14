# here  call the library (tool kit interface) that help us to make GUI 
from tkinter import *

# here  call the library just to get circle button
from tkmacosx import CircleButton

# this import (regular expressions) help us in string things  match.. find.. search
import re

# here we create window or form as you want
Calculato_Window = Tk()

# here we give the window title the name that shows up of window
Calculato_Window.title("Calculator")

# here determine window size (width = 400 , height = 500  , X = 400  , Y = 100)
Calculato_Window.geometry("400x600+400+40")

# here we disable or hide the window defualt buttons   (exit , minmize , maximize)
Calculato_Window.attributes('-toolwindow', True)

# here we disable sizableity of window 
Calculato_Window.resizable(False,FALSE)

# here we make the enter or input box
result_box = Entry(Calculato_Window)

# here some edit on input box shape
result_box.config(font=("Arial", 24), bd=3, relief="sunken")
result_box.config(text="0")
result_box.pack(fill="x")

# here we make the label      (: we put it to display the result  :)   
result_label = Label(Calculato_Window, bg="#40E0D0", height=5,font=("Arial",24))

# here we pack it (put it ) on window and fill = "x" mean its width fit with window with in x direction
result_label.pack(fill="x")


# here we create space or container or fram to put the buttons in it and to be easy to mange them
button_frame = Frame(Calculato_Window, bg="gray", height=20)

# here we pack it (put it ) on window and fill = "x" mean its width fit with window with in x direction
button_frame.pack(fill="x")


# here the function that open the guess game that in Guess_Game file 
def open_test_form():
    import Guess_Game


# here this function just to write the number or the button text in input box
def write(value):
    result_box.insert("end", value)


# here the function to delete or clean the input box
def clear():
        result_box.delete(0, "end")

# here the function to make the mathematical expression
def calculate():
    # here we take the input box text or the written expression
    expression = result_box.get()


    # here we use  re (regular expressions) library to replace every thing is not match whit element ..
    # ... in square brackets[] like digit 0 ot 9 and + - * / and replace it what we want here we replace it with none ""
    cleaned_expression = re.sub(r"[^0-9+\-*/.]", "", expression)


    # here try 
    try:
        # here we use the eval (Evaluate) funtion its built-in in python that recive exspression as string ...
        # .... and calculate or evaluation the expression and return numric resutls
        result = eval(cleaned_expression)
        # here the we  delete or clean the input box and Label :)
        result_label["text"]= ""
        result_box.delete(0, "end")

        # here we put new resutl in the input box and label 
        result_box.insert("end", result)
        result_label["text"]= result

        # here except the errors like  divid any number  over zero 
    except ZeroDivisionError:
        # here the we  delete or clean the input box and Label :)
        result_box.delete(0, "end")
        result_label['text']=""

        # here we put the Error message in the input box and label 
        result_box.insert("end", "Error: division by zero")
        result_label["text"]= "Error: division by zero"


        # in another wrong or mistack related whit any thing 
    except:
        # here the we  delete or clean the input box and Label 
        result_box.delete(0, "end")
        result_label['text']=""

             # here we put the Error message in the input box and label 
        result_box.insert("end", "Error")
        result_label["text"]= "Error"




##################################################################################################
# here we create all circul buttons and edit them shapes and set the command that prforme when the button clicked...
#... and them color and the color when we click on them and border and.....

button_0 = CircleButton(button_frame, text="0", command=lambda: write("0"), bg="#C70039", fg="black", borderless=1, activebackground=("#AE0E36", "#D32E5E"), activeforeground="#E69A8D")
button_1 = CircleButton(button_frame, text="1", command=lambda: write("1"), bg="#C70039", fg="black", borderless=1, activebackground=("#AE0E36", "#D32E5E"), activeforeground="#E69A8D")
button_2 = CircleButton(button_frame,text='2',command=lambda:write(button_2.cget("text")), bg='#C70039',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_3 = CircleButton(button_frame,text='3',command=lambda:write(button_3.cget("text")), bg='#C70039',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_4 = CircleButton(button_frame,text='4',command=lambda:write(button_4.cget("text")), bg='#C70039',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_5 = CircleButton(button_frame,text='5',command=lambda:write(button_5.cget("text")), bg='#C70039',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_6 = CircleButton(button_frame,text='6',command=lambda:write(button_6.cget("text")), bg='#C70039',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_7 = CircleButton(button_frame,text='7',command=lambda:write(button_7.cget("text")), bg='#C70039',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_8 = CircleButton(button_frame,text='8',command=lambda:write(button_8.cget("text")), bg='#C70039',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_9 = CircleButton(button_frame,text='9', bg='#C70039',fg='black',command=lambda:write(button_9.cget("text")), borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_c = CircleButton(button_frame,text='C', bg='#6495ED',command=lambda:clear(),fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D').grid(row=4,column=5)
button_dot = CircleButton(button_frame,text='.', bg='#6495ED',command=lambda:write(button_dot.cget("text")),fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_add = CircleButton(button_frame,text='+',command=lambda:write(button_add["text"]), bg='#6495ED',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_sub = CircleButton(button_frame,command=lambda:write(button_sub.cget("text")),text='-', bg='#6495ED',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_dived = CircleButton(button_frame,text='/',command=lambda:write(button_dived.cget("text")) ,bg='#6495ED',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_mult = CircleButton(button_frame,command=lambda:write(button_mult.cget("text")),text='x', bg='#6495ED',fg='black', borderless=1,activebackground=('#AE0E36', '#D32E5E'),activeforeground='#E69A8D')
button_mult.grid(row=3,column=6);button_dived.grid(row=2,column=6);button_sub.grid(row=3,column=1);button_add.grid(row=2,column=1);
button_0.grid(row=4,column=4) ;button_1.grid(row=1,column=3)  ;button_2.grid(row=1,column=4) ; button_3.grid(row=1,column=5) ;button_4.grid(row=2,column=3) ;button_5.grid(row=2,column=4) ;button_6.grid(row=2,column=5) ;button_7.grid(row=3,column=3) ;button_8.grid(row=3,column=4) ;button_9.grid(row=3,column=5)
test_button = Button(button_frame,command=open_test_form,text="Test\nyour\narithmetic\nabilities",height=5,font=("Arial", 16), bg='#6495ED').grid(row=1,column=1);button_dot.grid(row=4,column=3)
###################################################################################################



# here we detrmine the buttons place on fram or container that we created ...
# .... by row and coulmn
button_mult.grid(row=3,column=6);button_dived.grid(row=2,column=6);button_sub.grid(row=3,column=1);button_add.grid(row=2,column=1);
button_0.grid(row=4,column=4) ;button_1.grid(row=1,column=3)  ;button_2.grid(row=1,column=4) ; button_3.grid(row=1,column=5) ;button_4.grid(row=2,column=3) ;button_5.grid(row=2,column=4) ;button_6.grid(row=2,column=5) ;button_7.grid(row=3,column=3) ;button_8.grid(row=3,column=4) ;button_9.grid(row=3,column=5)


# this equal or =  button that when click it  it call the calculate function
calculate_button = Button(Calculato_Window,text='=',command=calculate,bg='#6495ED',fg='black', height=2, width=7)

# here we pack or (put it ) in window and fill ="x" mean its width will be same window widith
calculate_button.pack(fill="x")



# finally here the mainloop function that displaying the window until we close it 
Calculato_Window.mainloop()

