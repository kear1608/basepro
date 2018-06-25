import networkx as nx
import matplotlib.pyplot as plt
import random

import matplotlib.pyplot as plt
import networkx as nx



def dessine_graphe(mon_graphe):
    """
    Dessine un graphe sur le plot en cours en utilisant un arrangement circulaire
    """
    nx.draw_circular(mon_graphe, with_labels=True)
    positions = nx.circular_layout(mon_graphe)
    noms_des_arcs = dict([((u, v,), d['weight']) for u, v, d in mon_graphe.edges(data=True)])
    nx.draw_networkx_labels(mon_graphe, positions)
    nx.draw_networkx_edge_labels(mon_graphe, positions, edge_labels=noms_des_arcs)


# Génère un graphe aléatoire en utilisant le modèle de Erdős–Rényi
graphe_1 = nx.erdos_renyi_graph(7, 0.6, seed=13, directed=False)

# Assigne une masse aléatoire à chaque arc
for (u,v,w) in graphe_1.edges(data=True):
    w['weight'] = random.randint(0,10)

# Assigne une masse nulle à l'arc 0-5
graphe_1.add_edge(0, 5, weight=0)

# Cherche un arbre de recouvrement minimum du graphe_1
arbre_1 = nx.minimum_spanning_tree(graphe_1)
sorted(arbre_1.edges(data=True))

# Fait une copie de graphe_1 et assigne une grosse masse à l'arc 0-1
graphe_2 = nx.Graph(graphe_1)
graphe_2.add_edge(0, 5, weight=100)

# Cherche un arbre de recouvrement minimum du graphe_2
arbre_2 = nx.minimum_spanning_tree(graphe_2)
sorted(arbre_2.edges(data=True))

# Affiche les deux graphes graphe_1 et graphe_2 ainsi que les deux arbres
# arbre_1 et arbre_2
dessine_graphe(graphe_1)
plt.savefig('graphe_1.png')
plt.show()

dessine_graphe(arbre_1)
plt.savefig('arbre_1.png')
plt.show()

dessine_graphe(graphe_2)
plt.savefig('graphe_2.png')
plt.show()

dessine_graphe(arbre_2)
plt.savefig('arbre_2.png')
plt.show()

# Crée une page web très simple pour afficher les résultats
f = open('output.html','w')
message = """<html>
<head></head>
<body>
<p><img src="graphe_1.png"> <img src="graphe_1.png"></p>
<p><img src="arbre_1.png"> <img src="arbre_1.png"></p>
</body>
</html>"""
f.write(message)
f.close()