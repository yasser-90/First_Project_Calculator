from Operations  import opeartion as oper
#  User Select  the operation
print("Select type.")
print("1-simple.")
print("2-advance")
history=[]
while True:
    # take input from the user
    choice = input("Enter choice(1/2): ")

    # check if choice is one of the four options
    if choice ==('1'):
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        choice = input("Enter choice(1/2/3/4): ")
        

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
                 history.append([num1, '+', num2, '=', oper.add(num1, num2)])
                 
            elif choice == '2':
                print(num1, "-", num2, "=", oper.subtract(num1, num2))
                history.append([num1, "-", num2, "=",oper.subtract(num1, num2)])
            

            elif choice == '3':
                print(num1, "*", num2, "=", oper.multiply(num1, num2))
                history.append([num1, "*", num2, "=",oper.multiply(num1, num2)])
            

            elif choice == '4':
               print(num1, "/", num2, "=",oper.divide(num1, num2))
               history.append([num1, "/", num2, "=",oper.divide(num1, num2)])
            
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        #show_history = input("show history enter? (yes/no): ")
        if next_calculation == "no":
          print(history)
          break
        elif next_calculation == "yes":
            continue
        else:
            print("Invalid Input please try agine ")
        
        #if show_history == "yes":
            
       # elif show_history == "no":
        #    continue
       # else:
         #   print("Invalid Input please try agine ")
       
    elif choice ==('2'):
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.squared")
        print("6.cos")
        print("7.sin")
        print("8.tan")
        print("9.power")
        print("10.reminder")
        print("11.square root")
        print("12.cube root")
        #print("13.invers cos")
        #print("14.invers sin")
        #print("15.invers tan")
        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12): ")
        if choice in ('1', '2', '3', '4','9','10'):
            try:
                 num1 = float(input("Enter first number: "))# user enter first number (operand)
                 num2 = float(input("Enter second number: "))# user enter second number (operand)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            print("Result of Operation = ")
            if choice == '1':
                 print(num1, "+", num2, "=", oper.add(num1, num2))
                 history.append([num1, "+", num2, "=",oper.add(num1, num2)])
           
            elif choice == '2':
                print(num1, "-", num2, "=", oper.subtract(num1, num2))
                history.append([num1, "-", num2, "=",oper.subtract(num1, num2)])

            elif choice == '3':
                print(num1, "*", num2, "=", oper.multiply(num1, num2))
                history.append([num1, "*", num2, "=",oper.multiply(num1, num2)])

            elif choice == '4':
               print(num1, "/", num2, "=",oper.divide(num1, num2))
               history.append([num1, "/", num2, "=",oper.divide(num1, num2)])
            elif choice == '9':
               print(num1, "^", num2, "=",oper.power1(num1, num2))
               history.append([num1, "^", num2, "=",oper.power1(num1, num2)])
            elif choice == '10':
               print(num1, "%", num2, "=",oper.percentage1(num1, num2))
               history.append([num1, "%", num2, "=",oper.percentage1(num1, num2)])

            
        elif choice in ('5', '6', '7','8','12','11'):
            try:
                 num1 = int(input("Enter the number: "))# user enter first number (operand)
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
           
            print("Result of Operation = ")
            if choice == '5':
                print(num1, "^", '2', "=",oper.squared1(num1))
                history.append([num1, "^", '2', "=",oper.squared1(num1)])

            elif choice == '6':
               print("cos", num1, "=", oper.cosin(num1))
               history.append(["cos", num1, "=",oper.cosin(num1)])
               
            elif choice == '7':
               print("sin", num1, "=", oper.sinn(num1))
               history.append(["sin", num1, "=",oper.sinn(num1)])
 
            elif choice == '8':
               print("tan", num1, "=", oper.tann(num1))
               history.append(["tan", num1, "=",oper.tann(num1)])
            elif choice == '11':
               print("√", num1, "=",oper.root1(num1))
               history.append(["√", num1, "=",ooper.root1(num1)])
            elif choice == '12':
               print( "3√", num1, "=",oper.cr(num1))
               history.append(["3√", num1, "=",oper.cr(num1)])
          #  elif choice == '13':
           #    print( "invers cos", num1, "=",oper.inverscos11(num1))
           # elif choice == '14':
           #    print( "invers sin", num1, "=",oper.inverssin(num1))
           # elif choice == '15':
            #   print( "invers tan", num1, "=",oper.inverstan(num1))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
             print(history)
             break
        elif next_calculation == "yes":
            continue
        else:
            print("Invalid Input please try agine ")
        

        #show_history = input("show history")
        #if show_history == "yes":
        
        #elif show_history == "no":
        #    continue
       # else:
            #print("Invalid Input please try agine ")
    else:
        print("Invalid Input")

    
    
