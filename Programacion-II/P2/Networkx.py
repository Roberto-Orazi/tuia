'''
NetworkX es un paquete de python para crear, manipular y estudiar grafos.
Trae incluido muchos algoritmos para grafos
'''

# El metodo y el sufijo para importarlo suele ser asi
import networkx as nx
G = nx.Graph() # aca creamos un grafo G sin vertice ni arista

# Para agregar vertices/nodos de a 1 y usamos elnombredelgrafo.add_node(1)
G.add_node(1)

# Podemos agregar varios a la vez
G.add_nodes_from([2,3])

# para agregar aristas tenemos 2 sintaxis

G.add_edge(1,2)

e = (2,3)
G.add_edge(*e)

# Podemos agregar varias a la vez tambien
G.add_edges_from([(1,2), (1,3)])

# Para ver numero de vertices o aristas hacemos
G.number_of_nodes() # 3 # vertices
G.number_of_edges() # 3 # aristas

# Tambien podemos ver la lista completa de vertices y aristas que tiene el grafo
list(G.nodes) # [1, 2, 3]
list(G.edges) # [(1,2), (1, 3), (2, 3)]

# Atributo degree, nos da la key del vertice y su grado correspondiente
dict(G.degree) # { 1: 2, 2: 2, 3: 3 }

# ELIMINAR VERTICES ARISTAS ETC
G.remove_node(2)
G.remove_nodes_from([1,3])
G.remove_edge(1,3)

# Agregamos pesos a las aristas
G.add_edge(1,2, weight=4.7)

# Ahora vamos a crear un grafo
G = nx.Graph()
G.add_nodes_from([1,2,3])
G.add_edge_from([(1,2), (1,3)])
G.add_node('spam')
len(list(nx.connected_components(G))) # Esto es para ver cuantos componentes conectados hay nos devuelve 2 ya uqe tenemos el nodo 1 conectado al 2 y al 3


# Si queremos graficarlo
import matplotlib.pyplot as plt
nx.draw(G,with_labels=True,font_weight='bold')#le decimos que dibujamos y le pasamos primero el nodo y despues estilos


# Si hay que graficar grafos con pesos seria:
pos = nx.sprint_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_labels= dict([
    ((n1,n2), d['weight'])
    for n1,n2,d in G.edges(data=True)
    ])
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)

G = nx.Graph()
G.add_nodes_from("abcdefghijz")
G.add_edge("a", "b", weight=4)
G.add_edge("b", "c", weight=1)
G.add_edge("c", "d", weight=6)
G.add_edge("b", "e", weight=6)
G.add_edge("b", "f", weight=4)
G.add_edge("c", "f", weight=3)
G.add_edge("d", "z", weight=1)
G.add_edge("a", "e", weight=1)
G.add_edge("f", "e", weight=6)
G.add_edge("f", "g", weight=5)
G.add_edge("g", "h", weight=1)
G.add_edge("a", "i", weight=6)
G.add_edge("e", "j", weight=8)
print(nx.shortest_path_length( G, source="a", target="z", weight="weight" )) # Nos encuentra la longitud del camino mas corto de la a a la z en este caso

print(nx.shortest_path( G, source="a", target="z", weight="weight" ))# Nos encuentrael camino mas corto de la a a la z en este caso como indicamos

# Si es sin pesos / peso = 1, le sacamos el parametro weight

T = nx.dfs_tree(G, source='a') # Esto nos encuentra el arbol de expansion y utiliza el algo dfs
nx.draw(T)

T2 = nx.minimum_spanning_tree(G) # esto nos da el arbol de expansion minima
print(T2.size(weight="weight"))