class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n  # Track which baskets are used
        unplaced = 0

        for i in range(n):  # For each fruit
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced
