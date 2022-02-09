"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        n = len(s)
        answer = i = j = 0

        while i < n and j < n:
            if s[j] not in seen_chars:
                seen_chars.add(s[j])
                j +=1
                answer = max(answer, j - i)
            else:
                seen_chars.remove(s[i])
                i += 1

        return answer

