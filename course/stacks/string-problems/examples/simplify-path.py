"""
Problem: Simplify Path (LeetCode 71)
Chapter: Stacks / string problems
Source: course practice problem — stack of path segments.

Companion file: ../practice/2026-10-21-SimplifyPath.py is the attempt.

Idea: split on '/'. Empty and '.' segments are skip. '..' pops the stack
      (no-op at root). Anything else — including '...' — is a real name and
      gets pushed. Join with '/' and prefix a leading slash.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/home/"))                              # /home
    print(sol.simplifyPath("/home//foo/"))                         # /home/foo
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))    # /home/user/Pictures
    print(sol.simplifyPath("/../"))                                # /
    print(sol.simplifyPath("/.../a/../b/c/../d/./"))               # /.../b/d
