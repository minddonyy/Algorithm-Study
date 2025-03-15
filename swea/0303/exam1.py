import itertools

arr = ["박물관", "공원", "미술관"]

print(list(itertools.permutations(arr,3)))


def per(selected, remain):
    if not remain:
        print(selected)
    else:
        for i in range(len(remain)):
            select_i = remain[i]
            remain_list = remain[:i] + remain[i+1:]
            per(selected + [select_i], remain_list)

print(per([], arr))