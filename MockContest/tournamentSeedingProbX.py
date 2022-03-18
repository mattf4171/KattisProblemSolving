n_k = [int(x) for x in input().split()]
lines = pow(2,n_k[0])
values = []
close_occ = 0
for i in range(lines):
    line = int(input())
    values.append(line)
values.sort()
for i in range(len(values)-1):
    for j in range(1, len(values)):
        if i == j:
            continue
        if values[j] - values[i] <= n_k[1]:
            close_occ+=1
print(int(close_occ/2))