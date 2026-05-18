class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for i in s:
            if ('A' <= i <= 'Z'):
                ns = ns + chr(ord(i) - ord('A') + ord('a'))
            elif ('a' <= i <= 'z'):
                ns = ns + i
            elif ('0' <= i <= '9'):
                ns = ns + i
        return ns == ns[::-1]