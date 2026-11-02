"""
Problem: Online Stock Span (LeetCode 901)
Chapter: Monotonic

For each day's price, return the number of consecutive days ending today whose
prices are less than or equal to today's price.
"""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


if __name__ == "__main__":
    stock_spanner = StockSpanner()
    for price in [100, 80, 60, 70, 60, 75, 85]:
        print(stock_spanner.next(price))
    # expected: 1, 1, 1, 2, 1, 4, 6
