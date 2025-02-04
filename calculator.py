def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    # Continuous loop to keep the app running
    while True:
        # Hardcoded values for demonstration
        operation = '1'  # 1 for Add
        num1 = 10
        num2 = 20

        if operation == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

if __name__ == "__main__":
    main()

