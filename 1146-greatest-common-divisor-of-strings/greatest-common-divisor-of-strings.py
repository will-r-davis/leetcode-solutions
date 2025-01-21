class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def validateGcd(gcd: str, str: str):
            if len(str) % len(gcd) != 0:
                return False
            for i in range(0, len(str), len(gcd)):
                if str[i:i+len(gcd)] != gcd:
                    return False
            return True

        (shrt, lng) = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        gcd = shrt
    
        while len(gcd) > 0:
            if validateGcd(gcd, shrt) and validateGcd(gcd, lng):
                return gcd
            else:
                gcd = gcd[0:-1]
        return gcd