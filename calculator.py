import time

from operations import Opeartion as oper
#  User Select  the operation
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.cos")
print("6.sin")
print("7.tan")
print("8.squer")
print("9.factoril")
print("10.pwoer")
print("11.remender")
generalOp = ['1', '2', '3', '4']
mathmaticsOp = ['5', '6', '7', '8', '9']
start = True
while start:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11): ")

    # check if choice is one of the four options
    if choice in ('10', '11') or choice in generalOp or choice in mathmaticsOp:

        try:
            if choice in generalOp:
                userInputs = []
                userNumber = int(input("How many number do you have?: "))
                for count in range(userNumber):
                    number = float(input(f"Enter number {count+1}: "))
                    userInputs.append(number)
                print("Result of Operation =")
                if choice == '1':
                    print(oper.add(userInputs))

                elif choice == '2':
                    print(oper.subtract(userInputs))

                elif choice == '3':
                    print(oper.multiply(userInputs))

                elif choice == '4':
                    print(oper.divide(userInputs))

            elif choice in mathmaticsOp:
                number = float(input(f"Enter number : "))
                if choice == '5':
                    print(oper.cos(number))

                elif choice == '6':
                    print(oper.sin(number))

                elif choice == '7':
                    print(oper.tan(number))

                elif choice == '8':
                    print(oper.squer(number))
                elif choice == '9':
                    print(oper.factoril(number))
            else:
                x = float(input(f"Enter X : "))
                y = float(input(f"Enter Y : "))
                if choice == '10':
                    print(oper.power(x, y))
                elif choice == '11':
                    print(oper.remender(x, y))

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        while True:
            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "yes":
                break
            elif next_calculation == "no":
                print('Exiting...')
                time.sleep(3)
                start = False
                break
            else:
                print('Please choose "yes" or "no"')
    else:
        print("Invalid Input")
