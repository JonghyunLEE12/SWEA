t = int(input())
for _ in range(t):
    n = int(input())
    people = []
    for i in range(n):
        a,b = map(int,input().split())
        people.append(([a,b]))
    

    people.sort()
    temp = people[0][1]
    cnt = 1

    for j in range(len(people)):
        if temp > people[j][1]:
            cnt += 1
            temp = people[j][1]
    

    print(cnt)