"""
[(, [, {]
[), ], }]

{"}":"{", ")":"(", "]":"["}

Iterate through the input string, and if it's not in the map, add to the stack
    Else, check if the stack is empty or the top of the stack is the complement and, if it is, pop it off the stack; otherwise, return false
"""
