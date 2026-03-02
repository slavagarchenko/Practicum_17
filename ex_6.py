def build_graph(num_roads: int) -> dict:
    """
    Build a graph of cities and roads with distances.

    Args:
        num_cities (int): Number of cities.
        num_roads (int): Number of roads.

    Returns:
        dict: Graph represented as adjacency list with distances.
    """
    graph = {}

    for _ in range(num_roads):
        string = input().strip()
        words_list = string.split()
        city1 = words_list[0]
        city2 = words_list[1]
        distance = int(words_list[2])

        match city1 not in graph:
            case True:
                graph[city1] = {}

        match city2 not in graph:
            case True:
                graph[city2] = {}

        graph[city1][city2] = distance
        graph[city2][city1] = distance

    return graph


def find_shortest_path(start: str, end: str, graph: dict) -> int:
    """
    Find shortest distance between two cities using Dijkstra's algorithm.

    Args:
        start (str): Starting city.
        end (str): Destination city.
        graph (dict): Graph with cities and distances.

    Returns:
        int: Shortest distance between start and end, or -1 if no path exists.
    """
    if start not in graph or end not in graph:
        return -1

    distances = {}
    unvisited = []

    for city in graph:
        match city == start:
            case True:
                distances[city] = 0

            case False:
                distances[city] = float('inf')

        unvisited.append(city)

    while unvisited:
        current = None
        min_distance = float('inf')

        for city in unvisited:
            if distances[city] < min_distance:
                min_distance = distances[city]
                current = city

        if current is None:
            break

        if current == end:
            return distances[end]

        unvisited.remove(current)

        for neighbor, distance in graph[current].items():
            match neighbor in unvisited:
                case True:
                    new_distance = distances[current] + distance

                    match new_distance < distances[neighbor]:
                        case True:
                            distances[neighbor] = new_distance

    return distances[end] if distances[end] != float('inf') else -1


def main() -> None:
    """
    Main function.
    """
    try:
        num_cities = int(input())

        if num_cities < 0:
            print("Количество населенных пунктов должно быть неотрицательным")
            return

        num_roads = int(input())

        if num_roads < 0:
            print("Количество дорог должно быть неотрицательным")
            return

        graph = build_graph(num_cities, num_roads)

        last_line = input().strip()
        cities = last_line.split()
        start_city = cities[0]
        end_city = cities[1]

        result = find_shortest_path(start_city, end_city, graph)

        match result:
            case -1:
                print("Путь не найден")

            case _:
                print(result)

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены корректные данные")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
