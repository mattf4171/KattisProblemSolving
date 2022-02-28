lists = int(input())
for i in range(lists):
    travels = int(input())
    distinctLocations = set()
    for j in range(travels):
        city = input()
        distinctLocations.add(city)
    print(len(distinctLocations))