# Practica algo con grafos networkx
import networkx as nx

import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(G):
    """
    funcion auxiliar para imprimir los grafos con los que trabajemos El peso de las aristas, si los hay, debe estar en
    el atributo 'weight'
    """
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    edge_labels = dict(
        [
            (
                (
                    u,
                    v,
                ),
                d.get("weight", ""),
            )
            for u, v, d in G.edges(data=True)
        ]
    )
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    nx.draw_networkx_edges(G, pos)
    plt.axis("off")
    # nx.draw_networkx_labels(self.G,pos, font_size=20,font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, edge_cmap=plt.cm.Reds)

    plt.show()

# Grafo Camino P4
def grafo_camino()

# Grafo Ciclo C4


# Grafo Rueda W5


# Grafo Completo K5


# Grafo bipartito completo k2,3


