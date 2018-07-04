"""
Find shortest substring that contains all letters, and note that there can be duplicates
Ideal solution should use sliding window, with different behavior depending on whether the letter is a target letter or not

"ZZZZZZZADOBAAECODEBANC", "ABC"
           s
               f

Allowed duplicates in final result

{
A: 0
B: 3
C: 5
}


-9

[5, 1, 0, 0, 0, -10, 7]
                  s
                  f

=> "BCCCCCA", "ABC"
=>
"""

def shortestUniqueSubstring(string, substring):
    hashMap = {}
    windowComplete = False
    result = -1
    #The below creates a frequency hash map, something like {a:2, b:1} out of the substring "aab"
    for i in range(0, len(substring)):
        if substring[i] not in hashMap:
            hashMap[substring[i]] = 1
        else:
            hashMap[substring[i]] += 1
    start = 0
    #The below modifies the existing hash map, tracking how many characters you are away from having all of the substring characters in your window
    for i in range(0, len(string)):
        if string[i] in hashMap:
            hashMap[string[i]] -= 1
            if windowComplete == False:
                #If we just subtracted a frequency requirement off of our hash map, and we have not yet had a window that meets all of our requirements, then we have to check if our widnow now meets all of our requirements, such that our hashMap frequencies are all now 0 or less
                doneCheck = True
                for key in hashMap:
                    if hashMap[key] > 0:
                        doneCheck = False
                        break
                if doneCheck == True:
                    windowComplete = True
            #If we know our window contains all the substring characters, then we need to check if we can move the start pointer to the right
            if windowComplete == True:
                for j in range(start, i):
                    #If the character in question is not a special character, then we know we can move the pointer
                    if string[j] not in hashMap:
                        start += 1
                    #If the character in question is a special character, but its frequency in the hash map is negative, then we know we have at least one more of the character in the window than necessary, so we update our map and increment the pointer past it
                    elif hashMap[string[i]] < 0:
                        hashMap[string[i]] += 1
                        start += 1
                    else: #IF the character is in hashMap and is necessary for the window to contain the substring, than we should increment no longer
                        break
                #If the length from start to finish is less than the result, or there has been no result yet, then update result
                if i - start + 1 < result or result == -1:
                    result = i - start + 1
    return result



sampleString = "codebancdc"
sampleSubstring = "abcc"
print(shortestUniqueSubstring(sampleString, sampleSubstring))
