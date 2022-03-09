#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from graph import Graph


def main():
    routes = [
        ("Brazil", "USA"),
        ("Brazil", "South Korea"),
        ("USA", "Brazil"),
        ("USA", "South Korea"),
        ("Paris", "USA"),
        # ("Paris", "South Korea"),
        ("South Korea", "USA")
    ]

    route_graph = Graph(routes)

    start = "Paris"
    end = "South Korea"

    print(f"Paths between {start} and {end}")
    print(route_graph.get_paths(start, end))
    print(f"Shortest paths between {start} and {end}", route_graph.get_shortest_path(start, end))
    
if __name__ == "__main__":
    main()
