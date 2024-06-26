# ---------------------------- CONSTANTS ------------------------------- #

LOGO = """
 ____   ___  _   _   _    ____  _____       
/ ___| / _ \| | | | / \  |  _ \| ____|      
\___ \| | | | | | |/ _ \ | |_) |  _|        
 ___) | |_| | |_| / ___ \|  _ <| |___       
|____/ \__\_\____/_/   \_\_| \_\_____|      
  __ _ _ __   __| |                         
 / _` | '_ \ / _` |                         
| (_| | | | | (_| |                         
 \__,_|_| |_|\__,_|____ ___ ____  _  __   __
|  \/  | | | | | |_   _|_ _|  _ \| | \ \ / /
| |\/| | | | | |   | |  | || |_) | |  \ V / 
| |  | | |_| | |___| |  | ||  __/| |___| |  
|_|  |_|\___/|_____|_| |___|_|   |_____|_|  
"""


# ---------------------------- Functions ------------------------------- #

def print_logo():
    """
    Print the logo of the program to the console.
    :return: None
    """

    print()
    print(LOGO)
    print()


def validate_user_input(prompt):
    """
    Validate the user input.
    :param str prompt: The prompt message to display to the user.
    :return: The validated integer input from the user.
    """

    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)

            if value <= 0:
                raise ValueError("Invalid Input: Please enter a positive number.")
            break

        except ValueError:
            print("Invalid Input: Please enter a positiv number.")

    return value


def square_multiply(base, exponent, modulo):
    """
    Performs the square and multiply algorithm.
    :param int base: The base number.
    :param int exponent: The exponent.
    :param int modulo: The modulo.
    :return: The result of the square and multiply algorithm.
    """

    res = base
    exponent_in_bit = bin(exponent)[3::]

    for bit in exponent_in_bit:
        res = (res ** 2) % modulo

        if bit == "1":
            res = (res * base) % modulo

    return res


def main():
    """
    Main function of the program.
    :return: None
    """

    print_logo()

    # Variables
    base = validate_user_input("Base: ")
    exponent = validate_user_input("Exponent: ")
    modulo = validate_user_input("Modulo: ")

    # Body
    print(10 * "-")
    print(f"Result: {square_multiply(base, exponent, modulo)}")


# ------------------------------ Main ---------------------------------- #

if __name__ == "__main__":
    main()
