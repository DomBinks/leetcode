class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeros = 0
        ones = 0

        for student in students:
            if student == 0:
                zeros += 1
            else:
                ones += 1

        for i in range(0, len(sandwiches)):
            if sandwiches[i] == 0 and zeros > 0:
                zeros -= 1
            elif sandwiches[i] == 1 and ones > 0:
                ones -= 1
            else:
                return len(sandwiches) - i

        return 0
