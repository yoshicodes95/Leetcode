def longestPalindrome(s):
    if len(s) <= 1:
        return s
    longest = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            word = s[i:j]
            if word == word[::-1]:
                if len(word) > len(longest):
                    longest = word
    return longest
print(longestPalindrome("babad"))