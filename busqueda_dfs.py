from queue import Queue  # Importamos la libreria Queue
# Implementa colas multiproductor y multiconsumo

"""
Autor: Borja Vinicio
Para iniciar con la generación de los métodos de busqueda se uso librerias 
En python los metodos de busqueda se puede asociar con la teoria de Grafos.
Esta programa es un buen punto de partida si desea profundizar en la implementación de algoritmos relacionados con grafos.
"""


class Grafo:
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

    def __init__(self, numero_de_nodos, dirigido=True):  # Consstructor con sus parametros
        """
        El constructor permite inicializar los atributos del grafo

        Parámetros 
        -----------
            numero_de_nodos: int
                límite de nodos a ingresar
            dirigido: boolean
                simetria del grafo 

        """
        self.m_numero_de_nodos  = numero_de_nodos  # Inicializamos variable m_numero_de_nodos
        # Inicializamos variable m_nodes
        self.m_nodes = range(self.m_numero_de_nodos )

        self.m_dirigido = dirigido  # Inicializamos variable m_dirigido

        # creamos la estructura de un diccionario de datos
        self.m_adjutando_list = {node: set() for node in self.m_nodes}

     # agregamos los parametros en la función agregando_borde
    # agregamos los parametros en la función agregando_borde
    def agregando_borde(self, nodo1, node2, peso=1):
        """Agrega un nuevo grafo

        Se pasa una llave como identificador para su posterior ingreso de valor

        Parametros
        ----------
        node1: int
            valor del primer nodo 
        node2: int
            valor del segundo nodo
        peso: int, valor por defecto 1
            El peso de los grafos poderados

        Si dirigido es falso devolvera True para ingresar como llave el nodo2 y su valor el nodo 1

        Retorna
        -------
        Nada
        """
        self.m_adjutando_list[nodo1].add((node2, peso))

        if not self.m_dirigido:
            self.m_adjutando_list[node2].add((nodo1, peso))

    def imprimiendo_lista_adjuntada(self):
        """Imprime el diccionario
        Recorre el diccionario y muestra los datos tanto la llave como el valor 

        Retorna
        -------
        Nada
        """

        for key in self.m_adjutando_list.keys():  # Realizamos recorrido
            # Se imprmir el recorrido junto la llave y el valor
            print("node", key, ": ", self.m_adjutando_list[key])

    #parametros del metodo comienzo y objetivo
    def dfs(self, comienzo, objetivo, path=[], visitado=set()):
        """_summary_

        Args:
            comienzo (_type_): _description_
            objetivo (_type_): _description_
            path (list, optional): _description_. Defaults to [].
            visitado (_type_, optional): _description_. Defaults to set().

        Returns:
            _type_: _description_
        """
        
        #agregamos un dato a la coleción de tipo arreglo
        path.append(comienzo)
        #agregamos un dato a la coleción de tipo set
        visitado.add(comienzo)
        #en caso que comienzo sea igual a objetivo
        if comienzo == objetivo:
            return path#retorna el arreglo
        for (vecino, peso) in self.m_adjutando_list[comienzo]:
            #recuperamos los valores del diccionario
            if vecino not in visitado:#en caso que este visitado 
                resultado = self.dfs(vecino, objetivo, path, visitado)
                if resultado is not None:
                    return resultado
        path.pop()
        return None


if __name__ == "__main__":
    #### Programa principal #####
    # Creamos una instancia de la clase Grafo con 5 nodos
    grafo = Grafo(5, dirigido=False)

    grafo.agregando_borde(0, 1)
    grafo.agregando_borde(0, 2)
    grafo.agregando_borde(1, 3)
    grafo.agregando_borde(2, 3)
    grafo.agregando_borde(3, 4)

    # Imprmiendo la lista adyadencia con el formato nodo n: {(node, peso)}
    grafo.imprimiendo_lista_adjuntada()

    traversal_path = []
    traversal_path = grafo.dfs(0, 3)
    print(f" El camino transversal del nodo 0 al nodo 3 es {traversal_path}")


# Execution Steps
# Current Node	Path	visitado
# 0	[0]	{0}
# 1	[0, 1]	{0, 1}
# 3	[0, 1, 3]	{0, 1, 3}
