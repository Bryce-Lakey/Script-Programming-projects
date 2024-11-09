"""
File: testinputfunctions.py

Defines a function for robust input of ints.
"""

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return float(theString)
        else:
            print("This is a float.")

def main():
    n = inputInt("Please enter a number: ")
    print(n)
    f = inputFloat("Please enter a non-whole number: ")
    print(f)

if __name__ == "__main__":
    main()
