class Solution:
    def sortInWave(self, arr):
        n = len(arr)
        for i in range(1, n):
            if i%2 != 0:
                if arr[i]<=arr[i-1]:
                    continue
                else:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
            else:
                if arr[i]>=arr[i-1]:
                    continue
                else:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
        

