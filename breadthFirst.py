"""
Breadth-first search and Depth-first search in python are algorithms used to 
traverse a graph or a tree. They are two of the most important topics that any 
new python programmer should definitely learn about. Here we will study what 
breadth-first search in python is, understand how it works with its algorithm, 
implementation with python code, and the corresponding output to it. Also, we 
will find out the application and uses of breadth-first search in the real world.

As discussed earlier, Breadth-First Search (BFS) is an algorithm used for 
traversing graphs or trees. Traversing means visiting each node of the graph. 
Breadth-First Search is a recursive algorithm to search all the vertices of a 
graph or a tree. BFS in python can be implemented by using data structures like 
a dictionary and lists. Breadth-First Search in tree and graph is almost the same. 
The only difference is that the graph may contain cycles, so we may traverse to 
the same node again.

Before learning the python code for Breadth-First and its output, 
let us go through the algorithm it follows for the same. We can take the example 
of Rubik’s Cube for the instance. Rubik’s Cube is seen as searching for a path to
convert it from a full mess of colors to a single color. So comparing the Rubik’s 
Cube to the graph, we can say that the possible state of the cube is corresponding 
to the nodes of the graph and the possible actions of the cube is corresponding to 
the edges of the graph.

As breadth-first search is the process of traversing each node of the graph, a 
standard BFS algorithm traverses each vertex of the graph into two parts: 1) 
Visited 2) Not Visited. So, the purpose of the algorithm is to visit all the 
vertex while avoiding cycles.

BFS starts from a node, then it checks all the nodes at distance one from the 
beginning node, then it checks all the nodes at distance two, and so on. So as to 
recollect the nodes to be visited, BFS uses a queue.

The steps of the algorithm work as follow:

 1-> Start by putting any one of the graph’s vertices at the back of the queue.
 2-> Now take the front item of the queue and add it to the visited list.
 3-> Create a list of that vertex's adjacent nodes. Add those which are not within 
 the visited list to the rear of the queue.
 4-> Keep continuing steps two and three till the queue is empty.
Many times, a graph may contain two different disconnected parts and therefore 
to make sure that we have visited every vertex, we can also run the BFS algorithm 
at every node.

Implementation algorithm in python:

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling
"""

def breadthFirstSearch(graph, start):
    visited = set() # Множество для отслеживания посещенных узлов
    queue = [start] # Очередь для обхода в ширинуб начиная с начального узла

    while queue:
        current_node = queue.pop(0) # Извлечение текущего узла из очереди

        if current_node not in visited:
            # вывод текущего узла
            print(current_node, end=' ')
            # отметка узла как посещенного
            visited.add(current_node)
            # добавление  сщседей в очередь для дальнейшего исследования
            queue.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)

if __name__ == '__main__':
  graph = {
      'A': ['B', 'C'],
      'B': ['A', 'D', 'E'],
      'C': ['A', 'F', 'G'],
      'D': ['B'],
      'E': ['B'],
      'F': ['C'],
      'G': ['C']
  }

  print(breadthFirstSearch(graph, 'A'))