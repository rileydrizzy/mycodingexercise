"""
A Linked list is a data structure. It consist of chaining nodes that contains data 
and pointers sequentially. Thereby linking them all together
It uses the pointers to point to the next node. 
It's fast in inserting and deleting at either head or tail of the linked list

"""
import random

class Node:
    """"
    A node to contain the data and pointer
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """Single Linked List
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self):
        """return size of Linked List

        Returns
        -------
        Int
            return size of Linked List
        """
        return self.size

    def insert(self,data):
        """insert node into Linked List

        Parameters
        ----------
        data : Object
            data element
        """
        node_data = Node(data)
        if self.head is None:
            self.head = self.tail = node_data
            self.size += 1

        else:
            self.tail.next = node_data
            self.tail = node_data
            self.size += 1

    def _iter(self):
        current = self.head
        while current:
            current_data = current.data
            current = current.next
            yield current_data

    def search(self,data):
        """search for data in Linked List

        Parameters
        ----------
        data : Object

        Returns
        -------
        Bool
            if element is found, return True, else return False
        """
        found = False
        linked_gen = self._iter()
        linked_data = next(linked_gen)
        while linked_data is not None:
            if data == linked_data:
                found = True
                return found
            else:
                linked_data = next(linked_gen)
        return found

    def delete(self,data):
        """remove a node from the linked list

        Parameters
        ----------
        data : Object
            _description_
        """
        done = False
        if self.head is None:
            print("Linked List is Empty")

        elif self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            done = True
        else:
            curr_node = self.head
            prev_node = curr_node
            while curr_node is not None:
                if curr_node.data == data:
                    prev_node.next = curr_node.next
                    self.size -= 1
                    done = True
                    return done
                prev_node = curr_node
                curr_node = curr_node.next
        return done
    def traversal(self):
        """run test
        """
        list_ = []
        current = self.head
        while current:
            list_.append(current.data)
            current = current.next
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
    return sample_linked_list.length()

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
        intger_list = LinkedList()
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
    except Exception as error:
        print(error)

main()
