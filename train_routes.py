import sys

from graph import Graph

from operator import itemgetter

from dijkstra import dijkstra

def _shortest_path(v, path):    
    if v.get_previous():
        path.append(v.get_previous().get_id())
        _shortest_path(v.get_previous(), path)
    return

class TrainRoutes:
    """Is a implementation with basic operations to supports admin Train Routes  

        Using a directed graph where a node represents a town and an edge represents a route between two towns.
        The weighting of the edge represents the distance between the two towns. 

        As input, a route between two towns (A to B) with a distance of 5 is represented as AB5.

    :param routes: a list of base route between two towns. Example: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
    """

    _graph = Graph(directed=True)

    def __init__(self, routes):
        for route in routes:
            self._graph.insert_edge(route.frm, route.to, int(route.dist))

    def get_graph(self):
        return self._graph

    def get_all_routes(self, frm, to, max=0):
        return self._graph.bfs_paths_cost(frm, to, max)

    def get_all_routes2(self, frm, to):
        x = self._graph.bfs_paths(frm, to)
        #print(list(x))
        return x

    def get_shortest_route(self, frm, to):
        routes = self.get_all_routes(frm, to)
        routes_sorted = sorted(routes, key=itemgetter(1))
        return routes_sorted[0]


    def get_shortest_route_djk(self, frm, to):
        if frm==to:
            l = []
            for v in self._graph.get_vertexs():
                for adj in v.get_vertex_adjacents():
                    #print(adj)
                    if adj == self._graph.get_vertex(to):
                        l.append((v.get_cost(adj),v, v.get_id()))
            x = min(l, key = lambda t: t[0])
            #print(x)
            dijkstra(self._graph, frm)
            return (x[1].get_distance() + x[0])
        else:
            dijkstra(self._graph, frm)
            return (self._graph.get_vertex(to).get_distance())

        #path = [self._graph.get_vertex(to).get_id()]  
        #_shortest_path(self._graph.get_vertex(to), path)
        #return (path[::-1], v.get_distance()) 
        #return path

    def get_length_shortest_route(self, frm, to):
        route, distance = self.get_shortest_route(frm, to)
        return distance

    def get_distance(self, path):
        sum_ = 0
        path = path.split('-')
        for curr, next_ in self._routes(path):
            c = self._graph.get_vertex(curr)
            n = self._graph.get_vertex(next_)
            if n in c.get_vertex_adjacents():
                sum_ += (c.get_cost(n))
            else:
                if next_:
                    return 'NO SUCH ROUTE'
        return sum_

    def get_trips_by_stop(self, frm, to, stops, exactly=False):
        trips = 0
        result = []
        routes = list(self._graph.bfs_paths_cost(frm, to))
        routes = list(zip(*routes))[0]
        if routes:
            if exactly:
                result = list(
                    filter(lambda x: len(x) == stops + 1, routes)
                )
            else:
                result = list(
                    filter(lambda x: len(x) <= stops + 1, routes)
                )
        #print(result)
        unique = set([''.join(item) for item in result])
        return list(unique)

    def get_number_trips_by_stop(self, frm, to, stops, exactly=False):
        return len(self.get_trips_by_stop(frm, to, stops, exactly))

    def get_routes_max_distance(self, frm, to, max_):
        result = []
        routes = list(self._graph.bfs_paths_cost(frm, to, max_))
        if routes:
            less_max = list(
                filter(lambda x: x[1] < max_, routes)
            )
            result = list(zip(*less_max))[0]
        unique = set([''.join(item) for item in result])
        return list(unique)

    def get_length_routes_max_distance(self, frm, to, max_):
        return len(self.get_routes_max_distance(frm, to, max_))

    def _routes(self, iterable):
        iterator = iter(iterable)
        current_item = next(iterator)
        for next_item in iterator:
            yield (current_item, next_item)
            current_item = next_item
        yield  (current_item, None)
