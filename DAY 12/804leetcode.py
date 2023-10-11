class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique =set()
        for i in words:
            s = ""
            for letter in i:
                s+=letters[ord(letter) - ord('a')]
            unique.add(s)
        print(unique)
        return len(unique)
            
        