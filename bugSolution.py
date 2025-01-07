def function_with_uncommon_bug_solution(x):
    if x == 0:
        return 0  # Correct handling of x == 0
    elif x > 0:
        return 1 / x # No error here since x>0
    else:
        return -1 #Correct handling of x<0

# This improved version checks for x==0 explicitly before the division, eliminating the potential ZeroDivisionError