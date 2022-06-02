from queue import Queue #Importamos la libreria Queue
#Implementa colas multiproductor y multiconsumo

"""
Autor: Borja Vinicio
Para iniciar con la generación de los métodos de busqueda se uso librerias 
En python los metodos de busqueda se puede asociar con la teoria de Grafos.
Esta programa es un buen punto de partida si desea profundizar en la implementación de algoritmos relacionados con grafos.
"""

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
    agregando_borde(self, nodo1, node2, peso=1):
        Agrega un nuevo grafo
    imprimiendo_lista_adjuntada(self):
         Recorre el diccionario y muestra los datos tanto la llave como el valor 
    bfs_traversal(self, nodo_inicio):
        Imprimir recorrido BFS
    """
    
    def __init__(self, num_of_nodes, directed=True):#Consstructor con sus parametros
        """
        El constructor permite inicializar los atributos del grafo

        Parámetros 
        -----------
            numero_de_nodos: int
                límite de nodos a ingresar
            dirigido: boolean
                simetria del grafo 

        """
        self.m_num_of_nodes = num_of_nodes#Inicializamos variable m_numero_de_nodos
        self.m_nodes = range(self.m_num_of_nodes)#Inicializamos variable m_nodes 
		
        self.m_directed = directed#Inicializamos variable m_dirigido
		
        self.m_adj_list = {node: set() for node in self.m_nodes}# creamos la estructura de un diccionario de datos         
	

    def agregando_borde(self, nodo1, node2, weight=1):#agregamos los parametros en la función agregando_borde
        self.m_adj_list[nodo1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((nodo1, weight))
    

    def imprimiendo_lista_adjuntada(self):
        """Imprime el diccionario
        Recorre el diccionario y muestra los datos tanto la llave como el valor 

        Retorna
        -------
        Nada
        """
        
        for key in self.m_adj_list.keys():#Realizamos recorrido
            print("node", key, ": ", self.m_adj_list[key])#Se imprmir el recorrido junto la llave y el valor


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

    graph = Graph(5, directed=False)

 
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_adj_list()

    traversal_path = []
    traversal_path = graph.dfs(0, 3)
    print(f" The traversal path from node 0 to node 3 is {traversal_path}")




# Execution Steps
# Current Node	Path	Visited
# 0	[0]	{0}
# 1	[0, 1]	{0, 1}
# 3	[0, 1, 3]	{0, 1, 3}