"""
Problem: Simplify Path (LeetCode 71)
Chapter: Stacks / string problems

Given an absolute Unix-style path (always begins with '/'), return its
simplified canonical path.

'.' is the current directory, '..' is the parent directory, repeated '/'
counts as one, and names like '...' are ordinary directory names. The
canonical path starts with '/', joins directories with exactly one '/',
has no trailing '/' (unless it is root), and keeps no '.' or '..' segments.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        stack = []
        
        for path in split_path:
            if path == "." or path == '..' or path == '':
                continue
            else:
                stack.append("/")
                stack.append(path)

        if stack and stack[-1] == '/':
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
    print(Solution().simplifyPath("/a/./b/../../c/"))
    # expected: /c
    print(Solution().simplifyPath("/"))
    # expected: /
    print(Solution().simplifyPath("/home/foo/bar/"))
    # expected: /home/foo/bar
    print(Solution().simplifyPath("/../..//a"))
    # expected: /a
