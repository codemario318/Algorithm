people = [70, 50, 80, 50]
people = [70,80,50]
limit =100
cnt = 0
head = 0
tail = 1
sort_w = sorted(people)
sort_w[2:3]
while(tail <= len(people)):
    print('start:',head,tail)
    if sum(sort_w[head:tail]) < limit:
        print('appned',sort_w[head:tail])
        tail += 1
    elif sum(sort_w[head:tail]) == limit:
        print('same',sort_w[head:tail])
        cnt += 1
        head = tail
        tail = head + 1
    else:
        print('go:',sort_w[head:tail])
        cnt += 1
        head = tail -1
        tail = head + 1
    print('end:',head,tail,cnt)
return cnt + 1


for i,p1 in enumerate(sorted(people)):
    boat = [p1]
    if tail > i:
        print('bigtail',tail,j)
        continue
    for j,p2 in enumerate(people[tail:],tail):

        if (sum(boat) + p2 <= limit):
            boat.append(p2)
            print('append:',tail)
            tail = j+1
        else:
            print('limit:',tail,cnt)
            cnt += 1
            tail = j+1
            break
cnt
