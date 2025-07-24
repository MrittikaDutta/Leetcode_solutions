from typing import List
from collections import defaultdict
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        in_time = [0] * n
        out_time = [0] * n
        subtree_xor = [0] * n
        time = 1

        # DFS to compute subtree XORs and time intervals
        def dfs(u, parent):
            nonlocal time
            in_time[u] = time
            time += 1
            xor_val = nums[u]
            for v in tree[u]:
                if v != parent:
                    xor_val ^= dfs(v, u)
            out_time[u] = time
            subtree_xor[u] = xor_val
            return xor_val

        total_xor = dfs(0, -1)
        
        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        # Store all edges with child pointing to parent
        edge_list = []
        for u, v in edges:
            if in_time[u] > in_time[v]:
                u, v = v, u
            edge_list.append((v, u))  # child, parent

        min_score = float('inf')
        for i in range(len(edge_list)):
            c1, p1 = edge_list[i]
            xor1 = subtree_xor[c1]
            for j in range(i+1, len(edge_list)):
                c2, p2 = edge_list[j]
                xor2 = subtree_xor[c2]

                if is_ancestor(c1, c2):
                    x1 = subtree_xor[c2]
                    x2 = xor1 ^ x1
                    x3 = total_xor ^ xor1
                elif is_ancestor(c2, c1):
                    x1 = subtree_xor[c1]
                    x2 = xor2 ^ x1
                    x3 = total_xor ^ xor2
                else:
                    x1 = xor1
                    x2 = xor2
                    x3 = total_xor ^ xor1 ^ xor2

                vals = [x1, x2, x3]
                min_score = min(min_score, max(vals) - min(vals))

        return min_score
