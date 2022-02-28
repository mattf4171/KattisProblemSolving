for i in sys.stdin:
    # ab = i.split()
    # a = int(ab[0])
    # b = int(ab[1])
    # Solve the test case and output the answer
    testCases = int(input())
    for i in range(testCases):
        firstCommand = [int(x) for x in input()]
        if(testCases == 1): # handles impossible to tell case
            print('impossible')
            break;
        values = set()
        values.add(firstCommand)
