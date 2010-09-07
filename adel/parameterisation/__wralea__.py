
# This file has been generated at Fri Mar 13 10:06:46 2009

from openalea.core import *

RfunStr = """ #
#Write here R code returning geometric functions in a list named Rfun
#
Rfun = list(
  #azim should return the azimutal deviation of a leaf compared to the previous one (A = axe number [0..n], n = leaf nulmber from the base, ntop = idem from the top
  azim = function(a,n,ntop) {
    180 + 10 * (runif(1)-.5)
  },
  #xysr returns the index of the xysr database associated with a leaf
  xysr = function(a,n,ntop) {
    ntop + 1
  },
  #geomT returns azT,incT and dred.
  #azT is the difference of azimuth between parent axe and tiller
  #incT (deg) is the baseal inclination of tiller
  #dred (mockup length unit,ie cm for wheat) is the distance at flowering between top of parent axe and top of tiller
  geomT = function(a) {
    if (a == 0) {
      azT = 0
      incT = runif(1) * 5
      dred =0
    } else {
      azT = 75 + (runif(1) - .5) * 5
      incT = 82 + (runif(1) - .5) * 5
      dred = runif(1) * 7
    }
    list(azT=azT,incT=incT,dred=dred)
  }
  )"""

geoLeafStr = """

# R code for setting Azim and Lindex freely  (reference to index of leaf db)

geoLeaf <- list(

        Azim = function(a,n,ntop) {
          ifelse(ntop <= 4,
                 180 + 60 * runif(1),
                 180 + 20 * runif(1))
               },

        Lindex = function(a,n,ntop) {
                 ntop + 1
               }
        )


"""

__name__ = 'alinea.adel.parameterisation'

__editable__ = True
__description__ = 'Utilities for generating parameters to simulation models from different types of data'
__license__ = 'CECILL'
__url__ = ''
__alias__ = ['adel.parameterisation']
__version__ = '0.0.1'
__authors__ = 'C. Fournier, C. Pradal'
__institutes__ = 'INRA, CIRAD, INRIA'
__icon__ = ''


__all__ = ['parameterisation_freeGeoLeaf', 'parameterisation_genGeoLeaf', 'parameterisation_devCsv', 'parameterisation_genGeoAxe', 'parameterisation_setAdel', 'parameterisation_setAdelArv', 'p_plant_parameter','p_simpleMais','p_setCanopy','p_simpleMais_param','p_shape_factor','p_geometric_dist','p_bell_shaped_dist']

parameterisation_freeGeoLeaf = Factory(name='freeGeoLeaf',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='freeGeoLeaf',
                inputs=[{'interface': ITextStr, 'name': 'RCode for geometry of Leaves ', 'value': geoLeafStr , 'desc': ''}],
                outputs=[{'interface': None, 'name': 'Robj', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )

p_shape_factor = Factory(name='shape_factor',
                description='compute shape factors for nb_phy in a leaf database',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='shape_factor',
                inputs=[{'interface': None, 'name': 'leaf database', 'value': geoLeafStr , 'desc': ''},
                        {'interface': IInt, 'name': 'nb_phytomer', 'value': 16, 'desc': ''}],
                outputs=[{'interface': None, 'name': 'shape factors', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )

parameterisation_genGeoLeaf = Factory(name='geoLeaf',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='genGeoLeaf',
                inputs=[{'interface': IInt, 'name': 'ranktop', 'value': 4, 'desc': ''}, {'interface': IFloat, 'name': 'dazTop', 'value': 60, 'desc': ''}, {'interface': IFloat, 'name': 'dazBase', 'value': 10, 'desc': ''}],
                outputs=[{'interface': None, 'name': 'Robj', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




parameterisation_devCsv = Factory(name='devCsv',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='devCsv',
                inputs=[{'interface': IFileStr(filter="*.csv", save=False), 'name': 'axeT', 'value': None, 'desc': ''}, {'interface': IFileStr(filter="*.csv", save=False), 'name': 'dimT', 'value': None, 'desc': ''}, {'interface': IFileStr(filter="*.csv", save=False), 'name': 'phenT', 'value': None, 'desc': ''}, {'interface': IFileStr(filter="*.csv", save=False), 'name': 'earT', 'value': None, 'desc': ''}, {'interface': IFileStr(filter="*.csv", save=False), 'name': 'ssi2senT', 'value': None, 'desc': 'specification of leaf senescence patterns as a function of ssi'}],
                outputs=[{'interface': None, 'name': 'Robj', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




parameterisation_genGeoAxe = Factory(name='geoAxe',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='genGeoAxe',
                inputs=[{'interface': IFloat, 'name': 'axe Azimuth', 'value': 75, 'desc': ''}, {'interface': IFloat, 'name': 'dazT', 'value': 5, 'desc': ''}, {'interface': IFloat, 'name': 'MainStem inclination', 'value': 2, 'desc': ''}, {'interface': IFloat, 'name': 'dinc', 'value': 2, 'desc': ''}, {'interface': IFloat, 'name': 'tiller inclination', 'value': 60, 'desc': ''}, {'interface': IFloat, 'name': 'dincT', 'value': 5, 'desc': ''}, {'interface': IFloat, 'name': 'dredT', 'value': 7, 'desc': ''}],
                outputs=[{'interface': None, 'name': 'Robj', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




parameterisation_setAdel = Factory(name='setAdel',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='setAdel',
                inputs=[{'interface': None, 'name': 'devT', 'value': None, 'desc': 'R list of tables for dvpt'}, {'interface': None, 'name': 'geomLeaf', 'value': None, 'desc': 'Rfunc list for leaf geometry'}, {'interface': None, 'name': 'geomAxe', 'value': None, 'desc': 'R func list for axe geometry'}, {'interface': IInt, 'name': 'nplants', 'value': 1, 'desc': 'Number of plants to simulate'}, {'interface': IInt, 'name': 'randoom seed', 'value': None, 'desc': 'Seed for R random number generator'}],
                outputs=[{'interface': None, 'name': 'Parameter Robj', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )

p_setCanopy = Factory(name='setCanopy',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='setCanopy',
                inputs=[{'interface': None, 'name': 'canT', 'value': None, 'desc': 'R canopy table'},{'interface': IInt, 'name': 'nplants', 'value': 1, 'desc': 'Number of plants'},{'interface': IBool, 'name': 'randomize', 'value': True, 'desc': 'random sampling and random azimuth'}, {'interface': IInt, 'name': 'randoom seed', 'value': None, 'desc': 'Seed for R random number generator'}],
                outputs=[{'interface': None, 'name': 'new Canopy', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




parameterisation_setAdelArv = Factory(name='setAdelArv',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='setAdelArv',
                inputs=[{'interface': None, 'name': 'Calage Arvalis Robj', 'value': None, 'desc': ''}, {'interface': ITextStr, 'name': 'RFun for geometry', 'value': RfunStr , 'desc': ''}, {'interface': IInt, 'name': 'nplants', 'value': 1, 'desc': ''}, {'interface': IFloat, 'name': 'sdlevee', 'value': 20, 'desc': ''}],
                outputs=[{'interface': None, 'name': 'Parameter Robj', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )


p_plant_parameter = Factory(name='plant_parameter',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='plant_parameter',
                inputs=[ {'interface': IInt, 'name': 'surface (cm2)', 'value': 1000, 'desc': 'total surface of leaves'}, 
{'interface': IInt, 'name': 'plant height (cm)', 'value': 200 , 'desc': 'plant height (cm)'},
{'interface': IInt, 'name': 'pseudo-stem height (cm)', 'value': 20 , 'desc': 'heigth of pseudo-stem (longest sheath) (cm)'},
{'interface': IInt, 'name': 'phytomer', 'value': 15, 'desc': 'Total number of phytomers'}, 
{'interface': IInt, 'name': 'juvenil', 'value': 6, 'desc': 'Number of juvenil phytomers before flowering'},
# leaves surface
{'interface': IFloat(min=0., max=1000, step=0.1), 'name': 'leaf area skewness', 'value': 5, 'desc': 'Skewness of the leaf area distribution'}, 
{'interface': IFloat(min=0., max=1, step=0.1), 'name': 'max leaf area position', 'value': 0.7, 'desc': 'Position of the leaf with maximal area'}, 
{'interface': IFloat(min=0., step=0.1), 'name': 'internode dist.', 'value': 1, 'desc': 'Control parameter for the distribution of internode length using a geometrical model (un = q*u(n-1)'},
{'interface': IFloat(min=0., step=0.1), 'name': 'sheath dist.', 'value': 1.4, 'desc': 'Control parameter for the distribution of sheath length using a geometrical model (un = q*u(n-1)'},
{'interface': IInt, 'name': 'phyllotactic angle (degree)', 'value': 180, 'desc': 'Phyllotactic angle.'}, 
{'interface': IInt, 'name': 'juvenil variance (degree)', 'value': 20, 'desc': 'Phyllotactic angle variance for juvenil phytomer.'}, 
{'interface': IInt, 'name': 'mature variance (degree)', 'value': 60, 'desc': 'Phyllotactic angle variance for mature phytomer.'}, 
{'interface': IInt, 'name': 'basal insertion angle (degree)', 'value': 40, 'desc': 'Insertion angle of the first leaf.'}, 
{'interface': IInt, 'name': 'insertion deviation angle (degree)', 'value': 40, 'desc': 'Variation of the insertion angle along the axis.'}, 
{'interface': IInt, 'name': 'base diameter (cm)', 'value':2, 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'interface': IInt, 'name': 'top diameter (cm)', 'value':1, 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'interface': IFloat(min=0.1,max=1.,step=0.1), 'name': 'length maximal width ratio', 'value':0.1, 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'interface': None, 'name': 'leaf database', 'desc': 'Mapping between rank and a list of leaf shape (midrib curvature and width)'}, 

],
                outputs=[{'interface': IDict, 'name': 'Parameters', 'desc': ''},
                {'interface': None, 'name': 'Rparameters', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )

p_simpleMais_param = Factory(name='simpleMais_param',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='simpleMais_param',
                inputs=[ {'interface': IInt, 'name': 'surface (cm2)', 'value': 1000, 'desc': 'total surface of leaves'}, 
{'interface': IInt, 'name': 'plant height (cm)', 'value': 200 , 'desc': 'plant height (cm)'},
{'interface': IInt, 'name': 'pseudo-stem height (cm)', 'value': 20 , 'desc': 'heigth of pseudo-stem (longest sheath) (cm)'},
{'interface': IInt, 'name': 'phytomer', 'value': 15, 'desc': 'Total number of phytomers'}, 
{'interface': IInt, 'name': 'juvenil', 'value': 6, 'desc': 'Number of juvenil phytomers before flowering'},
# leaves surface
{'interface': IFloat(min=0., max=1000, step=0.1), 'name': 'leaf area skewness', 'value': 5, 'desc': 'Skewness of the leaf area distribution'}, 
{'interface': IFloat(min=0., max=1, step=0.1), 'name': 'max leaf area position', 'value': 0.7, 'desc': 'Position of the leaf with maximal area'}, 
{'interface': IFloat(min=0., step=0.1), 'name': 'pseudostem dist.', 'value': 1.4, 'desc': 'Control parameter for the geometric distribution of distances between leaves on pseudo stem'},
{'interface': IFloat(min=0., step=0.1), 'name': 'stem dist.', 'value': 1, 'desc': 'Control parameter for the geometric distribution of distances between leaves on pseudo stem'},
{'interface': IInt, 'name': 'phyllotactic angle (degree)', 'value': 180, 'desc': 'Phyllotactic angle.'},  
{'interface': IInt, 'name': 'basal insertion angle (degree)', 'value': 40, 'desc': 'Insertion angle of the first leaf.'}, 
{'interface': IInt, 'name': 'top insertion angle (degree)', 'value': 30, 'desc': 'Insertion angle of the last leaf'}, 
{'interface': IInt, 'name': 'base diameter (cm)', 'value':2, 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'interface': IInt, 'name': 'top diameter (cm)', 'value':1, 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'interface': IFloat(min=0.1,max=1.,step=0.1), 'name': 'length maximal width ratio', 'value':0.1, 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'interface': IFloat, 'name': 'shape_factor', 'desc': 'list of leaf shape factors','value': 0.75}, 

],
                outputs=[{'interface': IDict, 'name': 'Parameters', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )

p_simpleMais_plan = Factory(name='simpleMais_plan',
                description='Simulation plan for Mais',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='simpleMais_plan',
                outputs=[ {'interface': IInt, 'name': 'S', 'desc': 'total surface of leaves'}, 
{'name': 'H', 'desc': 'plant height (cm)'},
{'name': 'Hps', 'desc': 'heigth of pseudo-stem (longest sheath) (cm)'},
{'name': 'NbPhy', 'desc': 'Total number of phytomers'}, 
{'name': 'NbJ', 'desc': 'Number of juvenil phytomers before flowering'},
# leaves surface
{'name': 'Skew', 'desc': 'Skewness of the leaf area distribution'}, 
{'name': 'pmax', 'desc': 'Position of the leaf with maximal area'}, 
{'name': 'HLips', 'desc': 'Control parameter for the geometric distribution of distances between leaves on pseudo stem'},
{'name': 'HLi', 'desc': 'Control parameter for the geometric distribution of distances between leaves on pseudo stem'},
{'name': 'az', 'desc': 'Phyllotactic angle.'},  
{'name': 'phib', 'desc': 'Insertion angle of the first leaf.'}, 
{'name': 'phit', 'desc': 'Insertion angle of the last leaf'}, 
{'name': 'db', 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'name': 'dt', 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'name': 'lwr', 'desc': 'Ratio between leaf maximal width and length.)'}, 
{'name': 'ff', 'desc': 'list of leaf shape factors'}, 

],
                inputs=[{'interface': IDict, 'name': 'Parameters', 'desc': ''}, 
                {'interface':IInt(min=0), 'name':'step' }],
               )
__all__.append('p_simpleMais_plan')

p_simpleMais = Factory(name='simpleMais',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='simpleMais',
                inputs=[{'interface': IDict, 'name': 'Parameter dict', 'value': None, 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )

p_geometric_dist = Factory(name='geometric_dist',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='geometric_dist',

               )

p_bell_shaped_dist = Factory(name='bell_shaped_dist',
                description='',
                category='simulation',
                nodemodule='parameterisation',
                nodeclass='bell_shaped_dist',
               )
