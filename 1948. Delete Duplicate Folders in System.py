from typing import List, Dict
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = dict()
        self.name: str = ""
        self.deleted: bool = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        # Step 1: Build the Trie
        for path in paths:
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = TrieNode()
                    curr.children[folder].name = folder
                curr = curr.children[folder]

        # Step 2: Serialize each subtree
        subtree_map = defaultdict(list)

        def serialize(node: TrieNode) -> str:
            if not node.children:
                return ""
            serial = []
            for child_name in sorted(node.children):
                child_serial = serialize(node.children[child_name])
                serial.append(f"{child_name}({child_serial})")
            full_serial = "".join(serial)
            subtree_map[full_serial].append(node)
            return full_serial

        serialize(root)

        # Step 3: Mark all duplicate subtrees for deletion
        for nodes in subtree_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Step 4: Collect paths that are not marked for deletion
        result = []

        def collect_paths(node: TrieNode, path: List[str]):
            for name, child in node.children.items():
                if not child.deleted:
                    new_path = path + [name]
                    result.append(new_path)
                    collect_paths(child, new_path)

        collect_paths(root, [])
        return result
