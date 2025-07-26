from collections import defaultdict
import heapq

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:

        m = len(conflictingPairs)
        # Preprocess pairs: l, r, add at l
        adds = [[] for _ in range(n+2)]  # 1-indexed
        pairs = []  # store (l, r)
        for idx, (a, b) in enumerate(conflictingPairs):
            l = min(a, b)
            r = max(a, b)
            pairs.append((l, r))
            adds[l].append(idx)
        
        # counts of active r values
        counts = defaultdict(int)
        # mapping r -> list of pair indices
        mapping = defaultdict(list)
        # min-heap of unique r keys
        heap = []
        
        total_sub = n * (n+1) // 2
        union_full = 0
        # unique area per pair
        unique_area = [0] * m
        
        # sweep start positions s from n down to 1
        for s in range(n, 0, -1):
            # activate pairs with l == s
            for j in adds[s]:
                l, r = pairs[j]
                # update counts
                if counts[r] == 0:
                    heapq.heappush(heap, r)
                counts[r] += 1
                mapping[r].append(j)
            # clean invalid keys
            while heap and counts[heap[0]] == 0:
                heapq.heappop(heap)
            if not heap:
                continue
            # minimal r1
            r1 = heap[0]
            c1 = counts[r1]
            # accumulate union full
            union_full += (n - r1 + 1)
            # if unique minimal
            if c1 == 1:
                # find second minimal R2
                # remove r1 temporarily
                heapq.heappop(heap)
                # clean invalid
                while heap and counts[heap[0]] == 0:
                    heapq.heappop(heap)
                if heap:
                    r2 = heap[0]
                else:
                    r2 = n + 1
                # push back r1
                heapq.heappush(heap, r1)
                # the single pair index
                j_id = mapping[r1][0]
                unique_area[j_id] += (r2 - r1)
        
        # valid subarrays with all pairs
        valid_full = total_sub - union_full
        # choose best removal
        best_unique = max(unique_area) if unique_area else 0
        return valid_full + best_unique
