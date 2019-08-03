from town import Town


def get_graph():
    graph = dict()

    with open("graph.txt") as f:
        for line in f.readlines():
            town = Town(line[0]) if line[0] not in graph else graph[line[0]]

            town.set_dist(line[1], int(line[2]))
            graph[line[0]] = town

    return graph
