# Input
# The first line contains an integer π (1β€πβ€100) denoting the number of events. Each of the next π lines contains two integers π π and π‘π (1β€π πβ€π‘πβ€365) denoting that the πth event will be held from π π to π‘π (inclusive), and free food is served for all of those days.

# Output
# The output contains an integer denoting the number of days in which free food is served by at least one event.

daysOfEvents = int(input())

# use set, doesnt allow duplicates
freeFoodDays = set()

for i in range(daysOfEvents):
    days_range = [int(x) for x in input().split(" ")]
    # print(days_range)
    # create new list with all values within range of endpoints
    for x in range(days_range[0], days_range[0]+(days_range[1] - days_range[0]) +1):
        # print(x)
        freeFoodDays.add(x)
    for j in range(len(days_range)):
        freeFoodDays.add(days_range[j])

for i in range(len(freeFoodDays)):
    if(i == len(freeFoodDays)-1):
        print(i+1)