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


def find_routes_max_stops(graph, from_town, to_town, max_stops):
    routes = [[from_town]]
    result = []

    for route in routes:

        if 1 < len(route) and route[-1] == to_town:
            result.append(route)
            # continue

        if len(route) == max_stops + 1:
            continue

        for town in graph[route[-1]].get_dst():
            if town != route[-1]:
                routes.append(route + [town])

    # print(result)

    if not result:
        return "NO SUCH ROUTE"

    return len(result)


def find_routes_equal_stops(graph, from_town, to_town, eq_stops):
    routes = [[from_town]]
    result = []

    for route in routes:
        if len(route) == eq_stops + 1:
            if route[-1] == to_town:
                result.append(route)

            continue

        for town in graph[route[-1]].get_dst():
            if town != route[-1]:
                routes.append(route + [town])

    # print(result)

    if not result:
        return "NO SUCH ROUTE"

    return len(result)
