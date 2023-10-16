"""doc
"""


class HashItem:
    """_summary_"""

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashTable:
    """_summary_"""

    def __init__(self, size) -> None:
        self.size = size
        self.slots = [None for num in range(self.size)]
        self._max_load_factor = 0.65
        self._count = 0

    def _hash(self, key):
        hash_value = 0
        mutli = 0
        for char in key:
            hash_value = mutli * ord(char)
            mutli += 1
        return hash_value % self.size

    def put(self, key, data):
        """_summary_

        Parameters
        ----------
        key : _type_
            _description_
        data : _type_
            _description_
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
        """_summary_

        Parameters
        ----------
        key : _type_
            _description_

        Returns
        -------
        _type_
            _description_
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
