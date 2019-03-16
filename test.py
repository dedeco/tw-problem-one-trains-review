
import unittest

from train_routes import TrainRoutes

from utils import read_input_from_file


class StepCodingAssignment(unittest.TestCase):

    def setUp(self):
        graph = read_input_from_file('input.in')
        self.tr = TrainRoutes(graph)

    def test_routes_distances(self):
        self.assertEqual(self.tr.get_distance('A-B-C'), 9)
        self.assertEqual(self.tr.get_distance('A-D'), 5)
        self.assertEqual(self.tr.get_distance('A-D-C'), 13)
        self.assertEqual(self.tr.get_distance('A-E-B-C-D'), 22)
        self.assertEqual(self.tr.get_distance('A-E-D'), 'NO SUCH ROUTE')

    def test_trips_by_stops(self):
        # The number of trips starting at C and ending at C with a maximum of 3 stops. In the sample data below,
        #    there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops)
        self.assertEqual(
            self.tr.get_number_trips_by_stop('C', 'C', stops=3), 2)

        routes = self.tr.get_trips_by_stop('C', 'C', stops=3)
        routes.sort()
        self.assertEqual(','.join(map(str, routes)), "CDC,CEBC")

    def test_number_of_trips_exactly_stops(self):
        # The number of trips starting at A and ending at C with exactly 4 stops. In the sample data below, there
        # are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A
        # to C (via D,E,B)
        self.assertEqual(self.tr.get_number_trips_by_stop(
            'A', 'C', stops=4, exactly=True), 3)

        routes = self.tr.get_trips_by_stop('A', 'C', stops=4, exactly=True)
        routes.sort()
        self.assertEqual(','.join(map(str, routes)), "ABCDC,ADCDC,ADEBC")

    def test_length_shortest_routes(self):
        self.assertEqual(self.tr.get_length_shortest_route('A', 'C'), 9)
        self.assertEqual(self.tr.get_length_shortest_route('B', 'B'), 9)

    def test_get_length_routes_max_distance(self):
        # The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips
        # are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.
        self.assertEqual(
            self.tr.get_length_routes_max_distance('C', 'C', 30), 7)

        routes = self.tr.get_routes_max_distance('C', 'C', 30)
        routes.sort(key=lambda s:  (len(s), s))
        self.assertEqual(','.join(map(str, routes)),
                         "CDC,CEBC,CDEBC,CDCEBC,CEBCDC,CEBCEBC,CEBCEBCEBC")
