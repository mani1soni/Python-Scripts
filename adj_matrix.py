g = {
    'A' : [('B',10), ('C',10)],
    'B' : [('D',1)],
    'C' : [('F',5)],
    'D' : [('E',5), ('F',3)],
    'E' : [('G',5)],
    'F' : [('G',5)],
    'G' : []
}

import sys
import pandas as pd

def build_adj_matrix(g):
    inf = sys.maxint
    keys = g.keys()
    df = pd.DataFrame(index=g.keys(), columns=g.keys())
    df = df.fillna(float("inf"))

    for k, vals in g.iteritems():
        df[k][k] = 0
        for v in vals:
            df[k][v[0]] = v[1]

    return df

mat = build_adj_matrix(g)
print(mat)