class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        total_time = 0
        prev = 0  # index of previous balloon in the group
        
        for i in range(1, len(colors)):
            if colors[i] == colors[prev]:
                # remove the smaller one to minimize total cost
                total_time += min(neededTime[i], neededTime[prev])
                # keep the larger one for future comparison
                if neededTime[i] > neededTime[prev]:
                    prev = i
            else:
                prev = i
        
        return total_time
