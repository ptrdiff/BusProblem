from unittest import TestCase
from solveBusProblem import solve_bus_problem
import random as rnd
import numpy as np


def generator():
    max_number_of_stops = 5
    max_number_of_bus_routes = 5
    number_of_stops = rnd.randint(2, max_number_of_stops)
    stop_number_finish = rnd.randint(2, number_of_stops)
    number_of_bus_routes = rnd.randint(0, max_number_of_bus_routes)
    routes_description = list()
    for _ in range(number_of_bus_routes):
        route_number_of_stops = rnd.randint(2, number_of_stops)
        stops_range = np.array_split(range(1, number_of_stops + 1), route_number_of_stops)
        time_range = np.array_split(range(1, 100), route_number_of_stops)
        route_map = zip(map(lambda el: rnd.randint(el[0], el[-1]), stops_range),
                        map(lambda el: rnd.randint(el[0], el[-1]), time_range))
        route = list([route_number_of_stops]) + list(route_map)
        routes_description.append(route)
    return number_of_stops, stop_number_finish, number_of_bus_routes, routes_description


class TestSolveBusProblem(TestCase):

    def solve_bus_problem_generator(self):
        self.skipTest("Skip generator")
        raw_data = generator()
        print(raw_data)
        result = solve_bus_problem(*raw_data)
        print(result)
        return 0

    def test_solve_bus_problem_1(self):
        number_of_stops = 5
        stop_number_finish = 4
        number_of_bus_routes = 4
        routes_description = [[2, (1, 5), (2, 10)],
                              [2, (2, 10), (4, 15)],
                              [3, (5, 0), (4, 17), (3, 21)],
                              [3, (1, 2), (3, 40), (4, 44)]]
        expected_result = 44

        result = solve_bus_problem(number_of_stops,
                                   stop_number_finish,
                                   number_of_bus_routes,
                                   routes_description)
        self.assertEqual(result, expected_result)

    def test_solve_bus_problem_2(self):
        number_of_stops = 3
        stop_number_finish = 4
        number_of_bus_routes = 3
        routes_description = [[2, (1, 2), (2, 10)],
                              [2, (2, 15), (4, 45)],
                              [3, (1, 2), (3, 40), (4, 44)]]
        expected_result = 45

        result = solve_bus_problem(number_of_stops,
                                   stop_number_finish,
                                   number_of_bus_routes,
                                   routes_description)
        self.assertEqual(result, expected_result)

    def test_solve_bus_problem_3(self):
        number_of_stops = 6
        stop_number_finish = 3
        number_of_bus_routes = 5
        routes_description = [[2, (1, 5), (2, 10)],
                              [2, (2, 10), (4, 15)],
                              [3, (4, 20), (3, 27), (2, 41)],
                              [3, (1, 2), (4, 30), (6, 42)],
                              [3, (6, 45), (5, 47), (3, 51)]]
        expected_result = 51

        result = solve_bus_problem(number_of_stops,
                                   stop_number_finish,
                                   number_of_bus_routes,
                                   routes_description)
        self.assertEqual(result, expected_result)
