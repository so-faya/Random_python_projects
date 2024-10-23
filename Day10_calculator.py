import Day10_art


# addition
def add(n1, n2):
    return n1 + n2

# subtraction
def subtract(n1, n2):
    return n1 - n2

# division
def divide(n1, n2):
    return n1 / n2

# multiplication
def multiply(n1, n2):
    return n1 * n2

# dictionary for the operators
calculation_operators = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply,
}

def calculate():
    print(Day10_art.logo)
    first_num = int(input("Enter first number: "))

    calculation_running = True
    while calculation_running:
        for symbol in calculation_operators:
            print(symbol)
        operator_sign = input("Enter the operator sign: ")
        second_num = int(input("Enter Second number: "))

        operation = calculation_operators[operator_sign](first_num,second_num)
        print(operation)

        question = input(f"Type 'y' to continue with or type 'n' to start a new calculation:").lower()

        if question == 'n':
            calculation_running = False
            print("\n" * 20)
            calculate()

        elif question == 'y':
            first_num = operation

        else:
            question = input(f"Type 'y' to continue with or type 'n' to start a new calculation:").lower()

calculate()