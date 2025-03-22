class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f1,f2=[],[]
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                f1+=[i]
                f2+=[n//i]
        if f1[-1]==f2[-1]: f2.pop()

        factors = f1 + f2[::-1]

        return -1 if len(factors)<k else factors[k-1]

        