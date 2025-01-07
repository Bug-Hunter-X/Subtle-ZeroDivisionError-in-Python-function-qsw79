def function_with_uncommon_bug(x):
    if x == 0:
        return 0  # Correct handling of x == 0
    elif x > 0:
        return 1 / x # Potential ZeroDivisionError if x is not correctly checked
    else:
        return -1 #Correct handling of x < 0

#The bug is subtle.It might work correctly for most inputs, but if the function receives a value of 0 for the parameter x, it will return 0 correctly. However, if x is a very small negative number (close to zero), it may raise a ZeroDivisionError.