class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        while x > reversed_num:
            reversed_num = (reversed_num * 10) + (x % 10)
            x //= 10
            
        # For even length: x == reversed_num
        # For odd length: x == reversed_num // 10 (removes the middle digit)
        return x == reversed_num or x == reversed_num // 10
