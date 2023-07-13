 class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToReqs = {} # Stores requirements for each course

        # Setup dictionary for course to requitements
        for i in range(0, numCourses):
            courseToReqs[i] = []

        # Put requirements into dictionary
        for pair in prerequisites:
            courseToReqs[pair[0]].append(pair[1]) 

        seen = set() # Set to store courses seen

        # For each course
        for course in range(0, numCourses):
            # If you can find this course again
            if self.findAgain(course, seen, courseToReqs):
                return False

        # Otherwise
        return True

    def findAgain(self, course, seen, CTR):
        # If the course has no prerequisites or has previously
        # been checked and has had its prerequisites accounted for
        if CTR[course] == []:
            return False

        # If the course has prerequisites

        # If the course has already been seen, meaning that there
        # is a loop
        if course in seen:
            return True

        # Add this course to the courses seen
        seen.add(course)

        # For each prerequisite of this course
        for req in CTR[course]:
            # If any prequisite of this course is a course that's
            # been previously seen
            if self.findAgain(req, seen, CTR):
                return True
        # This also updates seen with new courses
        
        # This course's prerequisites are valid so set to [] so we
        # don't want to check again, which is important as course is
        # now in seen.
        # This course won't be checked again as findAgain will terminate
        # inside the 1st if statement.
        CTR[course] = []

        # Can't find any course again
        return False
