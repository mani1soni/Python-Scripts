from collections import deque

def minim(a, b):
    if a == None:
        return b
    if b == None:
        return a
    if a < b:
        return a
    else:
        return b

g = int(raw_input().strip())
for a0 in xrange(g):
    n,m,x = raw_input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    
    a = map(int, raw_input().strip().split(' '))
    qa = deque(a)
    b = map(int, raw_input().strip().split(' '))
    qb = deque(b)
    
    sum = 0
    count = 0
    #lena = len(qa)
    #lenb = len(qb)
    
    while sum <= x:
        if not qa:
            if not qb:
                break
            else:
                if sum + qb[0] <= x:
                    sum = sum + qb.popleft()
                    count += 1
                else:
                    break
        else:
            if not qb:
                if sum + qa[0] <= x:
                    sum = sum + qa.popleft()
                    count += 1
                else:
                    break
            else:
                if (sum + min(qa[0], qb[0])) <= x:
                    if qa[0] == min(qa[0], qb[0]):
                        sum = sum + qa.popleft()
                        count += 1
                    else:
                        sum = sum + qb.popleft()
                        count += 1
                else:
                    break


        #if (sum + minim(qa[0], qb[0])) <= x:
        #    if qa[0] == minim(qa[0], qb[0]):
        #        sum = sum + qa.popleft()
        #        count += 1
        #    else:
        #        sum = sum + qb.popleft()
        #        count += 1
        #else:
        #    break
    
    print count