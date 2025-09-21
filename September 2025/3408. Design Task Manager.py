class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # Maps taskId -> (priority, userId)
        self.taskMap = {}
        # Max-heap: store (-priority, -taskId) for ordering
        self.heap = []
        
        for userId, taskId, priority in tasks:
            self.taskMap[taskId] = (priority, userId)
            heapq.heappush(self.heap, (-priority, -taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.taskMap:
            userId = self.taskMap[taskId][1]
            self.taskMap[taskId] = (newPriority, userId)
            heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskMap:
            del self.taskMap[taskId]

    def execTop(self) -> int:
        # Pop until we find a valid task
        while self.heap:
            neg_prio, neg_tid = heapq.heappop(self.heap)
            prio = -neg_prio
            tid = -neg_tid
            if tid in self.taskMap and self.taskMap[tid][0] == prio:
                userId = self.taskMap[tid][1]
                del self.taskMap[tid]  # remove after execution
                return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
