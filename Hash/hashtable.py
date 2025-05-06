"""
hashtable.py

This module contains the implementation of a simple hash table with basic operations such as insertion and hashing.

Classes:
    HashItem: Represents an item in the hash table.
    HashTable: Represents the hash table with methods to insert and hash items.
"""

class HashItem:
    """
    Represents an item in the hash table.

    Attributes:
        key: The key associated with the item.
        value: The value associated with the item.
    """

    def __init__(self, key, value) -> None:
        """
        Initializes a new HashItem with the given key and value.

        Args:
            key: The key associated with the item.
            value: The value associated with the item.
        """
        self.key = key
        self.value = value


class HashTable:
    """
    Represents the hash table.

    Attributes:
        size: The size of the hash table.
        slots: The slots in the hash table.
        _max_load_factor: The maximum load factor before resizing.
        _count: The current number of items in the hash table.
    """

    def __init__(self, size) -> None:
        """
        Initializes a new HashTable with the given size.

        Args:
            size: The size of the hash table.
        """
        self.size = size
        self.slots = [None for num in range(self.size)]
        self._max_load_factor = 0.65
        self._count = 0

    def _hash(self, key):
        """
        Computes the hash value for a given key.

        Args:
            key: The key to hash.

        Returns:
            The hash value of the key.
        """
        hash_value = 0
        mutli = 0
        for char in key:
            hash_value = mutli * ord(char)
            mutli += 1
        return hash_value % self.size

    def put(self, key, data):
        """
        Inserts a key-value pair into the hash table.

        Args:
            key: The key to insert.
            data: The value to insert.
        """
        item = HashItem(key, data)
        hashval = self._hash(key)
        j = 1
        while self.slots[hashval] is not None:
            if self.slots[hashval].key == key:
                break
            hashval = (hashval + j * j) % self.size
            j += 1
        if self.slots[hashval] is None:
            self._count += 1
        self.slots[hashval] = item
        self._check_growth()

    def _growth(self):
        new_hashtable = HashTable(self.size * 2)
        new_hashtable.slots = [None for num in range(new_hashtable.size)]

        for idx in range(self.size):
            if self.slots[idx] is not None:
                new_hashtable.put(self.slots[idx].key, self.slots[idx].value)
        self.size = new_hashtable.size
        self.slots = new_hashtable.slots

    def _check_growth(self):
        load_factor = self._count / self.size
        if load_factor > self._max_load_factor:
            print("Growing Hashtable")
            self._growth()

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hash table.

        Args:
            key: The key to retrieve.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        hashval = self._hash(key)
        j = 1
        while self.slots[hashval] is not None:
            if self.slots[hashval].key == key:
                return self.slots[hashval].value
            hashval = (hashval + j * j) % self.size
        return None

    # Implementing hashtable as a dictionary
    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


# Test
Table = HashTable(size=3)
Table.put("good", "eggs")
Table.put("better", "ham")
Table.put("best", "spam")
Table.put("ad", "do not")
Table.put("ga", "collide")

for key_ in ("good", "better", "best", "worst", "ad", "ga"):
    value_ = Table.get(key_)
    print(value_)
# Testing the hash table as a dictionary
Table["Adele"] = "One and Only"
print(Table["Adele"])
