"""
[MEDIUM]

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file
system, convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory
up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any
other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory
(i.e., no period '.' or double period '..')

Return the simplified canonical path.



Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for i in path.split("/"):
            if i == '..':
                if stack:
                    stack.pop()
            elif i not in ('', '.'):
                stack.append(i)

        return "/" + "/".join(stack)

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We split the string based on /'s so that we will either have only file names, ..'s, or .'s. 
    If the current characters we are looking at is a .., then we can just pop the last item in the stack, but we need to
    make sure the stack is not empty first. 
    If the current characters is not '.', or empty, then we can just add those characters to the stack. 
    After we finish the for loop, we just have to join the stack with /'s and add a / in the beginning. 
    
    Since we go through the for loop once, the time complexity is O(n). 
    The space complexity is O(n) since we are creating a stack of items in the string, and we are creating a new string. 
"""