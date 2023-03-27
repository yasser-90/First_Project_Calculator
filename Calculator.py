from Operations  import opeartion as oper
#  User Select  the operation
print("Select operation   :)  ")
print("1.Add")
print("2.Subtract")
print("3.Multiply") 
print("4.Divide")
print("5.sin")
print("6.cos")
print("7.tan")
print("8.sqrt")
print("9.reverse")
print("10.exp")
print("11.reminder")   
print("12.max")
print("13.min")

while True: 
    # take input from the user
    choice = input("Enter choice(1 /2 /3 /4 /5 /6 /7 /8 /9 /10 /11 /12 /13): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','11','12 ','13'):
        try: 
            num1 = float(input("Enter first number: "))# user enter first number (operand)
            num2 = float(input("Enter second number: "))# user enter second number (operand)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        print("Result  of Operation = ")
        if choice == '1':
            print(num1, "+", num2, "=", oper.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", oper.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", oper.multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=",oper.divide(num1, num2))
            
        elif choice == '11':
            print(num1, "%", num2, "=", oper.divmod(num1, num2))
            
        elif choice == '12':
            print("the max number=", oper.max(num1, num2))
            
        elif choice == '13':
            print( "the min number=",oper.min(num1, num2))
            
            
            
    elif choice in ('5', '6', '7', '8','9','10'):
        try:
            num1 = float(input("Enter first number: "))# user enter first number (operand)
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        print("Result of Operation = ")
        
        if choice == '5':
            print('sin', num1, "=", oper.sin(num1))

        elif choice == '6':
            print('cos', num1, "=", oper.cos(num1))

        elif choice == '7':
            print('tan', num1, "=", oper.tan(num1))

        elif choice == '8':
            print('sqrt', num1, "=", oper.sqrt(num1))
            
        elif choice == '9':
            print('reverse num of ', num1, "=", oper.revers(num1))
            
        elif choice == '10':
            print('exp', num1, "=", oper.exp(num1))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")