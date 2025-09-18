import pytest

from ex06_voyageur_commerce.src.voyageur import (
    generate_cities, brute_force_tsp, calculate_distance, optimize_with_greedy, optimize_with_genetic_algorithm,
    optimize_with_dynamic_programming
)


def test_generate_cities():
    # Validate generating the correct number of cities
    cities = generate_cities()
    assert len(cities) == 5
    for city in cities:
        assert 0 <= city[0] <= 100
        assert 0 <= city[1] <= 100


def test_calculate_distance():
    # Validate distance calculation between two points
    point1 = (0, 0)
    point2 = (3, 4)
    distance = calculate_distance(point1, point2)
    assert distance == 5.0  # Expecting a 3-4-5 right triangle


def test_brute_force_tsp():
    # Validate brute force TSP returns optimal solution
    cities = [(0, 0), (0, 1), (1, 0)]
    path, distance = brute_force_tsp(cities)
    assert len(path) == len(cities) + 1  # Path should return to the start
    assert distance == pytest.approx(3.414, 0.001)  # Expect roughly 3.414 (shortest round-trip)


def test_optimize_with_greedy():
    # Validate greedy optimization generates a valid TSP solution
    cities = generate_cities()
    path, distance = optimize_with_greedy(cities)
    assert len(path) == len(cities) + 1  # Path should return to the start
    assert isinstance(distance, float)


def test_optimize_with_genetic_algorithm():
    # Validate genetic algorithm generates a valid TSP solution
    cities = generate_cities()
    path, distance = optimize_with_genetic_algorithm(cities)
    assert len(path) == len(cities) + 1  # Path should return to the start
    assert isinstance(distance, float)


def test_optimize_with_dynamic_programming():
    # Validate dynamic programming generates a valid TSP solution
    cities = generate_cities()
    path, distance = optimize_with_dynamic_programming(cities)
    assert len(path) == len(cities) + 1  # Path should return to the start
    assert isinstance(distance, float)
