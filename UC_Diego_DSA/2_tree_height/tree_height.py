"""doc
"""

import sys
import threading

class TreeNode:
    """_summary_
    """
    def __init__(self, parent) -> None:
        self.leftchild = None
        self.rightchild = None
        self.parent = parent

def compute_height(root):
    """_summary_

    Parameters
    ----------
    root : object
        _description_

    Returns
    -------
    int
        The height of the tree 
    """

    if not root:
        return 0
    else:
        return 1 + max(compute_height(root.leftchild), compute_height(root.rightchild))

def build_tree(parents_arr, number):
    """_summary_

    Parameters
    ----------
    parents_arr : list
        _description_
    number : int
        _description_

    Returns
    -------
    object
        _description_
    """
    for idx in range(number):
        parents_arr[idx] = TreeNode(parents_arr[idx])

    for idx, parent_node in enumerate(parents_arr):
        if parent_node.parent == -1:
            root = parent_node
        else:
            if not parents_arr[parent_node.parent].leftchild:
                parents_arr[parent_node.parent].leftchild = parents_arr[idx]
            else:
                parents_arr[parent_node.parent].rightchild = parents_arr[idx]
    return root

def main():
    """_summary_
    """
    num_node = int(input())
    parents = list(map(int, input().split()))
    tree_root = build_tree(parents, num_node)
    print(compute_height(tree_root))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
