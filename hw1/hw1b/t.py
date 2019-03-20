import time

n = 3
pp=2
count = 0

def DFS(row, shu, pie, na,nQ):
    global count
    available = ((1 << n) - 1) & ~(shu | pie | na)
    if row > n - pp + nQ:
        return;
    while available:
        p = available & -available
        index = 0
        while p >> index:
        	index+=1
        print(str(row)+" "+str(index))
        available ^= p
        if row == n - 1 or nQ == pp-1:
            count += 1
            print("-----------")
        else:
            DFS(row + 1, shu | p, (pie | p) >> 1, (na | p) << 1, nQ+1)
    if n != pp:
    	p = available & -available
    	DFS(row + 1, shu | p, (pie | p) >> 1, (na | p) << 1, nQ)

tic = time.time()
DFS(0, 0, 0, 0,0)
toc = time.time()
print "Total solutions: %d" % count
print "Elapsed time: %f seconds" % (toc - tic)
