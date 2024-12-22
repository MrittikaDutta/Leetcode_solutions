class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        events = [(idx, 10 ** 9, h) for idx, h in enumerate(heights)]
        for idx, query in enumerate(queries):
            a, b = min(query), max(query)
            if a == b or heights[a] < heights[b]:
                res[idx] = b
            else:
                events.append((b, idx, heights[a]))
                
        stack = [] # list of (height, idx)
        for pos, idx, h in sorted(events, reverse = True):
            if idx == 10 ** 9:
                while stack and stack[-1][0] <= h:
                    stack.pop()
                stack.append((h, pos))
            elif stack and stack[0][0] > h:
                low, high = 0, len(stack) - 1
                while low != high:
                    mid = (low + high + 1) >> 1
                    if stack[mid][0] > h:
                        low = mid
                    else:
                        high = mid - 1
                res[idx] = stack[low][1]
                
        return res
