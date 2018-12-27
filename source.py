from solveBusProblem import solve_bus_problem

if __name__ == '__main__':
    number_of_stops = 5
    stop_number_finish = 4
    number_of_bus_routes = 4
    routes_description = [[2, (1, 5), (2, 10)],
                          [2, (2, 10), (4, 15)],
                          [3, (5, 0), (4, 17), (3, 21)],
                          [3, (1, 2), (3, 40), (4, 44)]]
    result = solve_bus_problem(number_of_stops,
                               stop_number_finish,
                               number_of_bus_routes,
                               routes_description)
    print(result)
