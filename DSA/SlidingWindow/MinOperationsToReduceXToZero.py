class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i, j, n = 0, 0, len(nums)
        running_sum = 0
        operations = float("inf")
        
        while j < 2*n:
            running_sum += nums[j%n]

            while running_sum > x:
                running_sum -= nums[i%n]
                i += 1

            if running_sum == x and (i==0 or j==n-1 or (i <= n-1 and j>= n-1)):
                operations = min(operations, j-i+1)
            j += 1
        
        return operations if (operations != float("inf") and operations <= n) else -1
