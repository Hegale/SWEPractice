1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
T = int(input())
result_list = []
for test_case in range(1, T + 1):
    result = 0
    l = list(map(int, input().split()))
    C = l[1] - l[0]
    # 예외처리
    if C == 0 :
        result_list.append(0)
        continue
    elif C <= 1 or C < 0:
        result_list.append(-1)
        continue
    # 차가 홀수라면, 3이 무조건 한 번은 필요함.
    if C % 2 == 1 :
        C -= 3
        result += 1
    result += C // 2
    result_list.append(result)
 
for i in range(T):
    print("#%d %d" %(i + 1, result_list[i]))
