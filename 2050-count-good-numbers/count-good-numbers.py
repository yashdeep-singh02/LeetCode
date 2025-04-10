class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        power = n // 2
        result = pow(20, power, MOD)
        
        if n % 2 == 1:
            result = (result * 5) % MOD
        
        return result