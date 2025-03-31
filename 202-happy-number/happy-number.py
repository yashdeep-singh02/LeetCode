class Solution:
    def isHappy(self, n: int) -> bool:
        seen =set()

        def get_next(num):
            n=0
            for digit in str(num):
                n+=int(digit)**2

            return n
        
        while n!=1 and n not in seen:
            seen.add(n)
            n=get_next(n)


        return n==1


        
        