print("""
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Divition (/)
""")
next_calculation = "Yes"
while(next_calculation in ("Yes","yes","YES")):
    operator = input("Selcet Operator from (+,-,*,/): ")
    first_num = float(input("Enter First Number: "))
    secound_num = float(input("Enter Secound Number: "))
    if operator in ("+","-","*","/"):
        if operator == "+":
            result = first_num + secound_num
            print("The Addition of These Numbers is",result)
        elif operator == "-":
            result = first_num - secound_num
            print("The Subtraction of These Numbers is",result)
        elif operator == "*":
            result = first_num * secound_num
            print("The Multiplication of These Numbers is",result)
        else:
            if(secound_num != 0):
                result = first_num / secound_num
                print("The Divition of These Numbers is",result)
            else:
                print("The Division is not posible or infinite")
    else:
        print("Invalid Operator")
    next_calculation = input("Do You Want To Do Next Calculation (Yes/No): ")
print("Thank you")