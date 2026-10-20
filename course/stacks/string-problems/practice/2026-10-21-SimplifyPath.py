"""
Problem: Simplify Path (LeetCode 71)
Chapter: Stacks / string problems

Given an absolute Unix-style path (always begins with '/'), return its
simplified canonical path.

Rules:
  '.'  → current directory (ignore)
  '..' → parent directory (pop one level; stay at root if empty)
  '//' → treat as a single '/'
  '...' / '....' → valid directory names

Canonical form:
  starts with '/'
  directories separated by exactly one '/'
  no trailing '/' unless the path is root
  no '.' or '..' segments left

Example 1:
  Input: path = "/home/"
  Output: "/home"

Example 2:
  Input: path = "/home//foo/"
  Output: "/home/foo"

Example 3:
  Input: path = "/home/user/Documents/../Pictures"
  Output: "/home/user/Pictures"

Example 4:
  Input: path = "/../"
  Output: "/"

Example 5:
  Input: path = "/.../a/../b/c/../d/./"
  Output: "/.../b/d"
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for ch in path:
            if stack[-1] and ch == '/':
                continue
            else:
                stack.append(ch)
            
            
        if stack[-1] == "/":
            stack.pop()
            
        
        
        return "".join(stack)
        


if __name__ == "__main__":
    print(Solution().simplifyPath("/home/"))
    # expected: /home
    print(Solution().simplifyPath("/home//foo/"))
    # expected: /home/foo
    print(Solution().simplifyPath("/home/user/Documents/../Pictures"))
    # expected: /home/user/Pictures
    print(Solution().simplifyPath("/../"))
    # expected: /
    print(Solution().simplifyPath("/.../a/../b/c/../d/./"))
    # expected: /.../b/d
