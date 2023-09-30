"""doc
"""


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.count = 0

    def insert(self,data):
        item = Node(data)

        if self.root is None:
            self.root = item
            self.count+=1
            return
        current_node = self.root
        while True:
            if current_node.data < item.data:
                if current_node.rightchild is None:
                    current_node.rightchild = item
                    self.count+=1
                    return
                else:
                    current_node = current_node.rightchild
            else:
                if current_node.leftchild is None:
                    current_node.leftchild = item
                    self.count+=1
                    return
                else:
                    current_node = current_node.

    def _get_parent(self, data):
        
        
        current_ = None
        parent = None
    def delete(self,data):



    def inorder_traveral(self):
        tree = self.root
        stack, result = [], []
        while stack or tree:
            if tree:
                stack.append(tree)
                tree = tree.leftchild
            else:
                tree = stack.pop()
                result.append(tree.data)
                tree = tree.rightchild
        return result

    def inorder(self, root):
        curr_root = root
        if curr_root is None:
            return
        self.inorder(curr_root.leftchild)
        print(curr_root.data)
        self.inorder(curr_root.rightchild)

# Test Cases
BST = BinarySearchTree()
for num in [5,2,7,9,1]:
    BST.insert(num)

r = BST.inorder_traveral()
print(r)
