class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        temp = []
        idx = 0
        for num in nums:
            original_num = num
            new_num = []
            if num == 0:
                new_num = [str(mapping[0])]
            else:
                while num > 0:
                    digit = num % 10
                    num = num // 10
                    new_num.append(str(mapping[digit]))
                new_num.reverse()
            temp.append((int("".join(new_num)), idx, original_num))
            idx += 1
        
        temp.sort()
        result = []
        for _, _, original_num in temp:
            result.append(original_num)
        
        return result


