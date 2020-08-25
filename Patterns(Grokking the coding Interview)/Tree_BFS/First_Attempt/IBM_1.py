import math

def closest(s, queries):
    if s is None:
        return

    my_dict = dict()
    result = list()

    for idx in range(len(s)):
        _char = s[idx]
        if _char not in my_dict:
            my_dict[_char] = []
        my_dict[_char].append(idx)

    for idx in queries:
        _char = s[idx]
        my_list = my_dict[_char]
        # result_num = math.inf
        # result_prev = result_num
        # my_idx = -1
        # len_list = len(my_list)
        # for idx1 in range(len(my_list)):
        #     if my_list[idx1] != idx:
        #         result_prev = result_num
        #         result_num = min(result_num, abs( my_list[idx1] - idx))
        #         if result_num != result_prev:
        #             my_idx = idx1
        new_idx = my_list.index(idx)
        if len(my_list) <= 1:
            result.append(-1)
        else:
            p, n = new_idx - 1, new_idx + 1
            p_ans, n_ans = math.inf, math.inf
            if p >= 0 and n < len(my_list):
                p_ans = new_idx - p
                n_ans = n - new_idx
                
                if p_ans <= n_ans:
                    result.append(p)
                else:
                    result.append(n)
            
            elif new_idx == 0:
                result.append(my_list[1])
            elif new_idx == -1:
                result.append(my_list[-2])
            
            else:
                result.append(-1)


        # if result_num != math.inf:
        #     result.append(my_list[my_idx])
        # else:
        #     result.append(-1)

    return result

def main():
    print(closest("Hackerrank", [4,1,6,8]))
    print(closest("aaaa", [0,1,2,3]))
    print(closest("sam", [1]))


main()