num1 = int(input())
num2 = int(input())
operation = input()
res_type = ""

if (operation == "/" or operation == "%") and (num1 == 0 or num2 == 0):
    print(f"Cannot divide {num1} by zero")
else:
    if operation == "+":
        result = num1 + num2

        if result % 2 == 0:
            res_type = "even"
        else:
            res_type = "odd"

        print(f"{num1} {operation} {num2} = {result} - {res_type}")

    elif operation == "-":
        result = num1 - num2

        if result % 2 == 0:
            res_type = "even"
        else:
            res_type = "odd"

        print(f"{num1} {operation} {num2} = {result} - {res_type}")

    elif operation == "*":
        result = num1 * num2

        if result % 2 == 0:
            res_type = "even"
        else:
            res_type = "odd"

        print(f"{num1} {operation} {num2} = {result} - {res_type}")

    elif operation == "/":
        result = num1 / num2

        print(f"{num1} {operation} {num2} = {result:.2f}")

    elif operation == "%":
        result = num1 % num2

        print(f"{num1} {operation} {num2} = {result}")
