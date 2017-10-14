



class MinStack(object):

    dataList = []

    def __init__(self):
        """
        initialize your data structure here.
        self.dataList = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.dataList.append([x,curMin])
        

    def pop(self):
        :rtype: void
        """
        self.dataList.pop()
        if len(self.dataList) is 0:
            self.curMin = None
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.dataList) is 0:
            return None
        return self.dataList[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.dataList) is 0:
            return None
        return self.dataList[-1][1]
        

# Your MinStack object will be instantiated and called as such:
s = MinStack();
s.push(0);
s.push(1);
s.push(0);
s.getMin();
s.pop();
print(s.dataList)
m = s.getMin();
print(m)
