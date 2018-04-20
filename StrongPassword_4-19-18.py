#https://www.hackerrank.com/challenges/strong-password/problem

def minimumNumber(n, password):
    # Assuming a minimum length of 6 characters for a strong password, return the minimum number of characters to make the password strong
    requirementsArray = ["0123456789", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "!@#$%^&*()-+"]
    minimumLength = 6

    for letter in password:
        #IterationDone simply keeps track of whether the letter we are looking at matches one of the characters in the requirements array; if we did find a match, we can break all other loops because we know that if the letter matches a character in one of the requirements, it doesn't match the other due to mutual exclusivity
        iterationDone = False;
        for requirement in requirementsArray:
            if (iterationDone == True):
                break;
            #Note: I could have used a "if letter in requirement" kind of python syntax here, but this works just as well
            for char in requirement:
                if (letter == char):
                    requirementsArray.remove(requirement)
                    iterationDone = True
                    break;
    requirementsNotMet = len(requirementsArray)
    #If the number of requirements left is greater than the characters needed to reach the minimum length, return the number of requirements because one character is needed to meet each outstanding requirement; otherwise, return the number of characters necessary to reach the minimum length
    if (minimumLength - n > requirementsNotMet):
        return minimumLength - n
    else:
        return len(requirementsArray)

print(minimumNumber(8, "E1$EEEE"))
