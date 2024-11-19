"""imports calculator module"""
import calculator
"""imports os module"""
import os
"""function to add two numbers"""
def add(num1, num2):
    """returns the sum of two numbers"""
    return num1 + num2
"""function to subtract two numbers"""
def sub(num1, num2):
    """returns the difference of two numbers"""
    return num1 - num2
"""function to multiply two numbers"""
def mul(num1, num2):
    """returns the product of two numbers"""
    return num1 * num2
"""function to divide two numbers"""
def div(num1, num2):
    """returns the division of two numbers"""
    return num1 / num2

"""function to calculate"""
def calc():
    """prints the calculator logo"""
    print(calculator.logo)
    """takes the first number from the user"""
    firstNum = float(input("What's the first number?: "))
    """prints the operator symbols"""
    print("""
        +
        -
        *
        /
    """)
    """initially the calulator has not ended"""
    endOfCalculator = False
    """until the calculator has not ended, this loop will run"""
    while (endOfCalculator == False):
        """asks and stores the operation"""
        operator = input("Pick an operation: ")
        """stores the second number"""
        secondNum = float(input("What's the next number?: "))
        """if operator is + result is sum of the two numbers"""
        if (operator == "+"):
            result = add(firstNum, secondNum)
            """else if operator is - result is difference of the two numbers"""
        elif (operator == "-"):
            result = sub(firstNum, secondNum)
            """else if operator is * result is product of the two numbers"""
        elif (operator == "*"):
            result = mul(firstNum, secondNum)
            """else if operator is / result is division of the two numbers"""
        elif (operator == "/"):
            result = div(firstNum, secondNum)
        """prints in the manner '1 + 2 = 3"""
        print(f"{firstNum} {operator} {secondNum} = {result}")
        """asks the user to continue the calculation or start a new calculation"""
        continueCalculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        """if user wishes to continue, firstNum is set to the result"""
        if (continueCalculating == 'y'):
            firstNum = result
            """else if the user wishes to start a new calculation, the loop breaks and endOfCalculator is set to true;
            the screen clears, and the function is called again"""
        elif (continueCalculating == 'n'):
            endOfCalculator = True
            os.system("clear")
            calc()
        else:
            print("Wrong input. Program terminated!")
            endOfCalculator = True
"""function calc() is called initially""" 
calc()
    



