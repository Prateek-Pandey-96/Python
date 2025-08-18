class Solution:
    def helper(self, idx, temp, digits, mapping, result) -> None:
        if idx == len(digits):
            result.append("".join(temp))
            return

        for ch in mapping[digits[idx]]:
            temp.append(ch)
            self.helper(idx+1, temp, digits, mapping, result)
            temp.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {}
        mapping["2"] = ["a", "b", "c"]
        mapping["3"] = ["d", "e", "f"]
        mapping["4"] = ["g", "h", "i"]
        mapping["5"] = ["j", "k", "l"]
        mapping["6"] = ["m", "n", "o"]
        mapping["7"] = ["p", "q", "r", "s"]
        mapping["8"] = ["t", "u", "v"]
        mapping["9"] = ["w", "x", "y", "z"]

        result = []
        temp = []
        self.helper(0, temp, digits, mapping, result)
        return result
