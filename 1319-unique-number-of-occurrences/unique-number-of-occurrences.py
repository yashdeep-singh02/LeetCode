class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Dict={}
        for i in arr:
            if i in Dict:
                Dict[i]+=1
            else:
                Dict[i]=1

        return len(Dict)==len(set(Dict.values()))
        

        