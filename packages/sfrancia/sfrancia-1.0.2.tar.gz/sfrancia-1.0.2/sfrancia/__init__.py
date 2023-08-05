import numpy as np
from scipy import stats
   
def shapiroFrancia(array):
   
    def ppoints(n, a):
        """ numpy analogue or `R`'s `ppoints` function
            see details at http://stat.ethz.ch/R-manual/R-patched/library/stats/html/ppoints.html
            :param n: array type or number"""
        try:
            n = float(len(n))
        except TypeError:
            n = float(n)
        return (np.arange(n) + 1 - a)/(n + 1 - 2*a)

    x = np.sort(array)
    n = x.size
    y = stats.norm.ppf(ppoints(n, a = 3/8))
    W, _ = np.square(stats.pearsonr(x, y))
    u = np.log(n)
    v = np.log(u)
    mu = -1.2725 + 1.0521 * (v - u)
    sig = 1.0308 - 0.26758 * (v + 2/u)
    z = (np.log(1 - W) - mu)/sig
    pval = stats.norm.sf(np.abs(z))
   
    dic = {}
    dic["method"] = "Shapiro-Francia normality test"
    dic["statistics"] = W
    dic["p-value"] = pval

    return dic
