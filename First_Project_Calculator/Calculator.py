from Operations  import opeartion as oper
#  User Select  the operation
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply") 
print("4.Divide")
print("5.max")
print("6.min")
print("7.power")
print("8.remainder")
print("9.underdivided")
print("10.sqrt")
print("11.sin")
print("12.cos")
print("13.tan")
print("14.factorial")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

    # check if choice is one of the options
    if choice in ('1', '2', '3', '4' , '5' , '6' , '7' , '8' , '9'):
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
            print(num1, "/", num2, "=",oper.divide(num1, num2))

        elif choice == '5':
            print(num1, "max", num2, "=",oper.max(num1, num2))

        elif choice == '6':
            print(num1, "min", num2, "=",oper.min(num1, num2))

        elif choice == '7':
            print(num1, "power", num2, "=",oper.power(num1, num2))

        elif choice == '8':
            print(num1, "remainder", num2, "=",oper.remainder(num1, num2))

        elif choice == '9':
            print(num1, "underdivided", num2, "=",oper.underdivided(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    elif choice in ('10', '11', '12' , '13' , '14'):
        try:
            num = float(input("Enter first number: "))# user enter first number (operand)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        print("Result of Operation = ")
        if choice == '10':
            print( "sqrt",'(', num , ')', "=", oper.sqrt(num))

        elif choice == '11':
            print( "sin",'(', num , ')', "=",oper.sin(num))

        elif choice == '12':
            print("cos",'(', num , ')', "=",oper.cos(num))
        
        elif choice == '13':
            print("tan",'(', num , ')', "=",oper.tan(num))
        
        elif choice == '14':
            print("factorial",'(', num , ')', "=",oper.factorial(num))
        

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break

    else:
        print("Invalid Input")

    