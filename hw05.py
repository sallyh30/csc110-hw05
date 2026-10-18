"""
Name: Sally He
Peers: N/A
References: N/A
"""

def get_letter():
    """ Prompts user to provide an upper case letter (A, B, or C) """
    while True:
        # 1. ask for a string with the prompt: `"Give an single uppercase
        # letter: "`
        letter = input("Give an single uppercase letter: ")
        # 2. If the length of the provided text is different than 1
        if len(letter) > 1:
            print("Error: it needs to be a single character.")
            continue
        # 3. If the provided letter is not "A", "B", or "C"
        if letter not in ("ABC"):
            print("Error: You provided the wrong character.")
            continue
        break
    return letter

def get_digit():
    """ Prompts user to provide an integer (1, 2, or 3) """
    while True:
        # 1. ask for a string with the prompt: `"Give an single number character: "`
        digit = input("Give an single number character: ")
        # 2. If the provided text is not composed of only digits,
        if not digit.isdigit():
            print ("Error: your input should be only digits.")
            continue
        # 3. If the provided digit is not "1", "2", or "3"
        if digit not in ("123"):
            print("Error: a single digit needs to be in [1,3].")
            continue
        # 4. If the provided digit more than one digit
        if len(digit) > 1:
            print("Error: a single digit needs to be in [1,3].")
            continue
        break
    return digit


def check_pattern(letter, digit, lst):
    """ Checks the letter character and the digit character received
    and distinguishes the pattern
    """
    print ("String with the pattern:")
    digit_str = str(digit)
    for i in (lst):
        # checks if any of the words inside the list contain the letter and number
        if letter in i and digit in i:
            ch = i.index(letter)
            dg = i.index(digit_str)
            # check if the words contain the letter and number
            # have the correct order(the letter comes before the number)
            if dg > ch:
                # print the eligible words in the same line and separated by a space
                print (f"{i}", end = " ")
    print()



def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    lst = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    # TODO: Add your calls to get_letter, get_digit, and check_pattern        
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    while True:
        # 1. get a letter and a digit from the user
        #(calling the  get_letter and get_digit functions)
        letter = get_letter()
        digit = get_digit()
        # 2. checks the pattern to print the valid strings
        #(calling the check_pattern function)
        check_pattern(letter, digit, lst)
        # 3. After any words are printed, asks the user if they want to continue
        ask=input("Try Again? (y/n): ")
        # 4. if the user does not respond 'y', it ends;
        # otherwise repeat steps 1 - 4.
        if ask == "y":
            continue
        if ask == "n":
            break

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()