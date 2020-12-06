import os
import networkx as nx
import community as community_louvain
from networkx.algorithms import bipartite, community


def main():
    G = nx.read_edgelist('edges/2020Nov.edges', delimiter=',')

    politicians = bipartite.sets(G)[1]

    P = bipartite.overlap_weighted_projected_graph(
        G, politicians, jaccard=False)

    louv = louvain(P, 0.95, 5)

    write(louv)
    print(evaluate(P, louv))


def louvain(P, res=1.0, seed=None):
    partition = community_louvain.best_partition(
        P, resolution=res, random_state=seed)
    communities = {k: v for k, v in sorted(
        partition.items(), key=lambda item: item[1])}
    return communities


def partition(part_dict):
    part_list = list()
    for i in range(max(part_dict.values())+1):
        part_list.append([])
    for i, j in part_dict.items():
        part_list[j].append(i)
    return part_list


def write(l):
    with open('C:/Users/anton/Desktop/evaluation/clusters.txt', mode='w') as f:
        for line in partition(l):
            f.write(' '.join(line) + '\n')


def evaluate(P, l):
    part = partition(l)
    metrics = {'Communities': max(l.values())+1,
               'Modularity': community.modularity(P, part),
               'Coverage': community.coverage(P, part),
               'Performance': community.performance(P, part)
               }
    return metrics


if __name__ == '__main__':
    main()
