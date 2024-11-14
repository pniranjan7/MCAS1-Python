print("Calculator")
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
operation=input("Enter the operation(Addition, Subtraction, Multiplication, Division, Modulus):")
if operation =='Addition':
    result=num1+num2
elif operation =='Subtraction':
    result=num1-num2
elif operation =='Multiplication':
    result=num1*num2
elif operation =='Divison':
    if num2 !=0:
        result=num1/num2
    else:
        print("Error! Division by zero")
elif operation =='Modulus':
    if num2 !=0:
        result=num1%num2
    else:
        result="Error! Division by zero"
else:
    result="Invalid operator!"
print("Result:",result)