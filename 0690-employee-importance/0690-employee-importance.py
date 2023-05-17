"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {j.id:i for i, j in enumerate(employees)}
        stack = [id]
        ans = 0
        while(stack):
            curr = stack.pop()
            ans += employees[dic[curr]].importance
            for child in employees[dic[curr]].subordinates:             
                stack.append(child)
        return ans
        
        