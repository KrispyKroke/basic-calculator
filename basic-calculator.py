import sys



def addition(x, y):
    return round(float(x) + float(y), 2)

def subtraction(x, y):
    return round(float(x) - float(y), 2)

def multiplication(x, y):
    return round(float(x) * float(y), 2)

def division(x, y):
    return round(float(x) / float(y), 2)

def modulus(x, y):
    return round(float(x) % float(y), 2)


def check_num():
    run_func = True
    while run_func:
        num = input()
        if num == 'quit':
            sys.exit()
        try:
            float(num)
            run_func = False
        except:
            print("Invalid input. Please enter a number. ")
    return num

        
        

def check_operation(num_1, num_2):
    while True:
        operation = input()
        if operation == '+' or operation == 'addition':
            return addition(num_1, num_2)
        elif operation == '-' or operation == 'subtraction':
            return subtraction(num_1, num_2)
        elif operation == '/' or operation == 'division':
            return division(num_1, num_2)
        elif operation == '*' or operation == 'multiplication':
            return multiplication(num_1, num_2)
        elif operation == '%' or operation == 'modulus':
            return modulus(num_1, num_2)
        elif operation == 'quit':
            sys.exit()
        else:
            print("Invalid operation. Please enter a valid operation. ")
        

def calculate():
    print("Welcome! I'm a calculator. Enter " \
        "your first number: (Type 'quit' to exit the program.)")
    first_num = check_num()
    print("Great! Now enter your second number: ")
    second_num = check_num()
    print("Great! Now enter your operation: ")
    result = check_operation(first_num, second_num)
    return result
    


def main():
    while 1:
        result = calculate()
        print("Great! Your answer is: ", result)


main()
