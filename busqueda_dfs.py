from queue import Queue

class Graph:
      """
    Una clase que representa un Grafo

    ...
    Atributos
    ---------------------
    numero_de_nodos : int
        cantidad de nodos del grafo
    dirigido: boolean
        especifica si es dirigido o no
    m_nodes: int 
        almacena la secuencia de números 
    m_adjutando_lista: estructura de un  diccionario {}
        implementa una lista de adyacencia
    ---------------------

    Métodos
    -------
    agregando_borde(self, node1, node2, peso=1):
        Agrega un nuevo grafo
    imprimiendo_lista_adjuntada(self):
         Recorre el diccionario y muestra los datos tanto la llave como el valor 
    bfs_traversal(self, nodo_inicio):
        Imprimir recorrido BFS
    """
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
		
        # Directed or Undirected
        self.m_directed = directed
		
        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}      
	
    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))
    
    # Print the graph representation
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])

    def dfs(self, start, target, path = [], visited = set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        for (neighbour, weight) in self.m_adj_list[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None


if __name__ == "__main__":
    #### EXAMPLE #####

    # Create an instance of the `Graph` class
    # This graph is undirected and has 5 nodes
    graph = Graph(5, directed=False)

    # Add edges to the graph with default weight=1
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    # Print adjacency list in the form node n: {(node, weight)}
    graph.print_adj_list()

    traversal_path = []
    traversal_path = graph.dfs(0, 3)
    print(f" The traversal path from node 0 to node 3 is {traversal_path}")




# Execution Steps
# Current Node	Path	Visited
# 0	[0]	{0}
# 1	[0, 1]	{0, 1}
# 3	[0, 1, 3]	{0, 1, 3}