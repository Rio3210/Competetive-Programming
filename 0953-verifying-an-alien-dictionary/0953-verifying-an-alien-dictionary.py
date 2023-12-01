class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        ordd = {}
        for i, st in enumerate(order):
            ordd[st] = i
        
        for w in range(1, len(words)):
            word1 = words[w - 1]
            word2 = words[w]
        
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if ordd[word1[i]] > ordd[word2[i]]:
                        return False  
                    break  
            else:
                if len(word1) > len(word2):
                    return False  
        
        return True  