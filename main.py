x=float(input("Введите x:"))
y=float(input("Введите y:"))
print("Введите одну из операций:\n+\n-\n/\n*\n0 - выход")
operation = input("Ввод:")

while True:
    if operation == "0":
        break
    else:
        if operation == "+":
            print(f"Результат = {x+y}")
        elif operation == "-":
            print(f"Результат = {x-y}")
        elif operation == "*":
            print(f"Результат = {x*y}")
        elif operation == "/":
            if y!=0:
                print(f"Результат = {x/y}")
            else:
                print("Error")
    break
