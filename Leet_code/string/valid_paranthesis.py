# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Constraints:

# 1 <= s.length <= 10 ki power 4
# s consists of parentheses only '()[]{}'.

# Python range (start, stop, step)

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false
class Solution:
    def isValid(self, s: str) -> bool:
        temp_stack = []
        brackets_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        opening_brackets = set(['(','[','{'])
        for x in s:
            if x in opening_brackets:
                temp_stack.append(x)
            elif temp_stack and temp_stack[-1] == brackets_map[x]:
                temp_stack.pop()
            else:
                return False
        if temp_stack:
            return False
        else:
            return True
# TC = O(N)
# SC = O(N)