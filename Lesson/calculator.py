# Calculator option 1

a = float(input("value: "))
b = float(input("value: "))
action = input("action: ")

if action == "+":
    print(int(a + b))
elif action == "-":
    print(int(a - b))
elif action == "/":
    print(int(a / b))
elif action == "*":
    print(int(a * b))
else:
    print("Incorrect value")


# # Calculator option 2


a = float(input("value: "))
b = float(input("value: "))

while True:
    action = input("action: ")
    result = 0
    if action == "+":
        result = int(a + b)
    elif action == "-":
        result = int(a - b)
    elif action == "/":
        result = int(a / b)
    elif action == "*":
        result = int(a * b)
    else:
        print("Incorrect value")
        continue

    print(result)
    break
