class TreedNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f'key: {self.key}\n' \
               f'left {self.left}\n' \
               f'right {self.right}\n'


def copy_tree(root: TreedNode):
    if root is None:
        return None

    new_root = TreedNode(root.key)
    new_root.left = copy_tree(root.left)
    new_root.right = copy_tree(root.right)

    return new_root


def find_max_key(root: TreedNode):
    if root is None:
        return float('-inf')

    max_key = root.key
    max_left = find_max_key(root.left)
    max_right = find_max_key(root.right)

    return max(max_key, max_left, max_right)
