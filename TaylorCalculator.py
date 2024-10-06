import os
import math
clear = lambda: os.system('clear')

pi = 3.14159265359

# factorial function that takes a number as a parameter
def factorial (numby):
    sum = numby
    #loop goes the number of times as the parameter
    if numby == 0:
        sum = 1
        return sum
    for value in range(numby):
        #Value start at zero naturally so add one so it doesnt make it 0 times some number eternally 
        value = value + 1 
        if value == numby:
            break 
        sum *= value
    return sum

#function for sin 
def sin (numb, type):
    #create values to compare or add too
    computed_result = 0.0
    n = 0
    if type == "deg":
        numb = (numb * pi)/180
    #Used only to get comparable result
    result = math.sin(numb)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += ((-1)**n)*(numb**(2*n+1))/factorial(2*n+1)
        n += 1

    print( computed_result, f"After {n} of terms it is within less than or equal to 0.00001 ERROR")
    return computed_result

def cos (numb, type):
    #create values to compare or add too
    computed_result = 0.0
    n = 0
    if type == "deg":
        numb = (numb * pi)/180
    result = math.cos(numb)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += ((-1)**n)*(numb**(2*n))/factorial(2*n)
        n += 1

    print (computed_result, f"After {n} of terms it is within less than or equal to 0.00001 ERROR")
    return computed_result

def tan (numb, type):
    #create values to compare or add too
    computed_result = sin(numb, type)[0] / cos(numb, type)[0]

    print(computed_result)
    return computed_result


def arctan (numb, type):
    computed_result = 0.0
    n = 0
    if type == "deg":
        numb = (numb * pi)/180
    #Used only to get comparable result
    result = math.atan(numb)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += ((-1)**n)*(numb**(2*n+1))/(2*n+1)
        n += 1 

    print( computed_result, f"After {n} of terms it is within less than or equal to 0.00001 ERROR")
    return computed_result

def e(numb):
    computed_result = 0.0
    n = 0
    #Used only to get comparable result 
    result = math.e**(numb)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += (numb**(n))/factorial(n)
        n += 1

    print(computed_result, f"After {n} of terms it is within less than or equal to 0.00001 ERROR")
    return computed_result

def ln(numb):
    computed_result = 0.0
    n = 1
    #Used only to get comparable result 
    result = math.log1p(numb-1)
    while computed_result <= result - 0.00001 or computed_result >= result + .00001:
        computed_result += (( -1 ) ** ( n + 1 )) * (( numb - 1 )**n)/n
        print(computed_result)
        n += 1
    
    print(computed_result, f"After {n} of terms it is within less than or equal to 0.00001 ERROR")
    return computed_result


#The trig functions take a number then the unit of that number "rad" or "deg" after a comma
# Ex sin(45,"deg"), tan(pi/3,"rad")

# DESIRED FUNCTION CAN GO BELOW HERE
print()
ln(1.5)