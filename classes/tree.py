import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import networkx as nx
import tkinter as tk
import pydot
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

class Tree():
    def __init__(self, frame, treeExplorer):
        self.treeExplorer = treeExplorer
        self.frame = frame

        fig = plt.Figure()
        self.canvas = FigureCanvasTkAgg(fig, master=frame)

        G = nx.DiGraph()
        self.treeExplorer.exploreTreeNetworkX(2,'', G ,0)

        pos= nx.nx_pydot.pydot_layout(G, prog='dot')

        self.ax = fig.gca()  # it can gives list of `ax` if there is more subplots.
        self.ax.axis('on')
        self.ax.margins(0)
        self.ax.set_aspect('equal')
        self.ax.tick_params(which="both", direction="inout")
        self.ax.xaxis.set_visible(False)
        self.ax.yaxis.set_visible(False)

        fig.subplots_adjust(0, 0, 1, 1)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['left'].set_visible(False)

        labels = treeExplorer.getLabels(G.nodes())
        nodes = nx.draw_networkx_nodes(
            G,
            pos,
            node_size=[50*180 for v in G.nodes()],
            ax=self.ax,
            node_color='white',
            node_shape='s',
            linewidths=1,
            margins=0.18
        )
        nodes.set_edgecolor('black')
        nx.draw_networkx_edges(
            G,
            pos,
            arrows=True,
            ax=self.ax
        )

        nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=self.ax)

        widget = self.canvas.get_tk_widget()
        widget.pack(fill=BOTH,expand=1)

        # nx.draw(G, pos, node_size=[len(arbre[v].getPrenom()) * 75 for v in G.nodes()], with_labels=False, arrows=True, ax=self.ax)
    def draw(self, treeExplorer):
        pass
    def canvasTree(self, treeExplorer):
        self.ax.clear()

        fig = plt.Figure()
        fig.subplots_adjust(0, 0, 1, 1)

        G = nx.DiGraph()
        i = treeExplorer.getCurrentPersonneSosa()
        treeExplorer.exploreTreeNetworkX(i,'', G ,0)
        pos= nx.nx_pydot.pydot_layout(G, prog='dot')
        labels = treeExplorer.getLabels(G.nodes())

        nodes = nx.draw_networkx_nodes(
            G,
            pos,
            node_size=[50*180 for v in G.nodes()],
            ax=self.ax,
            node_color='white',
            node_shape='s',
            linewidths=1,
            margins=0.18
        )
        nodes.set_edgecolor('black')
        nx.draw_networkx_edges(G,pos,arrows=True,ax=self.ax)
        nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=self.ax)
        self.canvas.draw()

    def exploreTreeDot(self, sosa, idOld, tree, graph,i):
        if sosa in tree and i<3:
            personne = tree[sosa]
            id = personne.getNom() + str(personne.Sosa)
            labelPersonne = personne.getDisplayStr()
            shapePersonne = getForme(personne.Sosa)
            shapeColor = getColor(personne.Sosa)
            graph.add_node(pydot.Node(id, label=labelPersonne , style='filled', fontsize='16', shape=shapePersonne, fillcolor=shapeColor))

            if i >0 and idOld != '':
                graph.add_edge(pydot.Edge(id, idOld, arrows=True))

            exploreTreeDot(personne.getMere(), id, tree,graph, i+1)
            exploreTreeDot(personne.getPere(), id, tree,graph, i+1)

    def plotPngForThirdGen(self, tree, i):

        sosaList = []
        graph = pydot.Dot("my_graph",graph_type="graph", fontsize="16")
        exploreTreeDot(tree[i],'',tree, sosaList,graph,0)
        # # affichage(result, result[2])
        graph.write_png('data/png/'+str(i)+'-output.png')
        return graph

    # on fait un graph networkx

    # Louis XIV (M, birthday=1638-09-05, deathday=1715-09-01)


    def getForme(var):
        if var % 2 == 0:
            return "square"
        else:
            return "circle"

    def getColor(var):
        if var % 2 == 0:
            return "azure"
        else:
            return "navajowhite"
