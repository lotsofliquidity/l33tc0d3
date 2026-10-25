"""
Problem: Find Players With Zero or One Losses (LeetCode 2225)
Chapter: Hashing / counting
Regime: cold revisit — no notes, no solution file

You are given an integer array matches where matches[i] = [winner_i, loser_i]
indicates that the player winner_i defeated player loser_i in a match.

Return a list answer of size 2 where:
  answer[0] is all players that have not lost any matches.
  answer[1] is all players that have lost exactly one match.
Both lists are in increasing order.

Only consider players that have played at least one match.

Example:
  Input: matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
  Output: [[1, 2, 5, 6], []]
"""

from collections import defaultdict

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = defaultdict(int)

        # building my dictionary
        for match in matches:
            losses[match[0]] += 0
            losses[match[1]] += 1

        winners = []
        losers = []
        for team, loss in losses.items():
            if loss == 0:
                winners.append(team)
            elif loss == 1:
                losers.append(team)

        return [sorted(winners), sorted(losers)]
            


if __name__ == "__main__":
    print(Solution().findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
    # expected: [[1, 2, 5, 6], []]
