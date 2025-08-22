class Solution:
    def frequencySort(self, s: str) -> str:
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1

        heap = []
        idx = 0
        for k, v in mp.items():
            heappush(heap, (-v, idx, k))
            idx += 1
        
        result = []
        while heap:
            freq, _, ch = heappop(heap)
            freq = -freq
            while freq>0:
                result.append(ch)
                freq -= 1

        return "".join(result)

