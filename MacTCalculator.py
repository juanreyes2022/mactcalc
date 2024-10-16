import os
import math
clear = lambda: os.system('clear')

pi = math.pi
# divide menu sections
line = 70
trig = 40
eX = 40

def main():
    playerName = input('Please enter your name to begin: ')
    print('Hello ' + str(playerName) + ', welcome to the MacT Calculator!')

    menu = 0
    while menu != 5:
        print("-"*line)
        print("Main Menu\
              \n1. Start the Calculator\
              \n2. Program Information\
              \n3. Learn about Taylor/Maclaurin series.\
              \n4. Dedication & Contributors\
              \n5. Quit.")
        
        menu = int(input("\nPlease select one of the options above: "))

        if menu == 1:
            Calc(playerName)
        elif menu == 2:
            ShowInfo()
        elif menu == 3:
            ShowLearn()
        elif menu == 4:
            Special()
        elif menu == 5:
            print('Shutting down ...\
                  \nGoodbye ' + str(playerName) + ', and thank you for using the MacT calculator.')
        else:
            print('\nError ... Invalid option. Try again.')

def Calc(playerName):
    calcMenu = 0
    while calcMenu != 8:
        computedResult = 0.0
        n = 0
        num = 0
        type = ' '
        print("-"*line)
        # easier way to alter list
        FunctionList()

        try:
            calcMenu = int(input('\n' + str(playerName) + ', please select one of the options above: '))
        except ValueError:
            print('Error ... Invalid selection. Try again.')

        if calcMenu in [1, 2, 3, 4]:
            print("~"*trig)
        elif calcMenu in [5, 6, 7]:
            print("*"*eX)
        
        if calcMenu == 1:
            num, type = Prompt(calcMenu, num, type)
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                sin(num, type, n, computedResult)
            elif type == ' ':
                continue
            else:
                print('Error ... Invalid unit of angle. Try again.')

        elif calcMenu == 2:
            num, type = Prompt(calcMenu, num, type)
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                cos(num, type, n, computedResult)
            elif type == ' ':
                continue
            else:
                print('Error ... Invalid unit of angle. Try again.')

        elif calcMenu == 3:
            num, type = Prompt(calcMenu, num, type)
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                tan(num, type, n, computedResult)
            elif type == ' ':
                continue
            else:
                print('Error ... Invalid unit of angle. Try again.')

        elif calcMenu == 4:
            num, type = Prompt(calcMenu, num, type)
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                arctan(num, type, n, computedResult)
            elif type == ' ':
                continue
            else:
                print('Error ... Invalid unit of angle. Try again.')

        elif calcMenu == 5:
            num, type = Prompt(calcMenu, num, type)
            if type == ' ':
                e(num, n, computedResult)
            
        elif calcMenu == 6 or calcMenu == 7:
            num, type = Prompt(calcMenu, num, type)
            if type == ' ':
                ln(num, calcMenu, n, computedResult)

        elif calcMenu == 8:
            print('Returning to Main Menu ...')

def Prompt(calcMenu, num, type):
    try:
        num = eval(input('Enter your desired value: '))
        if calcMenu in [1, 2, 3, 4]:
            type = input('Enter the unit of angle (deg or rad): ')
    except ValueError:
        print('Error ... Invalid input. Try again.')
    except ZeroDivisionError:
        print('Error ... Attempted division by zero. Try again.')
        if calcMenu in [5, 6, 7]:
            type = 0

    return num, type

#The trig functions take a number then the unit of that number "rad" or "deg" after a comma
# Ex sin(45,"deg"), tan(pi/3,"rad")

#function for sin 
def sin (num, type, n, computedResult):

    if type == "deg":
        num = (num * math.pi)/180
    #Used only to get comparable result
    result = math.sin(num)
    while computedResult <= result - 0.00001 or computedResult >= result + .00001:
        computedResult += ((-1) ** n) * (num ** (2 * n+1))/math.factorial(2 * n+1)
        n += 1

    print("~"*trig)
    print(f"sin({num}) =", computedResult)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")
    
    return n, computedResult

def cos(num, type, n, computedResult):
    if type == "deg":
        num = (num * math.pi)/180
    result = math.cos(num)
    while computedResult <= result - 0.00001 or computedResult >= result + .00001:
        computedResult += ((-1) ** n) * (num ** (2 * n))/math.factorial(2 * n)
        n += 1

    print("~"*trig)
    print(f"cos({num}) =", computedResult)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")

    return n, computedResult

def tan(num, type, n, computedResult):
    # deg to rad conversion is not included as it is done in the sin and cos functions
    result = math.tan(num)
    try:
        while computedResult <= result - 0.00001 or computedResult >= result + .00001:
            computedResult = tuple(x / y for x, y in zip(sin(num, type, n), cos(num, type, n)))
            n += 1

        print("~"*trig)
        print(f"tan({num}) =", computedResult)
        print(f"After {n} term(s) of its Maclaurin expansion it is less than\
                \nor equal to the correct answer, within a 0.00001 ERROR")

    except ZeroDivisionError:
        print('The result is undefined.')

    return n, computedResult

def arctan(num, type, n, computedResult):
    if type == "deg":
        num = (num * math.pi)/180
    #Used only to get comparable result
    result = math.atan(num)
    while computedResult <= result - 0.00001 or computedResult >= result + .00001:
        computedResult += ((-1) ** n) * (num ** (2 * n+1)) / (2 * n+1)
        n += 1 

    print("~"*trig)
    print(f"arctan({num}) =", computedResult)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")
    
def e(num, n, computedResult):
    #Used only to get comparable result 
    result = math.e**(num)
    while computedResult <= result - 0.00001 or computedResult >= result + .00001:
        computedResult += (num**(n))/math.factorial(n)
        n += 1

    print("*"*eX)
    print(f"e^{num} =", computedResult)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")

def ln(num, calcMenu, n, computedResult):
    n = 1
    if calcMenu == 6:
        try: 
            result = math.log1p(num)
            while computedResult <= result - 0.00001 or computedResult >= result + .00001:
                computedResult += ((-1) ** (n + 1)) * (num ** n) / n
                n += 1

            print("*"*eX)
            print(f"ln(1 + {num}) =", computedResult)
            print(f"After {n} term(s) of its Maclaurin expansion it is less than\
                    \nor equal to the correct answer, within a 0.00001 ERROR")
        
        except ValueError:
            print('The result is undefined.')

    elif calcMenu == 7:
        try:
            result = math.log(1-num)
            while computedResult <= result - 0.00001 or computedResult >= result + .00001:
                computedResult += -(num ** n) / n
                n += 1
            
            print("*"*eX)
            print(f"ln(1 - {num}) =", computedResult)
            print(f"After {n} term(s) of its Maclaurin expansion it is less than\
                    \nor equal to the correct answer, within a 0.00001 ERROR")

        except ValueError:
            print('The result is undefined.')

# separate function if more math functions added
def FunctionList():
    print("Function Menu")
    print("~"*trig)
    print("Trigonometric Function Expansions:\
           \n1. Sine\
           \n2. Cosine\
           \n3. Tangent\
           \n4. Arctangent")
    print("~"*trig)
    print("*"*eX)
    print("Growth and Decay Function Expansions:\
           \n5. Euler's Number (e)\
           \n6. Natural Logarithm (1 + x)\
           \n7. Natural Logarithm (1 - x)")
    print("*"*eX)
    print("To return to the Main Menu, enter 8.")

def ShowInfo():
    print("-"*line)
    print("In this application, several functions are available to you,\
           \nand the program calculates the answer by the function's\
           \nMaclaurin expansion and the built-in functions of the math library.\
           \n\
           \nAt the end of the calculations, the program will determine how\
           \nmany terms the Maclaurin series needs to reach the correct answer.\
           \n\
           \nEach function will require the user to input a value to calculate,\
           \nbut the trigonometric functions require you to specify if\
           \nthe unit is degrees or radians. The syntax for entering the angle is\
           \n\"deg\" or \"rad\".\
           \n\
           \nTo enter fractions, the proper syntax is shown: a/b.")


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