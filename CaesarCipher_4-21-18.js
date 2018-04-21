//https://www.hackerrank.com/challenges/caesar-cipher-1/problem

//Note: Although most algorithms thus far have been done in Python, this one was done in JS as a refresher for me

function caesarCipher(s, k) {
    var alphabet = "abcdefghijklmnopqrstuvwxyz"
    var doubleAlphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    var rotation = k % 26
    var modifiedAlphabet = doubleAlphabet.substring(0 + rotation, rotation + 26)
    var solutionString = ""
    var lowerCase = s.toLowerCase()
    //This function walks through each letter of the string, s, and if it's uppercase, records that in the upper variable.  Then, it finds which character of the alphabet it is, and if it was uppercase, translates the new letter from modifiedAlphabet into uppercase and adds it onto the solution string (otherwise just adds it as lowercase).  If the character wasn't in the alphabet, foundTranslation = false, so it just pushes the character in without any modifications.
    for (var i = 0; i < s.length; i++){
        var foundTranslation = false
        var upper = false
      if (s[i] == s[i].toUpperCase()){
        upper = true
      }
      for (var j = 0; j < alphabet.length; j++){
        if (lowerCase[i] == alphabet[j]){
          if (upper == true){
            solutionString += modifiedAlphabet[j].toUpperCase()
          }
          else{
            solutionString += modifiedAlphabet[j]
          }
          foundTranslation = true
          break;
        }
      }
      if (foundTranslation == false){
        solutionString += s[i]
      }
    }
    return solutionString;
}

console.log(caesarCipher("thE-Ace", 2))
