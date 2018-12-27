import networkx as nx


def create_graph(routes_description):
    graph = nx.MultiDiGraph()
    for route in routes_description:
        current_node = route[1][0]
        current_node_weight = route[1][1]
        for node, weight in route[2::]:
            graph.add_edge(current_node, node,
                           start=current_node_weight,
                           finish=weight)
            current_node = node
            current_node_weight = weight
    return graph


def greedy_algorithm_graph(stop_number_start,
                           stop_number_finish,
                           routes_description):
    graph = create_graph(routes_description)
    try:
        paths = nx.edge_disjoint_paths(graph, stop_number_start, stop_number_finish)
        max_time = 0
        for path in map(nx.utils.pairwise, paths):
            path = list(path)[::-1]
            if max_time < graph.get_edge_data(*path[0])[0]['finish']:
                max_time = graph.get_edge_data(*path[0])[0]['finish']
    except nx.exception.NetworkXNoPath:
        return 'ПУТИ ДОМОЙ НЕТ!'
    return max_time


def solve_bus_problem(number_of_stops,
                      stop_number_finish,
                      number_of_bus_routes,
                      routes_description):
    stop_number_start = 1
    result = greedy_algorithm_graph(stop_number_start,
                                    stop_number_finish,
                                    routes_description)

    answer = 'ПУТИ ДОМОЙ НЕТ!'
    if result != 0:
        answer = result
    return answer
