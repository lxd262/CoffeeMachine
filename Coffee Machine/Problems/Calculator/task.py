# put your python code here
a, b, operand = float(input()), float(input()), input()
if operand == "+":
    ans = a + b
elif operand == "-":
    ans = a - b
elif operand == "*":
    ans = a * b
elif operand == "pow":
    ans = pow(a, b)
else:
    if b == 0:
        ans = "Division by 0!"
    elif operand == "/":
        ans = a / b
    elif operand == "mod":
        ans = a % b
    elif operand == "div":
        ans = a // b
print(ans)

