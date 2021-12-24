from VertexColor import VertexColor


class Vertex:
    """
    This class to represent the vertex in a graph.

    Attributes
    ----------
    v: int
        The vertex id.
    color: VertexColor
        The color of the vertex.
    d: int
        The start time in DFS or wave number in BFS.
    f: int
        The finish time in DFS.
    p: Vertex
        The parent of the vertex
    """

    def __init__(self, v: int, color=VertexColor.WHITE, d=0, f=0, p=None):
        """
        Create a new vertex in the graph.

        :param v: the vertex id.
        :param color: the vertex color.
        :param d: the start time in DFS or wave number in BFS.
        :param f: the finish time in DFS.
        :param p: the parent.
        """
        self.v = v
        self.color = color
        self.d = d
        self.f = f
        self.p = p

    def __str__(self) -> str:
        return "(" + str(self.v) + " d:" + str(self.d) + " f:" + str(self.f) + ")"
