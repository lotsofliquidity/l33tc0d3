"""
Problem: Find Players With Zero or One Losses
Chapter: Hashing / counting
Source: course example

Idea: Count losses for every player who appeared. Players with 0 and exactly 1 loss are the two sorted lists.
"""

from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = defaultdict(int)
        for winner, loser in matches:
            # += 0 records a new winner at 0 and leaves an existing loss count unchanged.
            losses[winner] += 0
            losses[loser] += 1

        zero, one = [], []
        for player, count in losses.items():
            if count == 0:
                zero.append(player)
            elif count == 1:
                one.append(player)
        return [sorted(zero), sorted(one)]
