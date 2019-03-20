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
shu = [False] * n               
pie = [False] * (2 * n - 1)     
na = [False] * (2 * n - 1) 

def findMaxInLine(row):
    maxInLine = 0
    for j in range(n):
        if pointMap[row][j]>maxInLine:
            maxInLine = pointMap[row][j]
    return maxInLine  

maxInLineArr = [0 for x in range(n)]
for k in range(n):
    maxInLineArr[k] = findMaxInLine(k)

def dfs_w_queen(row, numberOfQ, sum):
    global maxSum
    maxInLineSum =0
    if row == n or numberOfQ == p:
        if maxSum < sum:
           maxSum = sum
        return;
    if row > n - p + numberOfQ:
        return;

    for num in range(row,n):
        maxInLineSum += maxInLineArr[num]
    if sum + maxInLineSum < maxSum:
        return;

    for col in range(n):
        j = row + col
        k = n - 1 - row + col       
        if shu[col] or pie[j] or na[k]:
            continue     
        shu[col] = pie[j] = na[k] = True    
        dfs_w_queen(row + 1, numberOfQ + 1,sum + pointMap[row][col])
        shu[col] = pie[j] = na[k] = False 
    if n != p:
        dfs_w_queen(row + 1, numberOfQ, sum)
    
dfs_w_queen(0,0,0)
print(maxSum)
end = datetime.datetime.now()
print (end-start)
f2 = open("output.txt", "w")
f2.write(str(maxSum)+"\n")

