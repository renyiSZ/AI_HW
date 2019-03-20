import datetime
start = datetime.datetime.now()

f = open("input18.txt", 'r')
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
maxInLineSortedArr = [0 for x in range(n)]
for r in range(n):
    for t in range(r,n):
        maxInLineSumArr[r] += findMaxInLine(t)
    maxInLineSortedArr[r] = findMaxInLine(r)
#maxInLineSortedArr.sort(reverse = True)
def DFS(row, columnFlag, rightDiagFlag, leftDiagFlag,nQ,sum):
    global maxSum
    #maxInLineSum =0
    sort_arr = []
    if row == n or nQ == p:
        if maxSum < sum:
           maxSum = sum
        return;
    if row > n - p + nQ:
        return;

    if n == p:
        if sum + maxInLineSumArr[row] < maxSum:
            return;
    if n != p:
        sumLeftColomnMax = 0
        #sort_arr = sorted(maxInLineSortedArr,reverse = True)
        for u in range(row, n):
            sort_arr.append(maxInLineSortedArr[u])
        sort_arr.sort(reverse = True)
        for tt in range(p-nQ):
            sumLeftColomnMax += sort_arr[tt]
        if sum + sumLeftColomnMax < maxSum:
            return;  

    available = ((1 << n) - 1) & ~(columnFlag | rightDiagFlag | leftDiagFlag)
    #print(bin(available))
    #print("------------")
    while available:
        p2 = available & -available
        available ^= p2
        col = 0
        while p2 >> col:
            col+=1
        DFS(row + 1, columnFlag | p2, (rightDiagFlag | p2) >> 1, (leftDiagFlag | p2) << 1, nQ+1, sum+pointMap[row][n-col] )

    if n != p:
    	p2 = available & -available
    	DFS(row + 1, columnFlag | p2, (rightDiagFlag | p2) >> 1, (leftDiagFlag | p2) << 1, nQ, sum)


DFS(0, 0, 0, 0, 0,0)
print(maxSum)
end = datetime.datetime.now()
print (end-start)
f2 = open("output.txt", "w")
f2.write(str(maxSum)+"\n")
