from Operations  import opeartion as oper
#  User Select  the operation
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Enter equation")  # new option

while True:
    # take input from the user
    choice = input("Enter choice(1|2|3|4|5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        if choice == '5':
            equation = input('Enter the equation(Ex: 11+2-3): ')
            # will keep it as string
        else:
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

            if num2==0:
                # To avoid division by zero error
                print("Error! divide by zero error.")
            else:
                print(num1, "/", num2, "=",oper.divide(num1, num2))

        elif choice == '5':
            # in this case will take full equation from user and calculate the result using 'eval' function
            result = oper.equation_oper(equation)
            if result is not None:
                print(equation, ' = ', result)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower().startswith('n'):  # take other cases such as entering only on letter
            print('Ending app, goodbye.')
            break

    else:
        print("Invalid Input")
