import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for passi, totali in classes:
            # Compute initial marginal gain (negative for max-heap)
            delta = -( (passi + 1) / (totali + 1) - (passi / totali) )
            heapq.heappush(heap, (delta, passi, totali))
        
        # Assign extra students
        for _ in range(extraStudents):
            delta, passi, totali = heapq.heappop(heap)
            passi += 1
            totali += 1
            new_delta = -( (passi + 1) / (totali + 1) - (passi / totali) )
            heapq.heappush(heap, (new_delta, passi, totali))
        total_ratio = 0
        while heap:
            _, passi, totali = heapq.heappop(heap)
            total_ratio += passi / totali
        
        return total_ratio / len(classes)
