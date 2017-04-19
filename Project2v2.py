def makeMatrix():
    print("Enter Matrix parameters")
    n = int(input("# of rows: "))
    m = int(input("# of columns: "))
    matrix = [[0 for x in range(m)]for x in range(n)]
    for i in range (n):
        for j in range (m):
            matrix[i][j]=int(input("Enter the elements of the matrix: "))
    return (matrix)
	

def findDist(costArray,queueArray):
	minDist = float("INF")
	minIndex = -1
	for i in range(len(costArray)):
		if costArray[i] < minDist and i in queueArray:
			minDist = costArray[i]
			minIndex = i
	return minIndex

def dijkstra(matrix,startNode):
	row = len(matrix)
	column = len(matrix[0])
	costArray = [float("INF")]*row
	queueArray = []	
	costArray[startNode] = 0
	parentArray = [-1]*row
	
	for i in range(row):
		check = 0
		for j in range(column):
			if matrix[i][j] != 0:
				check = 1
		if check == 1:
			queueArray.append(i)
	
	print('Table')
	while queueArray:
		
		print(costArray[1::])
		for i in range(row):
			check = 0
			for j in range(column):
				if matrix[i][j] != 0:
					check = 1
			if check == 0:
				costArray[i] = float("INF")
	
		x = findDist(costArray, queueArray)
		if x in queueArray:
			queueArray.remove(x)
		
		for i in range(column):
			if matrix[x][i] and i in queueArray: 
				if costArray[x] + matrix[x][i] < costArray[i]:
					costArray[i] = costArray[x] + matrix[x][i]
					parentArray[i] = x
		
	result(matrix,costArray,parentArray)

def Route(parent, j):
    if parent[j] == -1 :
        print (j+1, end = " ")
        return
    Route(parent , parent[j])
    print (j+1, end = " ")
     
def result(matrix,cost, parent):
    begin = 0
    print("Node \t\tTotal Cost\tRoute")
    for i in range(0, len(cost)):
       	if i==3:
            print("%d to %d \t\t%d \t\t" % (begin+1, i+1, cost[i]), end = " "),
            Route(parent,i)
            deleteRoute(matrix,parent, i)
            print(" ")

def deleteRoute(matrix, parent, j):
	if parent[j] == -1:
		return
	deleteRoute(matrix,parent, parent[j])
	matrix[j][parent[j]] = 0
	matrix[parent[j]][j] = 0

#makeMatrix not used , matrix hardcoded based on example

matrix =[[0,10,2,0,0,0,8],
		[10,0,2,16,2,0,0],
		[2,2,0,8,0,1,0],
		[0,16,8,0,2,6,1],
		[0,2,0,2,0,0,4],
		[0,0,1,6,0,0,1],
		[8,0,0,1,4,1,0]]

print ('\nPath One')
dijkstra(matrix,0)
	
print ('\nPath Two')
dijkstra(matrix,0)
	
	
print ('\nPath Three')
dijkstra(matrix,0)
	