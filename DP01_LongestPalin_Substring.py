def longestPalindrome(s: str) -> str:
    if not s or len(s) == 0:
        return ""

    start, end = 0, 0

    def expandAroundCenter(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome
        return right - left - 1

    for i in range(len(s)):
        # Odd-length palindrome
        len1 = expandAroundCenter(i, i)
        # Even-length palindrome
        len2 = expandAroundCenter(i, i + 1)
        # Take the maximum of the two lengths
        max_len = max(len1, len2)

        if max_len > end - start:
            # Update the start and end pointers
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]
