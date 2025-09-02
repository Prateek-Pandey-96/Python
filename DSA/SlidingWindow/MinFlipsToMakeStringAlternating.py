class Solution:
    def getFlips(self, s, possibility):
        count = 0
        n = len(s)//2
        for i in range(n):
            if possibility[i]!=int(s[i]):
                count += 1
        
        flips = count
        for i in range(n, 2*n):
            if possibility[i]!=int(s[i]):
                count += 1
            if possibility[i-n]!=int(s[i-n]):
                count -= 1
            flips = min(flips, count)
        return flips

    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s

        possibility1 = [0]*(2*n)
        for i in range(0, 2*n, 2):
            possibility1[i] = 1
        
        possibility2 = [0]*(2*n)
        for i in range(1, 2*n, 2):
            possibility2[i] = 1

        flips1 = self.getFlips(s, possibility1)
        flips2 = self.getFlips(s, possibility2)
        
        return min(flips1, flips2)
        

