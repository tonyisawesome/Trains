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


main()
