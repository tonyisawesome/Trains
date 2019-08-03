import input
import utils


def main():
    graph = input.get_graph()

    # Test Input:
    # 1.
    print(utils.find_distance(graph, ['A', 'B', 'C']))

    # 2.
    print(utils.find_distance(graph, ['A', 'D']))

    # 3.
    print(utils.find_distance(graph, ['A', 'D', 'C']))

    # 4.
    print(utils.find_distance(graph, ['A', 'E', 'B', 'C', 'D']))

    # 5.
    print(utils.find_distance(graph, ['A', 'E', 'D']))

    # 6.
    print(utils.find_routes_max_stops(graph, 'C', 'C', 3))

    # 7.
    print(utils.find_routes_equal_stops(graph, 'A', 'C', 4))


main()
