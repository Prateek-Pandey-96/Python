class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        mp = defaultdict(int)
        mp[0] = -1
        
        max_len, running_sum = 0, 0
        for i in range(len(nums)):
            running_sum += nums[i] if nums[i] != 0 else -1

            if running_sum in mp:
                max_len = max(max_len, i-mp[running_sum])
            else:
                mp[running_sum] = i
        
        return max_len
