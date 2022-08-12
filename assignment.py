def mincost(N,K,prices,tasks):
    
    #tasks = [10, 20]
    #cost = [10, 50]
    #totalcost = 0
    #for i in range(len(tasks)):
        #totalcost += tasks[i]*cost[i]
    #print(totalcost)


    # N = 2
    # K = 50
    # prices = [10, 50]
    # tasks = [10, 20]

    _zip = zip(prices, tasks)
    prices_sorted = prices.copy()
    prices_sorted.sort(reverse=True)
    tasks_sorted= [x for _, x in sorted(_zip, reverse=True)]
    # print(tasks_sorted)
    # print(prices_sorted)
    #tasks.sort()
    # couter = 0
    
    final_cost = []
    for i in range(N):
        # print(i)
        totalcost = 0
        # print('---------------------------------------------', i)
        for j in range(i):
            # print(j)
            totalcost += (tasks_sorted[j]+K)*prices_sorted[j]
            # print(str(tasks_sorted[j]) + ' x ' + str(prices_sorted[j]))
            # print(j)
        totalcost += prices_sorted[i]*(sum(tasks_sorted[i:])+K)
        # print(totalcost)
        # print(tasks_sorted[i:])
        # print(prices_sorted[i])
        # print("-------------")
        
        final_cost.append(totalcost)
        # print(final_cost)
    print(min(final_cost))
        

T = int(input())
test_cases = []


for i in range(T):
    N,K = str(input()).split(' ')
    prices = [int(x) for x in str(input()).split(' ')]
    tasks = [int(x) for x in str(input()).split(' ')]
    test_cases.append([int(N), int(K), prices, tasks])

for test_case in test_cases:
    mincost(test_case[0], test_case[1], test_case[2], test_case[3])


