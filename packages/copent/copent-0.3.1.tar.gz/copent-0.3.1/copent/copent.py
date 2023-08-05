##################################################################################
###  Estimating Copula Entropy and Transfer Entropy 
###  2022-09-11
###  by Ma Jian (Email: majian03@gmail.com)
###
###  Parameters
###	x    	: N * d data, N samples, d dimensions
###	k    	: kth nearest neighbour, parameter for kNN entropy estimation. default = 3
###	dtype	: distance type ['euclidean', 'chebychev' (i.e Maximum distance)]
###	lag	: time lag. default = 1
###
###  References
###  [1] Ma Jian, Sun Zengqi. Mutual information is copula entropy. 
###      arXiv:0808.0845, 2008.
###  [2] Kraskov A, Stögbauer H, Grassberger P. Estimating mutual information. 
###      Physical review E, 2004, 69(6): 066138.
###  [3] Ma, Jian. Estimating Transfer Entropy via Copula Entropy. 
###      arXiv preprint arXiv:1910.04375, 2019.
###  [4] Ma, Jian. Multivariate Normality Test with Copula Entropy.
###      arXiv preprint arXiv:2206.05956, 2022.
##################################################################################

from scipy.special import digamma
from scipy.stats import rankdata as rank 
from scipy.spatial.distance import cdist
from math import gamma, log, pi
from numpy import array, abs, max, vstack, zeros, cov
from numpy.random import normal as rnorm
from numpy.linalg import det
import numpy as np

##### constructing empirical copula density [1]
def construct_empirical_copula(x):
	(N,d) = x.shape	
	xc = zeros([N,d]) 
	for i in range(0,d):
		xc[:,i] = rank(x[:,i]) / N
	
	return xc

##### Estimating entropy with kNN method [2]
def entknn(x, k = 3, dtype = 'chebychev'):
	(N,d) = x.shape
	
	g1 = digamma(N) - digamma(k)
	
	if dtype == 'euclidean':
		cd = pi**(d/2) / 2**d / gamma(1+d/2)
	else:	# (chebychev) maximum distance
		cd = 1;

	logd = 0
	dists = cdist(x, x, dtype)
	dists.sort()
	logd = np.cumsum(np.log(dists[:, k] * 2) * d / N)[-1]

	return (g1 + log(cd) + logd)

##### 2-step Nonparametric estimation of copula entropy [1]
def copent(x, k = 3, dtype = 'chebychev', log0 = False):
	xarray = array(x)

	if log0:
		(N,d) = xarray.shape
		max1 = max(abs(xarray), axis = 0)
		for i in range(0,d):
			if max1[i] == 0:
				xarray[:,i] = rnorm(0,1,N)
			else:
				xarray[:,i] = xarray[:,i] + rnorm(0,1,N) * max1[i] * 0.000005

	xc = construct_empirical_copula(xarray)

	try:
		return -entknn(xc, k, dtype)
	except ValueError: # log0 error
		return copent(x, k, dtype, log0 = True)


##### conditional independence test [3]
##### to test independence of (x,y) conditioned on z
def ci(x, y, z, k = 3, dtype = 'chebychev'):
	xyz = vstack((x,y,z)).T
	yz = vstack((y,z)).T
	xz = vstack((x,z)).T
	return copent(xyz,k,dtype) - copent(yz,k,dtype) - copent(xz,k,dtype)

##### estimating transfer entropy from y to x with lag [3]
def transent(x, y, lag = 1, k = 3, dtype = 'chebychev'):
	xlen = len(x)
	ylen = len(y)
	if (xlen > ylen):
		l = ylen
	else:
		l = xlen
	if (l < (lag + k + 1)):
		return 0
	x1 = x[0:(l-lag)]
	x2 = x[lag:l]
	y = y[0:(l-lag)]
	return ci(x2,y,x1,k,dtype)

##### multivariate normality test [4]
def mvnt(x, k = 3, dtype = 'chebychev'):
	return -0.5 * log(det(cov(x.T))) - copent(x,k,dtype)