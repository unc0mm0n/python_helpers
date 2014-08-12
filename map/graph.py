from collections import defaultdict

class Graph(object):

    def __init__(self, vertices = None, connected = False):
        ''' A graph of vertices and edges between them. Doesn't hold any information on represantation
                vertices => a set of initial vertices
                connected => if true connect all vertices to eachother
        '''
        if vertices == None:
            vertices = set()
        self.vertices = set(vertices)

        self.edges = defaultdict(set)

        if connected:
            self.connect_vertices(*vertices)

    def __str__(self):
        res = 'Graph:\n'
        for vertice in self.vertices:
            edges = self.edges[vertice]
            res += '{0} => {1}\n'.format(vertice, ', '.join(edges))
        return res

    # Creates edges between each vertice given as an argument
    # Adding them as new vertices if they do not exist
    def connect_vertices(self, *vertices):
        vertices = set(vertices)
        for vertice in vertices:
            # Add every vertice not already present
            if vertice not in self.vertices:
                self.vertices = self.vertices.union(vertice)
            self.edges[vertice] = self.edges[vertice].union(vertices - set(vertice))

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

