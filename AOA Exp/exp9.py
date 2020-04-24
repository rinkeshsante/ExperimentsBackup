def jobSchedule(arr,t):
    N =len(arr)
    # sorting according to price
    for i in range(N):
        for j in range(N-i-1):
            if arr[j][2] < arr[j+1][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    timeline = [None]*t

    for i in range(N):
        for j in reversed(range(t)):
            if timeline[j] is None and j < arr[i][1]:
                timeline[j]= arr[i][0]
                break
                
    return timeline

N = int(input('enter the number of jobs:'))
arr = [None for j in range(N)]
for i in range(N):
    name,dl,p= input('enter the name,deadline and price for job :').split()
    arr[i]=[name,int(dl),int(p)]

t = int(input('enter length of available timeline '))
print(jobSchedule(arr,t))