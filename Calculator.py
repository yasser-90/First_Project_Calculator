from Operations  import opeartion as oper
from Operations import operation2

from tkinter import *


def simple_cal_gui():

    # Create the GUI
    tk = Tk()
    tk.title('Simple Calculator')

    inp = Entry(tk, text="Enter Expression Here", width=20, font=('Times', 15))
    inp.pack(padx=10, pady=20)

    btn = Button(tk, text="Quit?")
    btn.pack()

    canvas = Canvas(tk, width=200, height=200)
    canvas.pack()


    # Create callback functions
    def end_program(event):
        '''Destroys the window and ends the program without needing
        to use global variables or a while loop'''
        tk.destroy()
        exit() # Automatically ends any Python program


    def update_canvas(event):
        '''Gets the input, tries to eval it, and displays it to the canvas'''
        expression = inp.get()
        try:
            solved = eval(expression)
        except SyntaxError:
            # The expression wasn't valid, (for example, try typing in "2 +")
            # so I defaulted to something else.
            solved = '??'
        except NameError:
            solved = 'invalid!'
        except ZeroDivisionError:
            solved = 'infinity!'
        canvas.delete('all')  # remove old text to avoid overlapping
        canvas.create_text(100, 100, text=expression, font=('Times', 10))
        canvas.create_text(100, 150, text=f'result={solved}', font=('Times', 15), fill='red', anchor='s')


    # Bind callbacks to GUI elements
    btn.bind('<Button-1>', end_program)
    inp.bind('<KeyRelease>', update_canvas)

    # Run the program
    tk.mainloop()


def simple_cal():
    #  User Select  the operation
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))# user enter first number (operand)
                num2 = float(input("Enter second number: "))# user enter second number (operand)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            print("Result of Operation = ")
            if choice == '1':
                print(num1, "+", num2, "=", oper.add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", oper.subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", oper.multiply(num1, num2))

            elif choice == '4':
                try:
                    print(num1, "/", num2, "=",oper.divide(num1, num2))
                except ZeroDivisionError:
                    print("Cannot divide by zero")
            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no): ")
           
            while next_calculation not in ('yes', 'y'):
                if next_calculation in ('no', 'n'):
                    print("Exiting ...")
                    exit()
                print("to continue type 'yes' or 'y' !")
                next_calculation = input("Let's do next calculation? (yes/no): ")
        else:
            print("Invalid Input")
def simple_cal2():
    while True:
        # to call input method form operation class
        operation2.input(operation2)
        # to check if continue the loop or break it
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation in ("no", "n", "NO", "N", "No"):
            exit()


print("...Welcome...\nselect calculator type:\n1-simple calculator\n2-simple calculator2\n3-simple gui calculator")
choice = input("\nselect:")

if choice == '1':
    simple_cal()
elif choice == '2':
    simple_cal2()
elif choice == '3':
    simple_cal_gui()
