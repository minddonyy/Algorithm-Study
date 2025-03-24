matrix = [list(input().strip()) for _ in range(5)]
zip_list = list(map(list,zip(*matrix)))
print(''.join(sum(zip_list, [])))