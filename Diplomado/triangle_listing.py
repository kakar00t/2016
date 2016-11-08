#!/usr/bin/env python
# -*- coding: utf-8 -*-


def intersection(neighbors_u, neighbors_v):
    """
    Por ejemplo: intersection([1,2,3,4], [2,3]) -> retorna: [2,3]

    :param neighbors_u: lista de adyacentes de u
    :param neighbors_v: lista de adyacentes de v
    :return: lista de la intersección entre ambas listas.
    """
    return list(set(neighbors_u).intersection(neighbors_v))




def counting_triangles(G):
    """
    Cuenta los triángulos en un grafo

    :param G: Grafo
    :return: Número de triángulos encontrados
    """
    count = 0
    V = G.nodes()
    triangles = []
    V.sort()
    for u in V:
        for v in [_v for _v in G.neighbors(u) if _v > u]:
            for w in [_w for _w in intersection(G.neighbors(u), G.neighbors(v)) if _w > v]:
                #print("Triángulo encontrado: (%s, %s, %s) " % (u, v, w))
                triangles.append((u, v, w))
                count += 1
    #print("Número de triángulos encontrados: %s" % count)
    return triangles


def counting_triangles_dp(G):
    """
    Cuenta los triángulos en un grafo(versión con programación dinamica)

    :param G: Grafo
    :return: Número de triángulos encontrados
    """
    count = 0
    V = G.nodes()
    V.sort()
    neighbors = {}
    triangles = []
    for u in V:
        for v in [_v for _v in G.neighbors(u) if _v > u]:
            if v not in neighbors:
                neighbors[v] = G.neighbors(v)
            for w in [_w for _w in intersection(G.neighbors(u), neighbors[v]) if _w > v]:
                #print("Triángulo encontrado: (%s, %s, %s) " % (u, v, w))
                triangles.append((u, v, w))
                count += 1
    #print("Número de triángulos encontrados: %s" % count)
    return triangles

