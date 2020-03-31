class Vertex:

    '''
    This class defines a vertex that can be added to a graph
    '''

    def __init__(self, value = None):
        self.id = value
        self.connectedTo = {}

    def addNeighbor(self, neighbor, connectionWeight = 0):
        self.connectedTo[neighbor] = connectionWeight

    def getAllConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getConnectionWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([v.id for v in self.connectedTo])

class Graph:

    '''
    This class defines a Graph data structure and uses a dictionary track edges of Vertices
    '''

    def __init__(self):
        # model vertex list as an adjacency list, even though its dict
        self.vertexList = {}
        self.numVertexes = 0

    def addVertex(self, value):
        newVertex = Vertex(value)
        self.vertexList[value] = newVertex
        self.numVertexes += 1
        return newVertex
    
    def getVertex(self, vertex):
        # if vertex name in list, return this vertex object
        if vertex in self.vertexList:
            return self.vertexList[vertex]
        else:
            return None

    def addEdge(self, v1, v2, weight = 0):
        if v1 not in self.vertexList:
            newVertex = self.addVertex(v1)
        if v2 not in self.vertexList:
            newVertex = self.addVertex(v2)

        self.vertexList[v1].addNeighbor(self.vertexList[v2], weight)
    
    def getAllVertices(self):
        return self.vertexList.keys()
    
    # this is the iter method that executes when we actually do "for <blank> in <graphname>"
    # iterator will be over all the values in the vertexList dict - so the vertex objects themselves
    def __iter__(self):
        return iter(self.vertexList.values())

    # allows use of 'in' operator on the graph object
    def __contains__(self, vertex):
        return vertex in self.vertexList