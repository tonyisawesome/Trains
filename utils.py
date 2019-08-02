def find_distance(graph, route):
    if len(route) < 2:
        return

    dist = 0

    for i in range(0, len(route) - 1):
        town = graph[route[i]]

        try:
            dist += town.get_dist(route[i + 1])
        except KeyError:
            return "NO SUCH ROUTE"

    return dist


# def find_num_trips(graph, max=None, eq=None):
