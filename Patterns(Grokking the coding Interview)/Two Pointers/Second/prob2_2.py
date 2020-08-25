def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    
    while (index1 >= 0 or index2 >= 0):
        i1 = get_next_idx(index1, str1)
        i2 = get_next_idx(index2, str2)

        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        if str1[i1] != str2[i2]:
            return False
        
        index1 = i1 - 1
        index2 = i2 - 1
    
    return True

def get_next_idx(idx, str):
    backspace_count = 0
    while idx >= 0:
        if str[idx] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        idx -= 1
    return idx

def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()