'''Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.'''

# Solution:
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            if s == '':
                return True
            else:
                return False
        if s:
            first_char_match = p[0] in (s[0], '.')
        else:
            first_char_match = False
        if len(p) > 1 and p[1] == '*':
            zero_ocr = self.isMatch(s, p[2:])
            if first_char_match:
                repeat = self.isMatch(s[1:], p)
                return zero_ocr or repeat
            return zero_ocr
        else:
            if first_char_match:
                return self.isMatch(s[1:], p[1:])
            else:
                return False
A = Solution()
print(A.isMatch("aa", "a*"))