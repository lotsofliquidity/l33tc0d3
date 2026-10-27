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
        stack = []
        split_path = path.split('/')

        for path in split_path:
            if path == '' or path == '.':
                continue
            if path == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path)

        print(stack)
        return '/' + '/'.join(stack)
                



if __name__ == "__main__":
    print(Solution().simplifyPath("/home/"))
    # expected: /home
    print(Solution().simplifyPath("/home//foo/"))
    # expected: /home/foo
    print(Solution().simplifyPath("/home/user/Documents/../Pictures"))
    # expected: /home/user/Pictures
