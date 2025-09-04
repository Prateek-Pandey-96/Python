class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()

        heap, result = [], []
        
        idx = 0
        while idx<n:
            t_start = tasks[idx][0]
            while idx < n and tasks[idx][0]==t_start:
                heappush(heap, (tasks[idx][1], tasks[idx][2], tasks[idx][0]))
                idx += 1
            
            while heap:
                duration, i, start = heappop(heap)
                result.append(i)

                limit = max(start, t_start) + duration
                while idx < n and tasks[idx][0] <= limit:
                    heappush(heap, (tasks[idx][1], tasks[idx][2], tasks[idx][0]))
                    idx += 1
                t_start = limit
        
        return result


