class Solution:
    def isPalindrome(self, s: str) -> bool:
       clean_s = "".join(char.lower() for char in s if char.isalnum())
       reverse = "".join(reversed(clean_s))
       if clean_s == reverse:
        return True
       else:
        return False