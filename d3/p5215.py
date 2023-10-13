# 사용 가능 재료, 남은 칼로리를 인자로 받아 낼 수 있는 최대 점수를 계산
# 인자 idx = 이 단계에서 수를 변경할(핵심적으로 다룰) 재료의 인덱스. 즉, 깊이
def get_max_score(cal, idx):
    # print("현 재료:%d, cal:%d" %(idx, cal), end = '')
    if idx >= ing_count or cal <= 0:
        return 0
    # 현재 상황이 마지막 재료라면, 더 이상 경우의 수가 없으므로 최대점수반환
    if idx == ing_count - 1 :
        if ing[idx][1] <= cal:
            return ing[idx][0]
        return 0
    now_max = 0
    # 현 깊이의 재료를 하나씩 줄여가며 다음 결과의 최대점수 찾기
    for i in range(1, -1, -1):
        now_score = i * ing[idx][0]
        now_cal = i * ing[idx][1]
        if now_cal > cal:
            continue
        # print(" i : ", i, "now_score:", now_score)
        # 다음 깊이 재료 점수. 아래 깊이에서 가능한 재료점수 최댓값계산
        inner_score = get_max_score(cal - now_cal, idx + 1)
        # print(" inner_score: ", inner_score)
        if now_score + inner_score > now_max:
            now_max = now_score + inner_score
    return (now_max)
 
# 재료의 가성비 순대로 리스트 정렬
def sort_ing():
    ing.sort(key = lambda x:(x[0]/x[1]))
 
 
T = int(input())
result_list = []
for test_case in range(T):
    # 재료 개수와 최대 칼로리 입력받기
    ing_count, max_cal = map(int, input().split())
    ing = [] # [재료 점수, 재료 칼로리] 쌍을 요소로 가짐.
    for i in range(ing_count):
        tmp = list(map(int, input().split()))
        ing.append(tmp)
    sort_ing()
    # print("ing = ", ing)
    result_list.append(get_max_score(max_cal, 0))
 
for i in range(T):
    print("#%d %d" %(i + 1, result_list[i]))
