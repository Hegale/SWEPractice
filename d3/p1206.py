def get_max(height):
    max = 0
    for h in height:
        if h > max:
            max = h
    return max
 
result_list = []
for test_case in range(10):
    result = 0
    # 건물 개수 및 각 건물의 높이 입력받기
    N = int(input())
    l = list(map(int, input().split()))
    for i in range(2, N - 2):
        max = get_max([l[i - 2], l[i - 1], l[i + 1], l[i + 2]])
        if (l[i] > max):
            result += l[i] - max
    result_list.append(result)
 
for i in range(10):
    print("#%d %d" %(i + 1, result_list[i]))
     
    #0 0 3 5 2 4 9 0 6 4 0 6 0 0
