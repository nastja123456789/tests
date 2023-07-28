def circular_array(n, m):
    array = list(range(1, n + 1))
    path = []
    current_index = 0
# пример - 1 2 3 4 5
    while True:
        path.append(array[current_index])
        current_index = (current_index + m - 1) % n
        if current_index==0:
            break
    return path

n,m=map(int, input().split())
result = circular_array(n, m)
print(''.join(map(str,result)))
