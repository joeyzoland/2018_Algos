"""
Given a string, such as ">><>", with an arrow indicating a soldier walking in that direction, and assuming that each soldier has to salute each time they cross the path of another soldier, calculate the number of salutes

In the case of the above, the answer would be 4, because the first two ">" cross the "<" in the third position / second index and thus both pairs have to salute, but the fourth position / third index never passes anyone going left, so the answer is just those 4

Numberof> = 0
NumberofSalutes = 0

Starting from the left, keep track of number of ">"

If we see a "<", add to the total number of salutes 2 * the number of ">"
"""

def salutes(string):
    rights = 0
    salutes = 0
    for char in string:
        if char == ">":
            rights += 1
        elif char == "<":
            salutes += rights * 2
    return salutes

sampleSalutes = ">><>"
print(salutes(sampleSalutes))
