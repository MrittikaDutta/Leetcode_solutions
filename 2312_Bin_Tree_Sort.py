# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps_to_sort(arr):
            """
            Calculate the minimum number of swaps needed to sort the array.
            """
            n = len(arr)
            indexed_arr = [(value, index) for index, value in enumerate(arr)]
            indexed_arr.sort()  # Sort based on the values, maintaining original indices
            
            visited = [False] * n
            swaps = 0

            for i in range(n):
                # If the element is already visited or in the correct position, skip it
                if visited[i] or indexed_arr[i][1] == i:
                    continue
                
                # Count the size of the cycle
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = indexed_arr[j][1]
                    cycle_size += 1
                
                # A cycle of size `k` requires `k-1` swaps to resolve
                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps
        if not root:
            return 0

        queue = deque([root])
        total_operations = 0

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate the minimum swaps needed to sort the current level
            total_operations += min_swaps_to_sort(level)

        return total_operations
