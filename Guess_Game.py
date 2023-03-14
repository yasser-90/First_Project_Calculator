# here  call the library (tool kit interface) that help us to make GUI 
from tkinter import * 

# here we call the random library to use it to give us nubmer randomly 
import random

# here we create window or form as you want 
window = Tk()


# here we disable or hide the window defualt buttons   (exit , minmize , maximize)
window.attributes('-toolwindow',True)


# here we disable sizableity of window
window.resizable(False,FALSE)

# here we give the window title the name that shows up of window
window.title("CALCULATOR")

# here determine window size (width = 400 , height = 500  , X = 450  , Y = 50)
window.geometry("400x500+450+50")

# here we have function to help us when first click and second click   .....
# in first click he call the change function and on the second click call the true function
# here the variable that represent nmbert of clicks
num_of_click = 0
def click():
    # here we make the var global to use it out of the function or where we need it
    global num_of_click
    # here he increment by 1
    num_of_click+=1
    # here the condition 
    if num_of_click == 1 :
        change()
    else:
        true()
        num_of_click=0



# her we have change function that called when we click suffle button
def change():
             # we clean the lable text
             result_Lable["text"] = ""

             # we make this vars global to call them from other function 
             global random_number1
             global random_number2
             global random_operation


             # here we get the two  random number between 1 and 100 by using thw randowm library function randint(random integer) 
             random_number1 = random.randint(1, 100)
             random_number2 = random.randint(1, 100)

             # here again using random laibrary choice function to choice between given operation + - * / randomly
             random_operation = random.choice(["+", "-", "*", "/"])

             # here check if the button text is "Shuffle"
             if button.cget("text") == "Shuffle":
               
                # if condition is true here we change or put new the  qustion lable text (Expression) ... 
                # we put first random number and random operation and second random numbert
               Question_Lable["text"] = str(random_number1) + " " + str(random_operation) + " " + str(random_number2)
    
               # here change the button text to "Check"
               button['text'] = 'Check'
             else :
               
               # here change the button text to "Shuffle"
               button['text'] = 'Shuffle'


def true():    

               # here we call the randoms number and operation to check the user answer is true or false    
               global random_number1
               global random_number2
               global random_operation
             
               # if the input box is null or empty we tell the user            
               if result_inputt.get() == "" :
                  result_Lable["text"] = "There Is No Answer"
               
     
               else:
                    # here we take the inputed value
                    temp = int(result_inputt.get()) 
                    
                    # if the random operation is + 
                    if random_operation == "+":
                         
                         #here we calculate the question and compare whit the user input
                        if temp == random_number1 + random_number2 :
                           
                           result_Lable["text"] = "True"
                           
                           button['text'] = 'Shuffle'
                        
                        else:
                        
                           result_Lable["text"] = "False"
                        
                           button['text'] = 'Shuffle'

                    
                    # if the random operation is - 
                    if random_operation == "-" :
                       
                       #here we calculate the question and compare whit the user input
                        if temp == random_number1 - random_number2 :
                       
                           result_Lable["text"] = "True"
                       
                           button['text'] = 'Shuffle'
                        
                        else:
                        
                           result_Lable["text"] = "False"
                        
                           button['text'] = 'Shuffle'
                        

                        # if the random operation is / 
                        if random_operation == "/":
                        
                        #here we calculate the question and compare whit the user input
                           if temp == random_number1 / random_number2 :
                        
                              result_Lable["text"] = "True"
                        
                              button['text'] = 'Shuffle'
                           
                           else:
                           
                              result_Lable["text"] = "False"
                           
                              button['text'] = 'Shuffle'
                        

                        # if the random operation is * 
                        if random_operation == "*":
                        
                        #here we calculate the question and compare whit the user input
                         if temp == random_number1 * random_number2 :
                              
                              result_Lable["text"] = "True"
                              
                              button['text'] = 'Shuffle'
                         
                         else:
                         
                              result_Lable["text"] = "False"

                              button['text'] = 'Shuffle'
            
            
# here we create the button and set command to it and edit it Shape
button = Button(window, command=click, text="Shuffle", width="20", height="2", bg="purple", fg="white", border="10")

# here we pack or (put it ) in window but on the bottom of window
button.pack(side=BOTTOM)

# here we create the label 
Question_Lable = Label(window, height="5", bg="gray", font=('Arial', 30))

# here we pack the label and make it widht fit with window widht
Question_Lable.pack(fill="x")

# here create the label we diplaying  the true or false and edit it shape
result_Lable = Label(window ,width=30,height=2, bg="black", font=('Arial', 20),fg="white")

# here we detrmine place of label in detlis
result_Lable.place(x=0,y=290)

# here is the var that we use to get the input box string or value
result_inputt = StringVar(window)

# here we cerate the input box that user enter the value to it
result_input = Entry(window,textvariable=result_inputt)

# here we determine the input box in detiles
result_input.place(x=135,y=250)

# finally here the mainloop function that displaying the window until we close it 
window.mainloop()
