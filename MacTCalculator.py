import os
import math
clear = lambda: os.system('clear')

pi = 3.14159265359

def main():
    playerName = input('Please enter your name to begin: ')
    print('Hello', playerName,', welcome to the MacT Calculator!')

    menu = 0
    while menu != 4:
        print("-"*35)
        print("Main Menu\
              \n1. Start the Calculator\
              \n2. Learn about Taylor/Maclaurin series.\
              \n3. Dedication & Contributors\
              \n4. Quit.")
        
        menu = int(input("\nPlease select one of the options above: "))

        if menu == 1:
            Calc(playerName)
        elif menu == 2:
            ShowInfo()
        elif menu == 3:
            Special()
        elif menu == 4:
            print('\nGoodbye. Thank you for using the Taylor calculator.')
        else:
            print('\nError ... Invalid option. Try again.')

def Calc(playerName):
    calcMenu = 0
    while calcMenu != 8:
        print("-"*35)
        print(playerName, 'here is a list of all available functions.')
        # easier way to alter list
        FunctionList()
        
        calcMenu = int(input("\nPlease select one of the options above: "))
        
        if calcMenu == 1:
            num = float(input('\nEnter your desired value: '))
            type = str(input('\nEnter the unit of angle (deg or rad): '))
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                sin(num, type)
            else:
                print('Error ... Invalid input. Try again.')

        elif calcMenu == 2:
            num = float(input('\nEnter your desired value: '))
            type = str(input('\nEnter the unit of angle (deg or rad): '))
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                cos(num, type)
            else:
                print('Error ... Invalid input. Try again.')

        elif calcMenu == 3:
            num = float(input('\nEnter your desired value: '))
            type = str(input('\nEnter the unit of angle (deg or rad): '))
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                tan(num, type)
            else:
                print('Error ... Invalid input. Try again.')

        elif calcMenu == 4:
            num = float(input('\nEnter your desired value: '))
            type = str(input('\nEnter the unit of angle (deg or rad): '))
            # user's string input only allows for degree and radian units
            if type in ["deg", "rad"]:
                arctan(num, type)
            else:
                print('Error ... Invalid input. Try again.')

        elif calcMenu == 5:
            num = float(input('\nEnter your desired value: '))
            e(num)
            
        elif calcMenu == 6 or calcMenu == 7:
            num = float(input('\nEnter your desired value: '))
            ln(num, calcMenu)

        elif calcMenu == 8:
            print('Returning to Main Menu...')
        else:
            print('Error ... Invalid selection. Try again.')

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

    print(f"sin({num}) =", computed_result, f". After {n} terms of its\
          \nMaclaurin expansion it is less than or equal to the correct\
          \nanswer, within a 0.00001 ERROR")
    
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

    print(f"cos({num}) =", computed_result, f". After {n} terms of its\
          \nMaclaurin expansion it is less than or equal to the correct\
          \nanswer, within a 0.00001 ERROR")

    return computed_result, n

def tan(num, type):
    #create values to compare or add too
    n = 0
    result = math.tan(num)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result = sin(num, type, n) / cos(num, type, n)
        n += 1

    print(f"tan({num}) =", computed_result, f". After {n} terms of its\
          \nMaclaurin expansion it is less than or equal to the correct\
          \nanswer, within a 0.00001 ERROR")

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

    print(f"arctan({num}) =", computed_result, f". After {n} terms of its\
          \nMaclaurin expansion it is less than or equal to the correct\
          \nanswer, within a 0.00001 ERROR")
    
def e(num):
    computed_result = 0.0
    n = 0
    #Used only to get comparable result 
    result = math.e**(num)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += (num**(n))/math.factorial(n)
        n += 1

    print(f"e^{num} =", computed_result, f". After {n} terms of its\
          \nMaclaurin expansion it is less than or equal to the correct\
          \nanswer, within a 0.00001 ERROR")

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
        
        print(f"ln(1 + {num}) =", computed_result, f". After {n} terms of its\
          \nMaclaurin expansion it is less than or equal to the correct\
          \nanswer, within a 0.00001 ERROR")

    elif calcMenu == 7:
        result = math.log(1-num)
        while computed_result <= result - 0.00001 or computed_result >= result + .00001:
            computed_result += -(num ** n) / n
            print(computed_result)
            n += 1
        
        print(f"ln(1 - {num}) =", computed_result, f". After {n} terms of its\
          \nMaclaurin expansion it is less than or equal to the correct\
          \nanswer, within a 0.00001 ERROR")

# separate function if more math functions added
def FunctionList():
    print("\nFunction Menu\
           \n\
           \nTrigonometric Function Expansions:\
           \n1. Sine\
           \n2. Cosine\
           \n3. Tangent\
           \n4. Arctangent\
           \n\
           \nGrowth and Decay Function Expansions:\
           \n5. Euler's Number (e)\
           \n6. Natural Logarithm (1 + x)\
           \n7. Natural Logarithm (1 - x)\
           \n8. Return to Main Menu")

def ShowInfo():
    print("-"*35)
    print("\nThe MacT Calculator uses material covered in Calculus II\
           \nregarding the Taylor series of a function. The concept is\
           \nnamed after the English mathematician Brook Taylor (1685\
           \n-1731), who introduced the series in 1715.\
           \n\
           \nIn short, the Taylor series of a function is a polynomial of\
           \nan infinite sum of terms expressed through the function's\
           \nderivatives at a single point. This means that for most\
           \ncommon functions, the function and the sum of its Taylor\
           \nseries are equal at that point.\
           \n\
           \nThe logic of this program uses a variation of the Taylor\
           \nseries, where the point chosen is 0. This expansion is known\
           \nas a Maclaurin series, named after the Scottish mathematican\
           \nColin Maclaurin (1698-1746).\
           \n\
           \nIn this application, several functions are available to you,\
           \nand the program calculates the answer by the function's\
           \nMaclaurin expansion and the built-in functions of the math library.\
           \n\
           \nAt the end of the calculations, the program will determine how\
           \nmany terms the Maclaurin series needs to reach the correct answer.")
    
def Special():
    print("-"*35)
    print("\nThis program orignally began as an optional route for\
           \na Calculus II project, but I plan to integrate this\
           \ninto a framework and proper web application.\
           \n\
           \nSpecial thanks to Antoine for designing some of\
           \nthe functions and their Maclaurin series, and Alex\
           \nfor the numerous study sessions we had when reaching\
           \nthe \"Infinite Series\" section. I could not have\
           \npassed Calculus without you guys!")

if __name__ == '__main__':
    main()