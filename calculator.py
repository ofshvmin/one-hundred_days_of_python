import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations  = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    keep_going = True
    number_1 = float(input("What is the first number?"))

    while keep_going:
        for symbol in operations:
            print(symbol)
        operation = input("Choose an operation: ")
        number_2 = float(input("What is the next number?: "))
        result = operations[operation](number_1, number_2)

        print (f"{number_1} {operation} {number_2} = {result}")

        choice = input(f"Type 'y' to continue caclulating with {result}, or type 'n' to start again. ").lower()

        if choice == "y":
            number_1 = result
            keep_going = True

        elif choice == "n":
            keep_going == False
            calculator()

        else:
            print("That is not a valid input.")
            calculator()
calculator()