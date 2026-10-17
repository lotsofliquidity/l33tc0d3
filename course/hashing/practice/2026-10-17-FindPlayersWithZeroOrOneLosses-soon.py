"""
Problem: Find Players With Zero or One Losses (LeetCode 2225)
Chapter: Hashing
Source: soon move (notes OK for the first pass, then re-derive closed-book)

You are given an integer array matches where matches[i] = [winner_i, loser_i]
indicates that the player winner_i defeated player loser_i in a match.

Return a list answer of size 2 where:
  answer[0] is all players that have not lost any matches.
  answer[1] is all players that have lost exactly one match.
Both lists are in increasing order.

Only consider players that have played at least one match.
No two matches have the same outcome.

Example 1:
  Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
  Output: [[1,2,10],[4,5,7,8]]

Example 2:
  Input: matches = [[2,3],[1,3],[5,4],[6,4]]
  Output: [[1,2,5,6],[]]

Constraints:
  1 <= matches.length <= 10^5
  matches[i].length == 2
  1 <= winner_i, loser_i <= 10^5
  winner_i != loser_i
  All matches[i] are unique.
"""

from collections import defaultdict

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        games = defaultdict(int)

        for winner, loser in matches:
            games[loser] += 1
            games[winner] += 0

        winners = []
        losers = []

        for player, count in games.items():
            if count == 0:
                winners.append(player)
            elif count == 1:
                losers.append(player)

        return [sorted(winners), sorted(losers)]

if __name__ == "__main__":
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
    # expected: [[1, 2, 10], [4, 5, 7, 8]]
    print(s.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
    # expected: [[1, 2, 5, 6], []]
