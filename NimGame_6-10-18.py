#leetcode
#https://leetcode.com/problems/nim-game/description/



#4 stones left and it's your turn

#3 You lose
#2 You lose
#1 You lose
#NOTE: You are playing optimally, but none of those options get you a win, so you lose

#5 stones left and it's your turn

#4 You win, no matter what your opponent does (you choose this one out of the three options because you are playing optimally, and this option wins for the same reason you were shown to lose if you start with 4 stones, as shown above)
#3 You lose
#2 You lose

#6 stones left and it's your turn

#5 You lose
#4 You win
#3 You lose

#7 stones left and it's your turn

#6 You lose
#5 You lose
#4 You win

#8 stones left and it's your turn

#7 You lose
#6 You lose
#5 You lose


"""
Whoever is left with the stones at a multiple of 4 at any time in the game loses.  As long as you don't start on a multiple of 4, you win because you can force your opponent down to a multiple of 4 instead; whoever can be left with 4 loses because the opponent can simply keep countering to force them to stay there.  For example:

1.) If you start with 11, you can take 3 and opponent is at 8, a 4-multiple
If opponent takes 3 and goes to 5, you can take 1 and he is forced to 4
If opponent takes 2 and goes to 6, you can take 2 and he is forced to 4
If opponent takes 1 and goes to 7, you can take 3 and he is forced to 4

2.)However, if you start with 8
If you take 1 and go to 7, your opponent takes 3 and you are forced to 4
If you take 2 and go to 6, your opponent takes 2 and you are forced to 4
If you take 3 and go to 5, your opponent takes 1 and you are forced to 4
"""

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n % 4 == 0):
            return False
        else:
            return True
