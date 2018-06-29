//https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

/*
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

NOTE: A more optimal solution would be to iterate from backwards to forwards through the string and record each word backwards, so that you don't have to iterate through each word twice as you do going forwards through string

Diagramming

"Let's take LeetCode contest"
 ^    ^
       ^   ^
            ^       ^
                     ^     ^
*/

var reverseWords = function(s) {
    start = 0
    for (var i = 1; i < s.length; i++){
      if (s[i] == " " || i == s.length - 1){
        //If you are running this because you've reached the end of the string and not the space following a word, you have to increment i because slice is non-inclusive on the endpoint and otherwise won't grab the entire last word
        if (i == s.length - 1){
          i++
        }
        current = ""
        for (var j = i - 1; j >= start; j--){
          current += s[j]
        }
        //Replaces the current words with its backwards counterpart and fits the rest of the existing string around it
        s = s.slice(0, start) + current + s.slice(i)
        //Because you're currently on an empty space and you are given that there are no extra spaces, you know there is a non-space character following the current space you are looking at, so you set start to that next character
        start = i + 1
      }
    }
    return s
};

sampleString = "Let's take LeetCode contest"
console.log(reverseWords(sampleString))
