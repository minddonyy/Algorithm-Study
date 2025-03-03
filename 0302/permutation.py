def perm(selected, remain):
    if not remain:
        print(selected)
    else:
        for i in range(len(remain)):
            select_i = remain[i]
            print("select_i", select_i)
            remain_list = remain[:i] + remain[i+1:]
            print("remain_list",remain_list)
            perm(selected + [select_i] ,remain_list)


perm([], [1,2,3])



def perm(selected, remain):
    if not remain:
        print(selected)
    else:
        for i in range(len(remain)):
            select_i = remain[i]
            remain_list = remain[:i] + remain[i+1:]
            perm(selected+[select_i], remain_list)
