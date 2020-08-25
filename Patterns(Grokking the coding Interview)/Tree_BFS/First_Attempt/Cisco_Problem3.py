def math():
        decode = ''
        nums = []
        chars = []
        index = 0
        while index < len(s):
            if s[index].isdigit():
                mul = ''
                while s[index].isdigit():
                    mul += s[index]
                    index += 1
                mul = int(mul)
                nums.append(mul)
            elif s[index] == '(':
                chars.append(decode)
                decode = ''
                index += 1
            elif s[index] == ')':
                temp = chars.pop()
                temp += decode * nums.pop()
                decode = temp
                index += 1
            else:
                decode += s[index]
                index += 1
        return decode