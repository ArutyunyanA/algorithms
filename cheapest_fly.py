""""We need to fly home as cheaply as possible so that more money is left for gifts. 
Aunt Lidia asked for different kinds of cheeses, and Vasia wanted a new toy car. 
I've been looking at the schedule for quite a while and I’m starting to think that 
some planes are flying in vain".

As the input you get the flight schedule as an list, each element of which 
is the price of a direct flight between 2 cities (list of 3 elements - 2 city 
names as a string, and a flight price).

Planes fly in both directions and the price in both directions is the same. There is 
a possibility that there are no direct flights between cities.

Find the price of the cheapest flight between cities that are given as the 2nd 
and 3rd arguments. In case the flight can not be performed, return 0.

Dijkstra algorithm

from collections import defaultdict
from typing import List

def cheapest_flight(flights: List, departure: str, arrival: str) -> int:
    # Initialization
    graph = defaultdict(dict)
    for city1, city2, price in flights:
        graph[city1][city2] = price
        graph[city2][city1] = price
    queue = list(graph.keys())
    path = {node: float("inf") for node in queue}
    path[departure] = 0

    # Dijkstra algorithm: main loop
    while queue:
        # find the city with a minimal cost
        current = min(queue, key=lambda city: path[city])
        queue.remove(current)

        for i in graph[current]:
            # compare alternatives and choose the shortest
            alternate = graph[current][i] + path[current]
            if path[i] > alternate:
                path[i] = alternate

    return 0 if path[arrival] == float("inf") else path[arrival]

import heapq

def cheapest_flight(schedule, start, destination):
    graph = {}
    for flight in schedule:
        source, dest, price = flight
        if source not in graph:
            graph[source] = []
        graph[source].append((dest, price))

    heap = [(0, start)]

    while heap:
        current_price, current_city = heapq.heappop(heap)

        if current_city == destination:
            return current_price

        if current_city not in graph:
            continue

        for neighbor, price in graph[current_city]:
            heapq.heappush(heap, (current_price + price, neighbor))

    return 0


def cheapest_flight(costs: list, a: str, b: str) -> int:
    tickets = [([char], a) for char in costs if a in char]
    cost = 999
    while tickets:
        flight, lastPosition = tickets.pop(0)
        start, end, price = flight[-1]
        currentPosition = end if start == lastPosition else start
        if b in (start, end):
            cost = min(cost, sum([price for _, _, price in flight]))
        else:
            for nextStep in [char for char in costs if currentPosition in char and char not in flight]:
                tickets.append((flight + [nextStep], currentPosition))
    return cost if cost != 999 else 0

"""

def cheapest_flight(costs: list, a: str, b: str) -> int:
    tickets = [([char], a) for char in costs if a in char]
    cost = 999
    while tickets:
        flight, lastPosition = tickets.pop(0)
        start, end, price = flight[-1]
        currentPosition = end if start == lastPosition else start
        if b in (start, end):
            cost = min(cost, sum([price for _, _, price in flight]))
        else:
            for nextStep in [char for char in costs if currentPosition in char and char not in flight]:
                tickets.append((flight + [nextStep], currentPosition))
    return cost if cost != 999 else 0


print("Example:")
#print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")) == 70
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A")) == 70
print(cheapest_flight([["A", "C", 40], ["A", "B", 20], ["A", "D", 20], ["B", "C", 50], ["D", "C", 70]], "D", "C",)) == 60
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F")) == 0
print(cheapest_flight([["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D")) == 25


print("The mission is done! Click 'Check Solution' to earn rewards!")
