import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get a task name --> number of tasks of that task as a dict, 
        # then sort by priority and do each task greedily (do the one which has the most number first)
        tasks_frequencies = {}
        for task in tasks:
            if task in tasks_frequencies:
                tasks_frequencies[task] += 1
            else:
                tasks_frequencies[task] = 1
        
        task_counts = []
        for taskName, frequency in tasks_frequencies.items():
            task_counts.append([-frequency, taskName])
        
        # convert it to a heap
        heapq.heapify(task_counts)

        # there are n tasks in the cooldown queue
        cooldown = deque([None] * (n + 1))
        fully_cooled = deque([None] * (n + 1))

        time = 0
        while task_counts or cooldown != fully_cooled:
            print(cooldown)
            print(task_counts)

            # take out any tasks which have been able to cool down
            cooled = cooldown.popleft()
            if cooled:
                heapq.heappush(task_counts, cooled)
            
            if len(task_counts) == 0:
                cooldown.append(None)
                print('idle\n')
                time += 1
                continue

            populous_task = heapq.heappop(task_counts)
            print(f'processing {populous_task}')
            print()

            # put this back in the cooldown queue
            if populous_task and populous_task[0] != -1:
                cooldown.append([populous_task[0] + 1, populous_task[1]])
            else:
                cooldown.append(None)

            time += 1
        
        return time
            


        