class MyHashMap:

    values = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = [-1] * 1000000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.values[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.values[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.values[key] = -1


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 999)
param_2 = obj.get(1)
print(param_2)
obj.remove(1)
param_3 = obj.get(1)
print(param_3)
