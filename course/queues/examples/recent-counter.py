"""
Problem: Number of Recent Calls (LeetCode 933)
Chapter: Queues
Source: course article (queues — enqueue the new ping, dequeue everything older
than t - 3000, return the queue length).

Companion file: none yet — there is no practice attempt for this problem.
"""

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
