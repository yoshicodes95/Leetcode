def calculate(s):
    stack = []
    s += '+'
    pre_op = '+'
    num = 0
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c == " ":
            pass
        else:
            if pre_op == "+":
                stack.append(num)
            elif pre_op == "-":
                stack.append(-num)
            elif pre_op == "*":
                operant = stack.pop()
                stack.append((operant*num))
            elif pre_op == "/":
                operant = stack.pop()
                # if operant < 0:
                stack.append(int(operant/num))
                #-5 / 2 == -2 
                #-5 // 2 == -3
                # else:
                #     stack.append(operant//num)
            num = 0
            pre_op = c
    return sum(stack)

print(calculate("3-5 /2 + 4 *2"))