# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A , B = len(word1), len(word2)
        i,j = 0,0
        word = ""

        while i <= A-1 or j <= B-1:
            if i <= A-1:
                word += word1[i]
                i+=1
            
            if j <= B-1 :
                word += word2[j]
                j+=1

        return word
