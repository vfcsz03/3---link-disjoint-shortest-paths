# 3-link-disjoint-shortest-paths

  For this project the Dijkstra algorithm was used to determine the shortest path. Shortest path here is defined as the minimum number of hops or minimum distance required to get from start to end. After finding the shortest path the same path would then be deleted from the routing table. Dijkstra is then performed again on the updated table until all possible routes are exhausted. For this example, there are only 3 possible routes because start node “1” only has 3 distinct paths. 
	
  The code demonstrates functionality with the given example first through user input. It will then take the matrix and process it to print shortest path (and complete routing table for that instance) from source node 1 to end node 4, for each of the 3 shortest path disjoint links and the total distance of each of the 3 shortest path disjoint links.

For the matrix:
	matrix =[[0,10,2,0,0,0,8],
		[10,0,2,16,2,0,0],
		[2,2,0,8,0,1,0],
		[0,16,8,0,2,6,1],
		[0,2,0,2,0,0,4],
		[0,0,1,6,0,0,1],
		[8,0,0,1,4,1,0]]
		
![alt text](https://github.com/vfcsz03/3---link-disjoint-shortest-paths/blob/master/output.png)
