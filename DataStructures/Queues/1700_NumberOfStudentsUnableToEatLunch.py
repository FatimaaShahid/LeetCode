from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)  
        sandwiches = deque(sandwiches)

        no_change_count = 0  

        while students:
            if students[0] == sandwiches[0]: 
                students.popleft()
                sandwiches.popleft()
                no_change_count = 0  
            else:
                students.append(students.popleft())  
                no_change_count += 1

            if no_change_count == len(students): 
                break
        
        return len(students)
