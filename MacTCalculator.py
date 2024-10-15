import os
import math
clear = lambda: os.system('clear')

pi = 3.14159265359
# divide menu sections
line = 70
trig = 35
eX = 35

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
            try:
                num = Constant(Convert(input('Enter your desired value (sin x): ')))
                type = str(input('Enter the unit of angle (deg or rad): '))
            except ValueError:
                print('Error ... Invalid input. Try again.')
            except ZeroDivisionError:
                print('Error ... Attempted division by zero. Try again.')
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                sin(num, type, 0)
            else:
                print('Error ... Invalid unit of angle. Try again.')

        elif calcMenu == 2:
            try:
                num = input('Enter your desired value (cos x): ')
                num = Convert(num)
                type = str(input('Enter the unit of angle (deg or rad): '))
            except ValueError:
                print('Error ... Invalid input. Try again.')
            except ZeroDivisionError:
                print('Error ... Attempted division by zero. Try again.')
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                cos(num, type, 0)
            else:
                print('Error ... Invalid unit of angle. Try again.')

        elif calcMenu == 3:
            try:
                num = input('Enter your desired value (tan x): ')
                num = Convert(num)
                type = str(input('Enter the unit of angle (deg or rad): '))
            except ValueError:
                print('Error ... Invalid input. Try again.')
            except ZeroDivisionError:
                print('Error ... Attempted division by zero. Try again.')
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                tan(num, type)
            else:
                print('Error ... Invalid unit of angle. Try again.')

        elif calcMenu == 4:
            try:
                num = input('Enter your desired value (arctan x): ')
                num = Convert(num)
                type = str(input('Enter the unit of angle (deg or rad): '))
            except ValueError:
                print('Error ... Invalid input. Try again.')
            except ZeroDivisionError:
                print('Error ... Attempted division by zero. Try again.')
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                arctan(num, type)
            else:
                print('Error ... Invalid unit of angle. Try again.')

        elif calcMenu == 5:
            try:
                num = input('Enter your desired value (e^x): ')
                num = Convert(num)
            except ValueError:
                print('Error ... Invalid input. Try again.')
            except ZeroDivisionError:
                print('Error ... Attempted division by zero. Try again.')
            e(num)
            
        elif calcMenu == 6 or calcMenu == 7:
            try:
                num = input('Enter your desired value (ln 1 ± x): ')
                num = Convert(num)
            except ValueError:
                print('Error ... Invalid input. Try again.')
            except ZeroDivisionError:
                print('Error ... Attempted division by zero. Try again.')
            ln(num, calcMenu)

        elif calcMenu == 8:
            print('Returning to Main Menu ...')

#The trig functions take a number then the unit of that number "rad" or "deg" after a comma
# Ex sin(45,"deg"), tan(pi/3,"rad")

#function for sin 
def sin (num, type, n):
    #create values to compare or add too
    computed_result = 0.0
    n = 0
    if type == "deg":
        num = (num * pi)/180
    #Used only to get comparable result
    result = math.sin(num)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += ((-1) ** n) * (num ** (2 * n+1))/math.factorial(2 * n+1)
        n += 1

    print("~"*trig)
    print(f"\nsin({num}) =", computed_result)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")
    
    return computed_result, n

def cos(num, type, n):
    #create values to compare or add too
    computed_result = 0.0
    n = 0
    if type == "deg":
        num = (num * pi)/180
    result = math.cos(num)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += ((-1) ** n) * (num ** (2 * n))/math.factorial(2 * n)
        n += 1

    print("~"*trig)
    print(f"\ncos({num}) =", computed_result)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")

    return computed_result, n

def tan(num, type):
    #create values to compare or add too
    n = 0
    # deg to rad conversion is not included as it is done in the sin and cos functions
    result = math.tan(num)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result = sin(num, type, n) / cos(num, type, n)
        n += 1

    print("~"*trig)
    print(f"\ntan({num}) =", computed_result)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")

def arctan(num, type):
    computed_result = 0.0
    n = 0
    if type == "deg":
        num = (num * pi)/180
    #Used only to get comparable result
    result = math.atan(num)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += ((-1) ** n) * (num ** (2 * n+1)) / (2 * n+1)
        n += 1 

    print("~"*trig)
    print(f"\narctan({num}) =", computed_result)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")
    
def e(num):
    computed_result = 0.0
    n = 0
    #Used only to get comparable result 
    result = math.e**(num)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += (num**(n))/math.factorial(n)
        n += 1

    print("*"*eX)
    print(f"\ne^{num} =", computed_result)
    print(f"After {n} term(s) of its Maclaurin expansion it is less than\
            \nor equal to the correct answer, within a 0.00001 ERROR")

def ln(num, calcMenu):
    computed_result = 0.0
    n = 1
    if calcMenu == 6:
        #Used only to get comparable result 
        result = math.log1p(num)
        while computed_result <= result - 0.00001 or computed_result >= result + .00001:
            computed_result += ((-1) ** (n + 1)) * (num ** n) / n
            print(computed_result)
            n += 1

        print("*"*eX)
        print(f"\nln(1 + {num}) =", computed_result)
        print(f"After {n} term(s) of its Maclaurin expansion it is less than\
                \nor equal to the correct answer, within a 0.00001 ERROR")

    elif calcMenu == 7:
        result = math.log(1-num)
        while computed_result <= result - 0.00001 or computed_result >= result + .00001:
            computed_result += -(num ** n) / n
            print(computed_result)
            n += 1
        
        print("*"*eX)
        print(f"\nln(1 - {num}) =", computed_result)
        print(f"After {n} term(s) of its Maclaurin expansion it is less than\
                \nor equal to the correct answer, within a 0.00001 ERROR")

# let user input fractions and convert to actual values
def Convert(num):
    if '/' not in str(num):
        return float(num)
    else:
        fract = num.split('/')
        return float(fract[0])/float(fract[1])

# these two functions ^ v have to be merged somehow to allow for fractions to work as well as "pi" be recognized as an input

def Constant(num):
    constants = {"pi": pi, "e": 2.718281828}
    if num in constants:
        return constants[num]
    else:
        return float(num)

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
           \nproject, but I plan to integrate this into a framework\
           \n and proper web application.\
           \n\
           \nSpecial thanks to Antoine for designing some of the functions\
           \nand their Maclaurin series, and Alex for the numerous study\
           \nsessions we had during the semester. I could not have\
           \npassed Calculus without you guys!")

if __name__ == '__main__':
    main()