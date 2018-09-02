class MyHashSet:

    data = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [False] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.data[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.data[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.data[key]


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
param_2 = obj.contains(1)
print(param_2)
obj.remove(1)
param_3 = obj.contains(1)
print(param_3)
