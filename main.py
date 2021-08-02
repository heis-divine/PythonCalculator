# Calculator project
print("What Calculation would you like to perform?")
print("1)Addition\n2)Subtraction\n3)Multiplication\n4)Division")
choice = int(input("Enter preferred Option: "))
if choice == 1:
    print("Addition")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    total = num1 + num2
    print(total)
    print("The sum of the two numbers entered are:", total)
    print("Thanks for using our calculator")
elif choice == 2:
    print("Subtraction")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    total1 = num1 - num2
    print("The difference of the two numbers entered are:" , total1)
    print("Thanks for using our calculator")
elif choice == 3:
    print("Multiplication")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    total2 = num1 * num2
    print("The product of the two numbers entered are:" , total2)
    print("Thanks for using our calculator")
elif choice == 4:
    print("Division")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    total3 = num1 / num2
    print("The quotient of the two numbers entered are:" , total3)
    print("Thanks for using our calculator")
