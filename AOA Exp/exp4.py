
def shortestDist(graph, INF, N):

    # to create dist arr (stores tje cost required to reach that position)
    dist = [0] * N

    dist[N - 1] = 0  # distance from last to last will be 0

    # back order
    for i in reversed(range(0, N-1)):

        dist[i] = INF

        for j in range(N):

            if graph[i][j] == INF:
               continue
                # recursive eqn
            dist[i] = min(dist[i], graph[i][j] + dist[j])

    return dist[0]


N = int(input('enter the size :'))
INF = 999999999
arr = [[INF for i in range(N)] for j in range(N)]
#print(arr)
for i in range(N):
    for j in range(i+1, N):
        arr[i][j] = int(input(f'from {i+1} to {j+1} '))

print(shortestDist(arr, INF, N))
