"""
Problem: Moving Average from Data Stream (LeetCode 346)
Chapter: Queues

Given a stream of integers and a window size, return the moving average of the
last `size` values seen. `next(val)` appends `val` to the stream and returns the
average of everything currently inside the window (fewer than `size` values
early on, so divide by how many you actually hold).
"""


class MovingAverage:
    def __init__(self, size: int):
        pass

    def next(self, val: int) -> float:
        pass


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
