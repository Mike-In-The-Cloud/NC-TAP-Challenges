#!/usr/bin/env python3.8


# function to assign colour to int
def digit(userInput):
    userInput = userInput.lower()
    # dictonary to 
    switcher = {
        "black" : 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    return switcher.get(userInput, "Invalid colour")


# function to assign colour to int
def suffix(userInput):
    userInput = userInput.lower()
    # dictonary to 
    switcher = {
        "black": "ohms",
        "brown": "ohms",
        "red" : "ohms",
        "orange" : "Kiloohms",
        "yellow" : "Kiloohms",
        "green" : "Megaohms",
        "blue" : "Megaohms",
        "violet" : "Statohms",
        "grey" : "Statohms",
        "white" : "Abohms",
    }
    return switcher.get(userInput, "Invalid colour")

# main function
def main():
    # get user input
    d1, d2, s1 = input("Please enter the THREE colours of the resistor: ").split()
    # process user input
    d1, d2, s1= digit(d1), digit(d2), suffix(s1)
    # print result to user
    print("The resistance is: {}{} {}".format(d1, d2, s1))

# entry point
if __name__ == '__main__':
    main()