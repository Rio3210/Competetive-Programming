class Solution(object):
    def sortSentence(self, s):
        word = s[::-1].split()
        result = []
        for word in sorted(word):
            result.append(word[1:][::-1]) 
        return ' '.join(result)
       
                
        
