"""
A Linked list is a 
"""

import random

class Node:
    """_summary_
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    """doc
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0

    def insert(self,data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        """
        node_data = Node(data)

        if self.head is None:
            self.head = self.tail = node_data
            self.size_ += 1

        else:
            node_data.prev = self.tail
            self.tail.next = node_data
            self.tail = node_data
            self.size_ += 1

    def size(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self.size_

    def _iter(self):
        current_node= self.head
        while current_node:
            current_data = (current_node.data, current_node)
            current_node = current_node.next
            yield current_data

    def search(self, data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        found = False
        linked_gen = self._iter()
        linked_data , _= next(linked_gen)
        while linked_data is not None:
            if data == linked_data:
                found = True
                return found
            linked_data, _ = next(linked_gen)
        return found

    def delete(self,data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        done = False
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            self.size_ -= 1
            done = True

        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size_ -= 1
            done = True

        else:
            curr_node = self.head.next
            prev_node = self.head
            while curr_node is not None:
                if curr_node.data == data:
                    prev_node.next = curr_node.next
                    curr_node.next.prev = prev_node
                    self.size_ -= 1
                    done = True
                prev_node = curr_node
                curr_node = curr_node.next
            return done

    def traversal(self):
        """doc
        """
        list_ = []
        current = self.head
        while current:
            list_.append(current.data)
            current = current.next
        return list_
    def backward_traversal(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        list_ = []
        current = self.tail
        while current:
            list_.append(current.data)
            current = current.prev
        return list_

# TEST CASE
def insert_test(array_, sample_linked_list):
    """run test
    """
    try:
        for num in array_:
            sample_linked_list.insert(num)
        print("Insert Succesful")
    except Exception as error:
        print(f"Insert failed {error}")


def size_of_list(sample_linked_list):
    """run test
    """
    return sample_linked_list.size()

def search_test(array_,sample_linked_list):
    """run test
    """
    try:
        no_iter = 4
        while no_iter > 0:
            element = random.choice(array_)
            result = sample_linked_list.search(element)
            print(result)
            if result is False:
                raise Exception
            no_iter -= 1
    except Exception as error:
        print(f"Search failed {error}")

def delete_test(array_,sample_linked_list):
    """run test
    """
    try:
        no_iter = 4
        while no_iter > 0:
            element = random.choice(array_)
            result = sample_linked_list.delete(element)
            print(result)
            if result is False:
                raise Exception
            no_iter -= 1
    except Exception as error:
        print(f"Delete failed {error}")


def main():
    """run test
    """
    try:
        sample_array = [random.randint(0, 1000) for num in range(10)]
        print(sample_array)
        intger_list = DoubleLinkedList()
        insert_test(sample_array,intger_list)
        print(size_of_list(intger_list))
        forward_list =  intger_list.traversal()
        print(forward_list)
        search_test(sample_array,intger_list)
        print('runing delete_test')
        delete_test(sample_array,intger_list)
        print(size_of_list(intger_list))
        forward_list =  intger_list.traversal()
        print(forward_list)
        backward_list =  intger_list.backward_traversal()
        print(backward_list)
    except Exception as error:
        print(error)

main()
