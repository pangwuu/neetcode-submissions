from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # index corresponds to the course number, and its value corresponds to 
        # the number of courses needed for u to take it

        indegree = [0] * numCourses
        queue = deque([])

        # index of the graph represents the course num, and the values at that indicate 
        # the courses that depend on this graph
        graph = [[] for _ in range(numCourses)]

        # cycle detection
        found = set()

        # go through and find all courses without prerequisites (indegree 0)        

        for prerequisite in prerequisites:
            course_num = prerequisite[0]
            prereq = prerequisite[1]
            
            # you need +1 prerequisite
            indegree[course_num] += 1
            graph[prereq].append(course_num)
        
        for index, prereq in enumerate(indegree):
            # adding all courses without prerequisites
            if prereq == 0:
                queue.append(index)
                found.add(index)
        
        if not queue:
            # if there is like endless cycles to start
            return False
        
        while queue:
            course_taken: int = queue.popleft()
            dependent_courses: List[int] = graph[course_taken]
            for course in dependent_courses:
                indegree[course] -= 1
                if indegree[course] <= 0:
                    queue.append(course)
                    found.add(course)
        
        return len(found) == numCourses



