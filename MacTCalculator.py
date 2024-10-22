import os
import math
from decimal import Decimal
clear = lambda: os.system('clear')

pi = math.pi
# divide up the menu into sections
line = 70
# error messages
errMen = 'Error ... Invalid selection. Try again.'
errAng = 'Error ... Invalid unit of angle. Try again.'
errIn = 'Error ... Invalid input. Try again.'
err0 = 'Error ... Attempted division by zero. Try again.'
und = 'The result is undefined.'

def main():
    playerName = input('Please enter your name to begin: ')
    print('Hello ' + str(playerName) + ', welcome to the MacT Calculator!')

    menu = 0
    while menu != 5:
        # reset value in case of invalid inputs
        menu = 0
        print("-"*line)
        print("Main Menu\
              \n1. Start the Calculator\
              \n2. Program Information\
              \n3. Learn about Taylor/Maclaurin series.\
              \n4. Dedication & Contributors\
              \n5. Quit")
        
        try:
            menu = int(input("\nPlease select one of the options above: "))
        except ValueError:
            print(errMen)

        if menu == 1:
            # open up list of functions for user to pick from
            Calc(playerName)
        elif menu == 2:
            # information on how program works and appropriate syntax
            ShowInfo()
        elif menu == 3:
            # information on the calculus behind the program
            ShowLearn()
        elif menu == 4:
            Special()
        elif menu == 5:
            print('Shutting down ...\
                  \nGoodbye ' + str(playerName) + ', and thank you for using the MacT calculator.')

def Calc(playerName):
    calcMenu = 0
    while calcMenu not in ['Q', 'q']:
        # initialize result, nth term of the series, unit type
        computedResult = 0
        n = 0
        num = 0
        type = ' '
        print("-"*line)
        # easier way to alter list
        FunctionList()

        try:
            calcMenu = input('\n' + str(playerName) + ', please select one of the options above: ')
        except ValueError:
            print(errMen)

        # different symbols for distinct groups of functions (i.e. trig, exp, log, geometric)
        if calcMenu in [1, 2, 3, 4, 5, 6]:
            print("~"*line)
        elif calcMenu in [7, 8, 9, 10, 11, 12]:
            print("*"*line)
        
        if calcMenu == '1':
            num, type = Prompt(calcMenu, num, type)
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                n, computedResult = sin(num, type, n, computedResult)
                print("~"*line)
                print(f"sin({num}) =", computedResult)
                nCompare(n)
            elif type in [' ', 0]:
                continue # to prevent multipe error messages from printing
            else:
                print(errAng)

        elif calcMenu == '2':
            num, type = Prompt(calcMenu, num, type)
            if type in ["deg", "rad"]:
                n, computedResult = cos(num, type, n, computedResult)
                print("~"*line)
                print(f"cos({num}) =", computedResult)
                nCompare(n)
            elif type in [' ', 0]:
                continue
            else:
                print(errAng)

        elif calcMenu == '3':
            num, type = Prompt(calcMenu, num, type)
            if type in ["deg", "rad"]:
                tan(num, type, n, computedResult)      
            elif type in [' ', 0]:
                continue
            else:
                print(errAng)

        elif calcMenu == '4':
            num, type = Prompt(calcMenu, num, type)
            # output is in radians so type remains unspecified
            if type == ' ':
                n, computedResult = arctan(num, n, computedResult)
                
        elif calcMenu == '5':
            # exp and log do not use angles as inputs
            num, type = Prompt(calcMenu, num, type)
            if type == ' ':
                n, computedResult = e(num, n, computedResult)
                print("~"*line)
                print(f"e^({num}) =", computedResult)
                nCompare(n)
            
        elif calcMenu == '6' or calcMenu == '7':
            num, type = Prompt(calcMenu, num, type)
            if type == ' ':
                n = ln(num, calcMenu, n, computedResult)
                nCompare(n)

        elif calcMenu in ['Q', 'q']:
            print('Returning to Main Menu ...')

# prompt user for the input value and, if applicable,
# the unit of angle
def Prompt(calcMenu, num, type):
    try:
        num = eval(input('Enter your desired value: '))
        if calcMenu in ['1', '2', '3']: # trig functions
            type = input('Enter the unit of angle (deg or rad): ')
    except (ValueError, SyntaxError, NameError):
        print(errIn)
    except ZeroDivisionError: # user inputs a fraction with a 0 as the denominator
        print(err0)
        type = 0 # prevent multiple error messages from displaying

    return num, type

# inputs given in degrees must be converted into radians
def ConvertRad(type, num):
    if type == "deg":
        num = (num * pi)/180
    return num

# use functions from math library to compare results and get the nth term of the series
def nCompare(n):
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")

# trig functions take a value then the unit of that value "rad" or "deg"
# i.e. sin(45, "deg"), tan(pi/3, "rad")
def sin (num, type, n, computedResult):
    num = ConvertRad(type, num)
    # Used to get comparable result
    result = math.sin(num)
    while computedResult <= result - 0.00001 or computedResult >= result + .00001:
        # maclaurin series of sine
        computedResult += ((-1) ** n) * (num ** (2 * n + 1)) / math.factorial(2 * n + 1)
        n += 1

    return n, computedResult

def cos(num, type, n, computedResult):
    num = ConvertRad(type, num)
    result = math.cos(num)
    while computedResult <= result - 0.00001 or computedResult >= result + .00001:
        # maclaurin for cosine
        computedResult += ((-1) ** n) * (num ** (2 * n)) / math.factorial(2 * n)
        n += 1

    return n, computedResult

def tan(num, type, n, computedResult):
    # deg to rad conversion is not included as it is done in the sin and cos functions
    try:
        # the actual maclaurin series for tangent is a mess and involves the Bernoulli numbers, no thanks
        computedTan = sin(num, type, n, computedResult)[1] / cos(num, type, n, computedResult)[1]
        n = sin(num, type, n, computedResult)[0]
        print("~"*line)
        print(f"tan({num}) =", computedTan)
        nCompare(n)      
    except ZeroDivisionError: # tan is undefined when cos(x) = 0, occuring at odd multiples of pi/2 rad
        print(und)

def arctan(num, n, computedResult):
    result = math.atan(num)
    try:
        while computedResult <= result - 0.00001 or computedResult >= result + .00001:
            # maclaurin of inverse tangent
            computedResult += ((-1) ** n) * (num ** (2 * n + 1)) / (2 * n + 1)
            n += 1
        print("~"*line)
        print(f"arctan({num}) =", computedResult)
        nCompare(n)
    except OverflowError: # domain of the series is |x| < 1
        print("Value exceeds domain of the function.")

    return n, computedResult
##### nonetype error? #####
def e(num, n, computedResult):
    #Used only to get comparable result 
    result = math.e**(num)
    while computedResult <= result - 0.00001 or computedResult >= result + .00001:
        # maclaurin for e^x
        computedResult += (num ** (n)) / math.factorial(n)
        n += 1
##### print in here doesn't display? #####
def ln(num, calcMenu, n, computedResult):
    # series does not use the first term
    n = 1
    # maclaurin for ln(x) does not exist because the derivative of the function,
    # 1/x, is undefined at x = 0, which is the point a maclaurin series centers around
    # the log must be shifted to the left or right to fix this issue
    if calcMenu == 6:
        try: 
            result = math.log1p(num)
            while computedResult <= result - 0.00001 or computedResult >= result + .00001:
                # maclaurin for ln(1+x)
                computedResult += ((-1) ** (n + 1)) * (num ** n) / n
                n += 1

            print("*"*line)
            print(f"ln(1 + {num}) =", computedResult)
        # ln(0) is undefined
        except ValueError:
            print(und)

    elif calcMenu == 7:
        try:
            result = math.log(1-num)
            while computedResult <= result - 0.00001 or computedResult >= result + .00001:
                # maclaurin for ln(1-x)
                computedResult += -(num ** n) / n
                n += 1
            
            print("*"*line)
            print(f"ln(1 - {num}) =", computedResult)
        # ln(0) is undefined
        except ValueError:
            print(und)

    return n

# easily alter list of available functions
def FunctionList():
    print("Function Menu")
    print("~"*line)
    print("Trigonometric Function Expansions:\
           \n1. sin x\
           \n2. cos x\
           \n3. tan x\
           \n4. arcsin x\
           \n5. arccos x\
           \n6. arctan x")
    print("~"*line)
    print("*"*line)
    print("Growth and Decay Function Expansions:\
           \n7. e^x\
           \n8. ln (1 + x)\
           \n9. ln (1 - x)\
           \n10. ln[(1+x)/(1-x)]")
    print("*"*line)
    print("^"*line)
    print("Geometric Series Expansions:\
           \n11. 1/(1-x)\
           \n12. 1/(1-x)^2\
           \n13. 1/(1-x)^3")
    print("^"*line)
    print("To return to the Main Menu, enter Q.")

def ShowInfo():
    print("-"*line)
    print("In this application, several functions are available to you,\
           \nand the program calculates the answer by the function's\
           \nMaclaurin expansion and the built-in functions of the math library.\
           \n\
           \nAt the end of the calculations, the program will determine how\
           \nmany terms the Maclaurin series needs to reach the correct answer.\
           \n\
           \nValid syntax for inputs is shown below:\
           \nTo enter unit of angle, type 'deg' for degree or 'rad' for radian.\
           \nTo enter fractions, type the value in the form a/b.\
           \nTo use constants such as pi and e, type 'pi' or 'e'.\
           \n\
           \nAn example of inputting a radian value into a trigonometric function\
           \ncan look like this: 3 * pi / 4. The program will evaluate\
           \nthe result using order of operations.")

def ShowLearn():
    print("-"*line)
    print("The MacT Calculator uses material covered in Calculus II regarding\
           \nthe Taylor series of a function. The concept is named after the\
           \nEnglish mathematician Brook Taylor (1685-1731), who introduced\
           \nthe series in 1715.\
           \n\
           \nIn short, the Taylor series of a function is a polynomial of an\
           \ninfinite sum of terms expressed through the function's derivatives\
           \nat a single point. This means that for most common functions, the\
           \nfunction and the sum of its Taylor series are equal at that point.\
           \n\
           \nThe logic of this program uses a variation of the Taylor series,\
           \nwhere the point chosen is 0. This expansion is known as a Maclaurin\
           \nseries, named after the Scottish mathematican Colin Maclaurin (1698-1746).")

# dedication towards the guys who made this possible
def Special():
    print("-"*line)
    print("This program orignally began as an optional route for a Calculus II\
           \nproject, but I plan to integrate this into a framework and\
           \nproper web application.\
           \n\
           \nSpecial thanks to Antoine for designing some of the functions and\
           \ntheir Maclaurin series, as well as Alex and Quan for the numerous\
           \nstudy sessions we had during the semester. I could not have passed\
           \nCalculus without you guys!")

if __name__ == '__main__':
    main()