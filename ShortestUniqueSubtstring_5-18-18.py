#This was an interview question for Pramp
#Below is the description

"""

Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:
input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"

"""

#Below shows how I first imagined my code working
#NOTE: I pretty much did what I imagined, except start became "minIndex" and held the index of the lowest character, and the "end" wasn't necessary

#"xyyzyzyx"
#{x:0, start:"x", end:"x"}

#{x:0, y:2, z:3, start:"x", end:"z"}
#solution = (3 - 0) + 1 = 4

#{x:0, y:4, z:3, start:"x", end:"y"}
#length not less than solution

#{x:0, y:4, z:5, start:"x", end:"z"}
#length not less than solution

#{x:0, y:6, z:5, start:"x", end:"y"}
#length not less than solution

#{x:7, y:6, z:5, start:"z", end:"x"}
#length less than solution

#Three main steps
#1 See if there is a character match between the string and the array
#2 Add that character to strObject or update its position, and maybe update "minIndex"
#3 If all array characters have been found, record substring if its length is less than current

#NOTE: Main pseudocode is at the bottom

def get_shortest_unique_substring(arr, str):
  strObject = {}
  solution = ""
  #Iterate forwards through the string, checking at each character whether or not it is one of the designated characters in the array
  for strIndex in range(0, len(str)):
    for arrIndex in range(0, len(arr)):
      if (str[strIndex] == arr[arrIndex]):
        #If the character matches the only one character in the array, then we can exit early because we know that the optimal substring is simply that one character
        if (len(arr) == 1):
          return str[strIndex]
        else:
          #We create an object like the one shown above; if it's the first key we are adding to the dictionary, we also add a "minIndex" key to track the key that appears earliest in the string
          strObject[str[strIndex]] = strIndex
          if (len(strObject) == 1):
            strObject["minIndex"] = strIndex
          #If we get a duplicate of the same character that used to be our "minIndex" character, we iterate through all of the keys in our strObject to see what the new "minIndex" is; we reInitialize "minIndex" with our current key because we know the real minimum will be less than that
          elif (str[strIndex] == str[strObject["minIndex"]]):
            strObject["minIndex"] = strIndex
            for character in strObject:
              if (strObject[character] < strObject["minIndex"]):
                strObject["minIndex"] = strObject[character]
          #If the length our strObject = the length of the given array + 1 (the +1 is because of the "minIndex" key), then we know we have a plausible solution, and if the distance between "minIndex" and what we are currently looking at is either the first real solution or the smallest plausible solution, we replace our current solution with it
          if (len(strObject) == len(arr) + 1):
            if (solution == "" or strIndex - strObject["minIndex"] < len(solution)):
              solution = str[strObject["minIndex"]:strIndex + 1]
  return solution

sampleArray = ["A","B","C"]
sampleString = "ADOBECODEBANCDDD"
print(get_shortest_unique_substring(sampleArray, sampleString))

#Create an object with each of the characters as keys and positions as values, initialized with each value at False
#Initialize the solution string as ""
#Iterate through the string, checking if the character matches a character in the dictionary
    #If it matches a character in the dictionary
        #Update the dictionary value
        #If all of the characters in the dictionary are something other than False
            #If the length between the lowest index and the highest index is equal to the array's length
                #return that subtstring
            #Else if the length between the lowest index and the highest index is less than the length of the currently recorded solution, or the solution is an empty string
                #solution = that new substring
#Return solution after outer loop is complete
