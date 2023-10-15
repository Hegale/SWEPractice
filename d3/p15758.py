
# start부터 시작하는 문자열이 길이 len의 토큰 str과 일치하는지 확인
def is_same(str, start, size):
   if (len(start) < size):
      return False
   for i in range(size):
      if str[i] != start[i]:
         return False
   return True

# is_same을 이용해 길이 len이 실제로 토큰이 맞는지 확인
def is_token(str, size):
   # 문자열 전체가 토큰인 상황이 아니려면, 최소 아래 for문이 한번은 돌아가야함
   if size * 2 > len(str) :
      return False
   for i in range(size, len(str) - size + 1, size):
      if is_same(str, str[i:], size) == False:
         return False
   return True

# 토큰이 존재한다면 그 길이를 반환.
def find_token(str):
   first = str[0]
   # 첫 문자열과 같은 문자열을 찾기
   for i in range(1, len(str)):
      # 첫 번째 문자를 찾은 경우
      if str[i] == first:
         if is_token(str, i) == True:
            return i
   # 토큰이 존재하지 않는다면 전체 문자열 길이를 반환
   return len(str)

T = int(input())
result_list = []
for test_case in range(T):
   a, b = input().split()
   a_len = find_token(a)
   b_len = find_token(b)
   #print("alen = %d, blen = %d" %(a_len, b_len))
   if a_len == b_len and is_same(a, b, a_len):
      answer = "yes"
   else:
      answer = "no"
   result_list.append(answer)

for i in range(T):
   print("#%d %s" %((i + 1), result_list[i]))
