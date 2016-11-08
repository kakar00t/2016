#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Diplomado BigData & DataScience - PUCV
import sys
from pylab import figure
from triangle_listing import *
from triangle_type_partition import *
import networkx as nx
import matplotlib.pyplot as plt
import time


def drawing_graph(G):
    """
    Se dibuja el grafo con sus caracteristicas visuales.

    :param G: Grafo
    :return:
    """
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos,
                           nodelist=G.nodes(),
                           node_color='r',
                           node_size=200,
                           alpha=0.6)

    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    #   Labels
    #   Se agregan los label a cada nodo

    labels = {}
    for v in G.nodes():
        labels[v] = r'$%s$' % v

    ##''' Se agrega texto al grafo'''
    #nx.draw_networkx_labels(G, pos, labels, font_size=16)

    plt.axis('off')
    plt.show()

if __name__ == '__main__':

    figure(facecolor='white')

   ## '''Se abre el archivo y se leen las aristas(edges)'''
    file = open('data/data06.txt', 'r')

    edges = []
    i = 0
    for line in file:
       ## '''Si no es digito el primer carácter, entonces salta a la siguiente linea.'''
        if not line[0].isdigit():
            continue

        try:
            e1, e2 = [int(e) for e in line.split()]
            edges.append((e1, e2))
        except Exception as e:
           ## print "Error en la lectura del .txt, %s", e
            break

    file.close()

    G = nx.Graph()

    '''Se crean las aristas'''
    #edges = list(set([tuple(sorted(t)) for t in edges]))
    #edges.sort()
    G.add_edges_from(edges)

    start = time.clock()
    triangles = counting_triangles(G)

    '''Cuenta los triángulos del grafo'''
    printlen(triangles)
    ## print "Tiempo total: %s" % (time.clock() - start)
    ##print ""

    start = time.clock()


    assign_partions_to_nodes(G.nodes())

    f = {}

    start = time.clock()

    ''' REDUCE '''
    for i in G.edges():
        map(i[0], i[1])

    ct_triangles = 0
    for k in partition_found:
        #print(k, '-->', partition_found[k])
        G.clear()
        G.add_edges_from(partition_found[k])
        triangles = counting_triangles_dp(G)
       # print("count: %s" % len(triangles))
        ct_triangles += len(triangles)
        for t in triangles:
            tuple_triangle = (t[0], t[1], t[2])

            #print(tuple_triangle, partition[t[0]] , partition[t[1]], partition[t[2]])
            if tuple_triangle not in f:
                f[tuple_triangle] = 0

            if partition[t[0]] == partition[t[1]] == partition[t[2]]:
                # print('::::::::', tuple_triangle)
                f[tuple_triangle] += (1 / ((NUM_PARTITIONS - 1)*1.0))
            else:
                f[tuple_triangle] += 1
    c = 0
    for ff in f:
        c += f[ff]
    ## print "Total: %s" % c
     ## print "Tiempo total(TTP): %s" % (time.clock() - start)
    '''Se dibuja el grafo'''
    #drawing_graph(G)
