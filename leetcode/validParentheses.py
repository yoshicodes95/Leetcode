def minRemoveToMakeValid(s):
    left_count = 0
    right_count = 0
    stack = []

    for each in s:
        if each == "(":
            left_count += 1
            stack.append(each)
        elif each == ")":
            right_count += 1
            if right_count > left_count:
                right_count -= 1
            else:
                stack.append(each)
        else:
            stack.append(each)
    result = []

    while stack:
        char = stack.pop()
        if char == "(" and left_count > right_count:
            left_count -= 1
        else:
            result.append(char)
    return "".join(reversed(result))

print(minRemoveToMakeValid("lee(t(c)o)de)"))


