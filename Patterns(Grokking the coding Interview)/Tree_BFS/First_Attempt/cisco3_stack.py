def prb3(_input):
    s = _input
    if s is None:
        return
    stack = list()
    num = 0
    _string = ""
    idx = 0
    while idx < len(s):
        if s[idx] == ")":
            elem = ""
            idx1 = idx
            while stack:
                if s[idx1] == "(":
                    stack.pop()
                    break
                if s[idx1] != ")":
                    elem = s[idx1] + elem
                idx1 -= 1
            if _string != "":
                num = int(elem)
            else:
                _string = elem

            if num != 0 and _string != "":
                helper_stack(stack, num, _string)
                num, _string = 0, ""

            if idx == len(s) - 1:
                return _string
        else:
            stack.append(s[idx])
        idx += 1
    return _string

def helper_stack(stack, num, _string):
    idx = 0
    while idx < num:
        stack.append(_string[idx])



def main():
    print(prb3("(ab)(3)(cd)(2)"))

main()
