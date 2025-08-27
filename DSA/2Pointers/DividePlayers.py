class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        low, high = 0, len(skill)-1
        
        chemistry_sum = skill[low]*skill[high]
        expected_sum = skill[low]+skill[high]
        low += 1
        high -= 1
        while low < high:
            sum = skill[low] + skill[high]
            if sum != expected_sum:
                return -1
            else:
                chemistry_sum += skill[low]*skill[high]
                low += 1
                high -= 1
        
        return chemistry_sum

