"""
Problem: Moving Average from Data Stream (LeetCode 346)
Chapter: Queues
Source: session solution (2026-10-29 — practice attempt stalled at ~1 hour).

Companion file: course/queues/practice/2026-10-29-MovingAverageFromDataStream.py
"""

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()

        return self.total / len(self.queue)


if __name__ == "__main__":
    moving_average = MovingAverage(3)
    print(moving_average.next(1))
    # expected: 1.0
    print(moving_average.next(10))
    # expected: 5.5
    print(moving_average.next(3))
    # expected: 4.666666666666667
    print(moving_average.next(5))
    # expected: 6.0

    single = MovingAverage(1)
    print(single.next(-3))
    # expected: -3.0
    print(single.next(4))
    # expected: 4.0
