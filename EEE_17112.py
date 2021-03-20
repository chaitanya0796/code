n = int(input())
d = dict()
for i in range(n):
    k = input().split(': ')
    d[int(k[1])] = k[0]

k = list(d.keys())
k.sort()
M = int(input()) - 1
final = []
for i in range(n - M):
    final.append(k[i + M] - k[i])

kk = 0
mn = final[0]
for i in range(1, n - M):
    if (mn > final[i]):
        mn = final[i]
        kk = i
for i in k[kk:kk + M + 1]:
    print(d[i], ": ", i)

print("And the difference between the chosen goodie with highest price and the lowest price is " + str(mn))