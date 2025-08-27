class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_cost = 0
        i, n = 0, len(colors)
        while i < n:
            count = 0
            sum_color = 0
            max_time = 0
            while i < n-1 and colors[i]==colors[i+1]:
                sum_color += neededTime[i]
                max_time = max(max_time, neededTime[i])
                count += 1
                i += 1
            sum_color += neededTime[i]
            max_time = max(max_time, neededTime[i])
            count += 1
            if count >= 2:
                min_cost += sum_color-max_time
            i += 1
        return min_cost
                
            
