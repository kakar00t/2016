import math

NUM_PARTITIONS = 4
partition = {}


def assign_partions_to_nodes(nodes):
    '''

    :param nodes:
    :return:
    '''
    print "Numero de nodos: %s" % len(nodes)
    nodes.sort()
    ct = 1
    num_partition = 1
    total_graph_for_partition = math.ceil(len(nodes) / (NUM_PARTITIONS*1.0))
    #print(nodes, total_graph_for_partition)
    for i in nodes:
        if ct % total_graph_for_partition == 0:
            partition[i] = num_partition
            num_partition += 1
        else:
            partition[i] = num_partition
        ct += 1
    #print(partition)
partition_found = {}


def map(u, v):
    '''

    :param u:
    :param v:
    :return:
    '''
    for a in range(1, NUM_PARTITIONS):
        for b in range(a+1, NUM_PARTITIONS+1):
            #print((a, b), (u, v))

            if {partition[u], partition[v]}.issubset({a, b}):
                if (a,b) not in partition_found:
                    partition_found[(a, b)] = []
                partition_found[(a, b)].append((u,v))

    if partition[u] != partition[v]:
        for a in range(1, NUM_PARTITIONS - 1):
            for b in range(a + 1, NUM_PARTITIONS):
                for c in range(b + 1, NUM_PARTITIONS + 1):
                    #print((a, b, c), (u, v))
                    if {partition[u], partition[v]}.issubset({a, b, c}):
                        if (a, b, c) not in partition_found:
                            partition_found[(a, b, c)] = []
                        partition_found[(a, b, c)].append((u, v))


