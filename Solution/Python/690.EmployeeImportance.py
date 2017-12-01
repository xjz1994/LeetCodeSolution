direct


# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        val = 0
        employDict = dict()
        for i in employees:
            employDict.update({i.id:i})

        emp = employDict[id]
        if emp :
            val += emp.importance

        sub = emp.subordinates
        while sub:
            item = employDict[sub.pop(0)]
            if item:
                val += item.importance
                if item.subordinates:
                    sub += item.subordinates

        return val
