class Solution:
    def longestPalindrome(self, s):
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # odd length palindrome
            odd_length_palindrome = expand_around_center(s, i, i)
            if len(odd_length_palindrome) > len(longest):
                longest = odd_length_palindrome

            # even length palindrome
            even_length_palindrome = expand_around_center(s, i, i + 1)
            if len(even_length_palindrome) > len(longest):
                longest = even_length_palindrome

        return longest