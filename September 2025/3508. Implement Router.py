from collections import deque, defaultdict
import bisect
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # stores packets in FIFO: (src, dest, ts)
        self.packetSet = set()  # to detect duplicates
        self.destMap = defaultdict(list)  # dest -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        # Check duplicate
        if packet in self.packetSet:
            return False

        # If full, evict oldest
        if len(self.queue) >= self.memoryLimit:
            old_src, old_dest, old_ts = self.queue.popleft()
            self.packetSet.remove((old_src, old_dest, old_ts))
            # remove old timestamp from destMap
            idx = bisect.bisect_left(self.destMap[old_dest], old_ts)
            if 0 <= idx < len(self.destMap[old_dest]) and self.destMap[old_dest][idx] == old_ts:
                self.destMap[old_dest].pop(idx)

        # Insert new packet
        self.queue.append(packet)
        self.packetSet.add(packet)
        bisect.insort(self.destMap[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        src, dest, ts = self.queue.popleft()
        self.packetSet.remove((src, dest, ts))
        # remove timestamp from destMap
        idx = bisect.bisect_left(self.destMap[dest], ts)
        if 0 <= idx < len(self.destMap[dest]) and self.destMap[dest][idx] == ts:
            self.destMap[dest].pop(idx)
        return [src, dest, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destMap[destination]
        # Find lower bound for startTime
        left = bisect.bisect_left(timestamps, startTime)
        # Find upper bound for endTime
        right = bisect.bisect_right(timestamps, endTime)
        return right - left
