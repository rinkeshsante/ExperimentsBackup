def minKey(key,mstSet):#to find minimum possible edge value 
    min= INF
    for i in range(N):
        if key[i]< min and mstSet[i] ==False:#chack if not used
            min = key[i]
            minIndex = i
    return minIndex

def primsAlgo(gragh):
    key = [INF] *N # cerating space for key values
    parent = [None]*N# to store possible parent of node
    key[0]=0# for first coast is 0
    mstSet=[False]*N#to decide used or not
    parent[0]=-1# parent of first is 0

    for i in range(N):
        u=minKey(key,mstSet)
        mstSet[u]=True# after being used

        for j in range(N):
            if gragh[i][j] > 0 and mstSet[j] ==False and key[j]> gragh[i][j]:
                key[j] = gragh[i][j]
                parent[j]=u

    for i in range(1,N):
        print(parent[i] ,'->',i,' (',gragh[i][parent[i]],')')


N = int(input('enter the size :'))
INF = 999999999
arr = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        arr[i][j] = int(input(f'weight from {i+1} to {j+1} :'))


primsAlgo(arr)