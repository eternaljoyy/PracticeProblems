class Graph:  

    def __init__(self, Vertex): 
        self.Vertex = Vertex 
        self.adjacency_list = [[] for i in range(V)]  

    # Create edges between 2 nodes 
    def createEdge(self, node_u, node_v): 
        self.adjacency_list[node_u].append(node_v)

    # Runs DFS 
    def depth_first_search(self, node):  
        ''' 
        Algorithm for traverseing a tree or graph. Keep visiting all nodes
        until reaching a dead end (where there are no more nodes). Then, backtrack until 
        you reach a node which has unvisited adjacent neighbors. 

        ==================================================================================

        ** TODO - Time Complexity: 
        ''' 

        #Check if node is visited 
        
        visited = [False for j in range(self.Vertex)] 

        stack = [node] 

        while len(stack) > 0:

            node = stack.pop() 

            if not visited[node]:
                print(node, end= ' ')
                visited[node] = True 

                #go through the neighbors of the current vertex
                for item in self.adjacency_list:
                    if not visited[item]:
                        stack.append(item)

 