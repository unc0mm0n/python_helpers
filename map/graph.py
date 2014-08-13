from collections import defaultdict

class Graph(object):

    def __init__(self, vertices = None, connected = False):
        ''' A graph of vertices and edges between them. Doesn't hold any information on represantation
                vertices => a list of initial vertices
                connected => if true connect all vertices to eachother
        '''

        self.edges = defaultdict(list)

        if connected:
            self.connect_vertices(vertices)
        else:
            for vert in vertices:
                self.connect_vertices((vert,))

    def __contains__(self, key):
        return key in self.edges

    def __str__(self):
        res = '{}\n'.format(self.__class__.__name__)
        for vertice in self.edges:
            edges = self.edges[vertice]
            res += '{0} => {1}\n'.format(vertice, edges)
        return res

    # Creates edges between each vertice given as an argument
    # Adding them as new vertices if they do not exist
    def connect_vertices(self, vertices):
        for vertice in vertices:
            # Add every vertice not already present
            for vert in vertices:
                if vert != vertice and vert not in self.edges[vertice]:
                    self.edges[vertice].append(vert)

            if not self.edges[vertice]:
                self.edges[vertice] = []

    def neighbours(self,vertice):
        return self.edges[vertice]

# Returns all vertices that are reachable from given vertice in given graph
def reachable(graph, vertice):
    visited_vertices = []
    vertice_queue = [vertice]
    while vertice_queue:
        vertice = vertice_queue.pop()
        visited_vertices.append(vertice)

        neighbours = graph.neighbours(vertice)
        for neighbour in neighbours:
            if neighbour not in visited_vertices and neighbour not in vertice_queue:
                vertice_queue.append(neighbour)

    return visited_vertices



if __name__ == '__main__':
    map = Graph()
    map.connect_vertices('a', 'd')
    map.connect_vertices('c', 'b')
    map.connect_vertices('b', 'd')
    map.connect_vertices('e', 'd')
    map.connect_vertices('e', 'f')
    map.connect_vertices('g', 'f')

    print(reachable(map, 'g'))

    print(map)

