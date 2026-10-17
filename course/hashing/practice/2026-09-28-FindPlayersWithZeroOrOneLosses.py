"""
Problem: Find Players With Zero or One Losses (LeetCode 2225)
Chapter: Hashing / counting
Source: course practice

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


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
      counts = defaultdict(int)
       # [1, 3], [2, 3], [3, 6]
       
       # count losses
      for team in matches:
        if team[0] not in counts:
          counts[team[0]] = 0
        else:
          counts += 1
        
        counts[]

        # {1 : 1, 2: 1, 3: 1}





      


      return [[winners], [losers]]
        


if __name__ == "__main__":
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
    print(s.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
