

from utils import read_input

from train_routes import TrainRoutes


def test():

    # INPUT: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

    tr = TrainRoutes(read_input(input()))

    #for x in tr.get_graph().get_list_vertexs_adjs():
    #    print (x)

    print(tr.get_shortest_route_djk('B', 'B'))
    #print(tr.get_shortest_route_djk('A', 'C'))

    #print(list(tr.get_all_routes2('B', 'B')))

    # print(tr.get_distance('A-B-C'))
    # print(tr.get_distance('A-D'))
    # print(tr.get_distance('A-D-C'))
    # print(tr.get_distance('A-E-B-C-D'))
    # print(tr.get_distance('A-E-D'))
    #print(tr.get_number_trips_by_stop('C', 'C', stops=4))
    # print(tr.get_number_trips_by_stop('A', 'C', stops=4, exactly=True))
    #print(tr.get_length_shortest_route('A', 'C'))
    #print(tr.get_length_shortest_route('B', 'B'))  
    #print(tr.get_length_routes_max_distance('C', 'C', 30))

if __name__ == "__main__":    
    test()

