def breadth_first_search_iterative(graph, node): 
    ''' 
    - You visit nodes of a tree/graph level by level 
      -> visit all the neighbors of the current vertex (before moving onto 
      next level)   

    ======================================================================= 
    ** TODO ~ Algorithmic Runtime: 


    '''  

    #Keeps track of nodes which have been visited 
    visited = [False] * len(graph) 

    queue = [] 
    queue.append(node)

    while queue: 
        n = queue.pop(0)

        print(n, end = ' ')

        #Iterate through neighbors of current node 
        for neighbor in graph[n]:  
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)


breadth_first_search(
    {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    }, 
    'A'
)