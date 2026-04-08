class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        return clean.strip() == clean[::-1].strip()