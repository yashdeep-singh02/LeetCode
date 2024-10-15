class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        current_sum=sum(arr[:k])
        target=k*threshold
        if current_sum>=target:
            count+=1
        for i in range(k,len(arr)):
           current_sum += arr[i] - arr[i - k]
           if current_sum>=target:
                count+=1 
        
        return count