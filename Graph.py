from typing import Optional
from Vertex import Vertex
from VertexColor import VertexColor


class Graph:
    """
    This class represents a directed graph.

    Attributes
    ----------
    v: int
        The vertices count
    vertices: [Vertex]
        List of vertices in the graph
    adj: [v][v]
        The adjacency matrix of the graph

    Methods
    -------
    add_edges(u: int, v: int):
        Add an edge from u to v.
    traverse_bfs():
        Traverse the graph in BFS.
    traverse_dfs():
        Traverse the graph in DFS.
    """

    def __init__(self, v: int):
        """
        Create a graph instance.

        :param v: the number of vertices in the graph.
        """
        self.v = v
        self.vertices = [Vertex(i) for i in range(v)]
        self.adj = [[0 for i in range(v)] for i in range(v)]
        self.time = 0

    def add_edge(self, u: int, v: int):
        """
        Add a edge from u to v.

        :param u: the source vertex.
        :param v: the destination vertex.
        """
        self.adj[u][v] = 1

    def traverse_bfs(self, start: Optional[int]):
        """
        Perform the graph traversal using BFS.
        """
        if start is None:
            u = self.vertices[0]
        else:
            u = self.vertices[start]

        queue = [u]
        wave = 1
        ordered = []
        while len(queue) > 0:
            u = queue.pop(0)
            u.color = VertexColor.BLACK
            ordered.append(u)
            for i in range(self.v):
                if self.adj[u.v][i] == 1:
                    v = self.vertices[i]
                    if v.color == VertexColor.WHITE:
                        v.p = u
                        v.color = VertexColor.GREY
                        v.d = wave
                        queue.append(v)
            wave += 1
        return ordered

    def __dfs_visit(self, u: Vertex):
        self.time += 1
        u.d = self.time
        for i in range(self.v):
            if self.adj[u.v][i] == 1:
                v = self.vertices[i]
                if v.color == VertexColor.WHITE:
                    v.color = VertexColor.GREY
                    v.p = u
                    self.__dfs_visit(v)
        u.color = VertexColor.BLACK
        self.time += 1
        u.f = self.time

    def traverse_dfs(self):
        """
        Perform the graph traversal using DFS.
        """
        self.time = 0
        for vertex in self.vertices:
            if vertex.color == VertexColor.WHITE:
                self.__dfs_visit(vertex)
        return self.vertices
