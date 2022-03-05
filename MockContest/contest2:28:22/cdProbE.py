n_m = [int(x) for x in input().split(" ")]
n = n_m[0]
m = n_m[1]
count = 0
check_for_duplicates = set()
while:
    for i in range(n):
        num = input()
        check_for_duplicates.add(num)

    for j in range(m):
        num = input()
        if num in check_for_duplicates:
            count +=1
    throw_away = input()
    if throw_away == 0
print(count)