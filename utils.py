
from collections import namedtuple


def format(s):
    routes = [(frm, to, dist) for frm, to, dist in (x.strip()
                                                    for x in s.split(','))]
    Route = namedtuple('Route', ['frm', 'to', 'dist'])
    return [Route(*r) for r in routes]

def read_input_from_file(file):
    with open(file) as f:
        rows = f.readlines()
    return format(rows[0])

def read_input(input_):
    return format(input_)
