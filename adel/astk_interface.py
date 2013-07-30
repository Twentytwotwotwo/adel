""" Class instanciating a wheat canopy and complying to astk canopy interface
"""

from alinea.adel.AdelR import setAdel,RunAdel,genGeoLeaf,genGeoAxe
from alinea.adel.newmtg import *
import alinea.adel.data_samples as adel_data
from alinea.adel.mtg_interpreter import *

class AdelWheat(object):
    
    def __init__(self, nplants = 1, positions = None, nsect = 1, devT = None, leaf_db = None):
    
        if devT is None: 
            devT = adel_data.devT()
        if leaf_db is None: 
            leaf_db = adel_data.leaves_db()
        geoLeaf = genGeoLeaf()
        geoAxe = genGeoAxe()
        self.pars = setAdel(devT,geoLeaf,geoAxe,nplants)
        self.positions = positions
        self.leafdb = leaf_db
        self.nsect = nsect
        
    def setup_canopy(self, age = 10):
    
        self.canopy_age = age
        canopy = RunAdel(age, self.pars)
        if self.positions is not None:
            stand = [(pos,0) for pos in self.positions]
        else:
            stand = None
        g = mtg_factory(canopy, adel_metamer, leaf_sectors=self.nsect, leaf_db=self.leafdb, stand=stand)
        g = mtg_interpreter(g)
        return g

    def grow(self, g, time_control):
    
        if time_control.dt <= 0:
            pass
        else:
            self.canopy_age += time_control.dt
            canopy = RunAdel(self.canopy_age, self.pars)
            mtg_update_from_table(g, canopy)
            g = mtg_interpreter(g)
            
        return g
        
    def plot(self, g):
        from openalea.plantgl.all import Viewer
        s = plot3d(g)
        Viewer.display(s)
        return s