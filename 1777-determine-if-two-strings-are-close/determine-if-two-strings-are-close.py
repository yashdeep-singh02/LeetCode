class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1, dict2={},{}
    
        if len(word1)!=len(word2):
            return False
        count=0
        for c in word1:
            if c in dict1:
                dict1[c]+=1
            else:
                dict1[c]=1
        
        for c in word2:
            if c in dict2:
                dict2[c]+=1
            else:
                dict2[c]=1
        
        for c in dict1:
            if c not in dict2:
                return False
        
        return Counter(dict1.values())==Counter(dict2.values())
        