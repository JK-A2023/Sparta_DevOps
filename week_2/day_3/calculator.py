"""
    Calculator - Uses 4 base functions of addition, subtraction, multiplication, and division.
    The while statement assumes a start of True of user_continue. If at the end of a cycle, the user enters "No",
    the status of user_continue will flip and become False. The script then exits.
"""

def addition(int1, int2):
    return int1 + int2


def subtraction(int1, int2):
    return int1 - int2


def multiplication(int1, int2):
    return int1 * int2


def division(int1, int2):
    return int1 / int2


def calculator():
    choices = ["Addition", "Subtraction", "Multiplication", "Division"]
    user_continue = True

    while user_continue:

        print(choices)
        first_input = input("Select operation:").strip()

        if first_input not in choices:
            print("Please select a valid option")
            continue

        first_number_select = (float(input("choose first number").strip()))
        second_number_select = (float(input("choose second number").strip()))

        if first_input == choices[0]:
            result = (addition(first_number_select, second_number_select))

        elif first_input == choices[1]:
            result = (subtraction(first_number_select, second_number_select))

        elif first_input == choices[2]:
            result = (multiplication(first_number_select, second_number_select))

        elif first_input == choices[3]:
            result = (division(first_number_select, second_number_select))

        print(f"Result: {result}")

        choices_to_cont = ["Yes", "No"]
        continue_choice = input("Do you want to continue: ")

        if continue_choice == choices_to_cont[1]:
            print("Cheers")
            user_continue = False

calculator()