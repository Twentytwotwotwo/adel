#
# Utilitaires pour l'analyse de sensibilite
#
import numpy
import rpy2.robjects as robj
from rpy2.robjects.numpy2ri import numpy2ri #force conversion mode of Robject
r = robj.r

r.require('sensitivity')

def Morris(repet,factors,binf,bsup):
    """ Simplified import of R'Morris function"""
    factors=robj.StrVector(factors)
    binf=numpy.array(binf)
    bsup=numpy.array(bsup)
    d=r.list('oat', 5, 3)
    d= r['names<-'](d,['type','levels','grid.jump'])
    m = r.morris(factors=factors,r=repet,design=d,binf=binf,bsup=bsup)
    param=r['data.frame'](m.r["X"][0])
    pdict = dict((k,numpy.array(param.r[k][0]).tolist()) for k in r.colnames(param))
    return m,pdict

def Morris_IS(morrisPlan,y):
    """ Compute morris sensitivity indicators for a Morris plan and the corresponding model responses"""
    mod=r.tell(morrisPlan,numpy.array(y))
    ee=mod.r['ee'][0]
    mu=r.apply(ee,2,r['mean'])
    mustar=r.apply(ee,2,r('function(x) mean(abs(x))'))
    sigma=r.apply(ee,2,r.sd)

    return mod,numpy.array(mustar).tolist(),numpy.array(sigma).tolist()

def plotSens(mod):
    """ moris plot"""
    return r.plot(mod)
