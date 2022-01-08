n, k = map(int, input().split()) # m은 동전의 개수 / k 는 금액
m = [] # 동전의 개수를 담을 곳 
num = 0

for i in range(n):
    m.append(int(input())) # 동전의 종류를 안에다가 담음

for i in range(n-1, -1, -1): # 맨 끝에서 끝까지 -1씩 내림차순으로 내려옴
    if k == 0:
        break
    if m[i] > k:
        continue
    num += k // m[i]
    k %= m[i]

print(num)