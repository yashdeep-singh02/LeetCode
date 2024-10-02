class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n==1:
            arr[0]=-1
            return arr

        max = arr[-1]
        i = n-1

        while i >= 0:
            if i==n-1:
                arr[i] = -1
            else:
                 temp = arr[i]
                 arr[i]=max
                 if(temp>max):
                    max = temp
           
            i-=1

        return arr
        