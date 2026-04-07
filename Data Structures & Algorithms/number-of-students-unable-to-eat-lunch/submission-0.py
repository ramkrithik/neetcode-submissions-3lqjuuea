class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import Counter
        available = Counter(students)
        for s in sandwiches:
            if available[s] == 0:
                return sum(available.values())
            available[s]-=1
        return 0
