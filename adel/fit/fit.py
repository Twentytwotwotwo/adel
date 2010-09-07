from alinea.adel import fitting
from copy import deepcopy

def fit(x, y, s, r, nb_points):
    return fitting.fit3(x, y, s, r, nb_points)

def fit_leaf( leaf ):
    x, y, s, r = leaf
    return fitting.fit2(x, y, s, r)

simplify = fitting.simplify

def fit_leaves( db, nb_points):
    return fitting.fit_leaves(db, nb_points),

