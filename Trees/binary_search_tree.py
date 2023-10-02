"""doc
"""

class Node:
    """_summary_
    """
    def __init__(self,data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None

class BinarySearchTree:
    """_summary_
    """
    def __init__(self) -> None:
        self.root_node = None
        self.count = 0

    def insert(self,data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        """
        item = Node(data)
        if self.root_node is None:
            self.root_node = item
            self.count+=1
            return
        current_node = self.root_node
        while True:
            if item.data > current_node.data:
                if current_node.rightchild is None:
                    current_node.rightchild = item
                    self.count+=1
                    return
                current_node = current_node.rightchild
            else:
                if current_node.leftchild is None:
                    current_node.leftchild = item
                    self.count+=1
                    return
                current_node = current_node.leftchild

    def _get_parent(self, data):
        current_node = self.root_node
        parent_node = None
        if current_node is None:
            return (parent_node, current_node)
        while True:
            if data == current_node.data:
                return(current_node, parent_node)
            if data > current_node.data:
                parent_node = current_node
                current_node = current_node.rightchild
            else:
                parent_node = current_node
                current_node = current_node.rightchild
        return  (current_node, parent_node)

    def delete(self, data):
        current, parent = self._get_parent(data)
        if current is None and parent is None:
            print("Not Found")
            return False
        if (current.leftchild is not None) and (current.rightchild is not None):
            no_childern_count = 2
        elif (current.leftchild is None) and (current.rightchild is None):
            no_childern_count = 0
        else:
            no_childern_count = 1

# Delete a node that has no child
        if no_childern_count == 0:
            if parent is not None:
                if parent.leftchild is current:
                    parent.leftchild = None
                else:
                    parent.rightchild = None
            else:
                self.root_node = None
# Delete a node that has one child
        if no_childern_count == 1:
            if current.leftchild:
                next_node = current.leftchild
            else:
                next_node = current.rightchild
            if parent is not None:
                if parent.leftchild is current:
                    parent.leftchild = next_node
                else:
                    parent.rightchild = next_node
            else:
                self.root_node = next_node
        # Delete a node that has two childs
       
        self.count-= 1

    def inorder_traveral(self):
        tree = self.root_node
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

    def max_node(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        curr_node = self.root_node
        parent = None
        while curr_node:
            parent = curr_node
            curr_node = curr_node.rightchild
        return parent.data

    def min_node(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        curr_node = self.root_node
        parent = None
        while curr_node:
            parent = curr_node
            curr_node = curr_node.leftchild
        return parent.data
    def search(self, item):
        current = self.root_node
        while current is not None and current.data == item:
            if current.data < item:
                current = current.leftchild
            else:
                current = current.rightchild
        return current
# Test
def test():
    """_summary_
    """
    bst_tree = BinarySearchTree()
    bst_tree.insert(5)
    bst_tree.insert(2)
    bst_tree.insert(7)
    bst_tree.insert(9)
    bst_tree.insert(1)
    print(bst_tree.min_node())
    print(bst_tree.max_node())

    node = bst_tree.search(9)
    print(f'node is {node.data}')
    #bst_tree.delete(9)
    #bst_tree.search(9)
    print(bst_tree.inorder_traveral())
    print(bst_tree.min_node())
    print(bst_tree.max_node())

test()
