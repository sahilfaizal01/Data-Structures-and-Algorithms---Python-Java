from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self,v1,v2):
        self.graph[v1].append(v2)
    
    def DFS(self,startNode):
    	visited = set()
        stack = []
        stack.append(startNode)
        while(len(stack)):
        	current = stack[-1]
            stack.pop()
            
            if(current not in visited):
            	print(current,end=" ")
                visited.add(current)
            
            for vertex in self.graph[current]:
            	if(vertex not in visited):
                	stack.append(vertex)
       
    
    def printGraph(self):
        for node in self.graph:
            for nextn in self.graph[node]:
                print(node,'->',nextn)

g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)
g.printGraph()
g.DFS(2)
