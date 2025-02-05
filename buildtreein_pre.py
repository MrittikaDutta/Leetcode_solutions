class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    index_map = {data: i for i, data in enumerate(inorder)}  # Store inorder indices for O(1) lookup
    pre_index = [0]  # Using a list to keep track of current preorder index across recursive calls

    def construct(in_left, in_right):
        if in_left > in_right:
            return None

        root_data = preorder[pre_index[0]]
        root = TreeNode(root_data)
        pre_index[0] += 1  # Move to the next root in preorder

        inorder_index = index_map[root_data]  # Find root index in inorder
        root.left = construct(in_left, inorder_index - 1)
        root.right = construct(inorder_index + 1, in_right)

        return root

    return construct(0, len(inorder) - 1)

def postorder_traversal(root):
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.data]

# Example Usage
preorder1 = [1, 6, 7, 8]
inorder1 = [1, 6, 8, 7]
root1 = build_tree(preorder1, inorder1)
print(postorder_traversal(root1))  # Output: [8, 7, 6, 1]

preorder2 = [0, 1, 3, 4, 2, 5]
inorder2 = [3, 1, 4, 0, 2, 5]
root2 = build_tree(preorder2, inorder2)
print(postorder_traversal(root2))  # Output: [3, 4, 1, 5, 2, 0]

preorder3 = [1, 4, 5, 2, 3]
inorder3 = [2, 5, 4, 1, 3]
root3 = build_tree(preorder3, inorder3)
print(postorder_traversal(root3))  # Output: [2, 5, 4, 3, 1]
