class Graph:  

    def __init__(self, Vertex): 
        self.Vertex = Vertex 
        self.adjacency_list = [[] for i in range(V)]  

    # Create edges between 2 nodes 
    def createEdge(self, node_u, node_v): 
    

    # Runs DFS 
    def depth_first_search(graph, visited):  
    ''' 
    Algorithm for traverseing a tree or graph. Keep visiting all nodes
    until reaching a dead end (where there are no more nodes). Then, backtrack until 
    you reach a node which has unvisited adjacent neighbors. 

    ==================================================================================

    Time Complexity: 
    ''' 

    #Check if node is visited 
    
    visited = [] 

    unvisited_node_stack = []  



    #Traverse through the graph 