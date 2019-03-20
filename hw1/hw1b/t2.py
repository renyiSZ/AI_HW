import datetime
start = datetime.datetime.now()

f = open("input13.txt", 'r')
n = int(f.readline().rstrip('\n'))
p = int(f.readline().rstrip('\n'))
s = int(f.readline().rstrip('\n'))

print("n: "+str(n))
print("p: "+str(p))
#import numpy
pointMap = [[0 for x in range(n)] for y in range(n)]

i = 1
while i <= int(s*12):
    line = f.readline().rstrip('\n')
    input = line.split(",")
    pointMap[int(input[1])][int(input[0])]+=1
    i += 1

for arr in pointMap:
    line = ""
    for num in arr:
        line += str(num)+" "
    print("[ "+line+"]")


maxSum = 0
def findMaxInLine(row):
    maxInLine = 0
    for j in range(n):
        if pointMap[row][j]>maxInLine:
            maxInLine = pointMap[row][j]
    return maxInLine  


maxInLineSumArr = [0 for x in range(n)]
for r in range(n):
    for t in range(r,n):
        maxInLineSumArr[r] += findMaxInLine(t)

def DFS(row, shu, pie, na,nQ,sum):
    global maxSum
    maxInLineSum =0
    
    if row == n or nQ == p:
        if maxSum < sum:
           maxSum = sum
        return;
    if row > n - p + nQ:
        return;

    if sum + maxInLineSumArr[row] < maxSum:
        return;

    available = ((1 << n) - 1) & ~(shu | pie | na)
    while available:
        p2 = available & -available
        available ^= p2
        col = 0
        while p2 >> col:
            col+=1
        DFS(row + 1, shu | p2, (pie | p2) >> 1, (na | p2) << 1, nQ+1, sum+pointMap[row][n-col] )

    if n != p:
    	p2 = available & -available
    	DFS(row + 1, shu | p2, (pie | p2) >> 1, (na | p2) << 1, nQ, sum)


DFS(0, 0, 0, 0, 0,0)
print(maxSum)
end = datetime.datetime.now()
print (end-start)
f2 = open("output.txt", "w")
f2.write(str(maxSum)+"\n")
