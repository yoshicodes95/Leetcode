def isPalindrome(num):
    if num<0:
        return False
    original_num = num
    reversed = 0
    while num > 0:
        reversed = reversed * 10 + num % 10
        num = num//10
    return original_num == reversed

print(isPalindrome(525))

