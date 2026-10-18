"""
Name: Sally He
Peers: N/A
References: N/A
"""

def get_letter():
    """ Prompts user to provide an upper case letter (A, B, or C) """
    while True:
        letter = input("Give an single uppercase letter: ")
        if len(letter) > 1:
            print("Error: it needs to be an single character.")
            continue
        if letter not in ("ABC"):
            print("Error: You provided the wrong character.")
            continue
        break
    return letter

def get_digit():
    """ Prompts user to provide an integer (1, 2, or 3) """
    while True:
        digit = input("Give an single number character: ")
        if not digit.isdigit():
            print ("Error: your input should be only digits.")
            continue
        if digit not in ("123"):
            print("Error: a single digit needs to be in [1,3]")
            continue
        if len(digit) > 1:
            print ("Error: it needs to be an single integer")
            continue
        break
    return digit


def check_pattern(letter, digit, lst):
    """ Add your own Docstring """
    # remove the default pass and add your code
    pass


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    get_letter()
    get_digit()
    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()