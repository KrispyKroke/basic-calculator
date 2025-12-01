



def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def modulus(x, y):
    return x % y


def check_num():
    num = input()
    if type(num) == (int or float):
        return num
    else:
        print("Invalid input.")
        check_num()

def check_operation(num_1, num_2):
    operation = input()
    if operation == '+':
        return addition(num_1, num_2)
    elif operation == '-':
        return subtraction(num_1, num_2)
    elif operation == '/':
        return division(num_1, num_2)
    elif operation == '*':
        return multiplication(num_1, num_2)
    elif operation == '%':
        return modulus(num_1, num_2)
    else:
        print("Invalid operation. Try again. ")
        check_operation()

def calculate():
    print("Welcome! I'm a calculator. Enter " \
        "your first number: ")
    first_num = check_num()
    print("Great! Now enter your second number: ")
    second_num = check_num()
    print("Great! Now enter your operation: ")
    result = check_operation(first_num, second_num)
    return result
    


def main():
    while(1):
        result = calculate()
        print(result)


main()
