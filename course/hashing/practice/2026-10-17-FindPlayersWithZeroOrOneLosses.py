"""
Problem: Find Players With Zero or One Losses (LeetCode 2225)
Chapter: Hashing / counting
Source: cold revisit — no notes/hints

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




# Return a list answer of size 2 where:
#   answer[0] is all players that have not lost any matches.
#   answer[1] is all players that have lost exactly one match.
# Both lists are in increasing order.

from collections import defaultdict

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        count = defaultdict(int)

        for team1, team2 in matches:
              count[team2] += 1
              count[team1] += 0

        losers = []
        winners = []

        for k, v in count.items():
            if v == 0:
                winners.append(k)

            if v == 1:
                losers.append(k)
            

        return [sorted(winners), (sorted(losers))]

        

if __name__ == "__main__":
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
    # expected: [[1, 2, 10], [4, 5, 7, 8]]
    print(s.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
    # expected: [[1, 2, 5, 6], []]
