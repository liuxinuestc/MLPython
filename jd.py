a = stree.fit(X_train)# -*- coding: utf-8 -*-
__author__ = 'Xin'

import numpy as np


def bifind(listA,x):
    m = 0
    n = len(listA)
    while(m<n-1):
        if x<listA[(m+n)/2]:
            n = (m+n)/2-1
        elif x>listA[(m+n)/2]:
            m = (m+n)/2+1
        else:
            break
    return n

def abc():
    n = input()
    peopleList = raw_input()

    cop = []
    theif = []

    for j,i in enumerate(peopleList):
        if i == 'X':
            theif.append(j)
        elif  i== '#':
            continue
        else:
            xleft = j-int(i)
            if len(cop)==0 or xleft>cop[-1][1]:
                cop.append([xleft,j+int(i)])
            elif j+int(i)<cop[-1][1]:
                continue
            else:
                c = map(lambda t:t[1], cop)
                n = bifind(c,xleft)
                if cop[n][0] >xleft:
                    cop[n] = [xleft,j+int(i)]
                else:
                    cop[n][1] = j+int(i)
    count = 0
    j = 0
    for i in theif:
        while(j<len(cop)):
            if i > cop[j][0] and i <cop[j][1]:
                count += 1
                break
            if i< cop[j][0]:
                break
            else:
                j += 1
    print count

    n = int(raw_input())
    carlist = []
    setTime = set()
    for i in range(n):
        a = map(int,raw_input().split())
        carlist.append([a[0],a[0]+a[1]])
        setTime.add(a[0])
        setTime.add(a[0]+a[1])
    a = sorted(list(setTime))
    ans = 0
    for i in range(len(a)):
        for j in range(len(a)):
            curNum = 0
            pa = a[i]
            pb = a[j]
            for k in range(len(carlist)):
                ll = carlist[k]
                if ((carlist[0]<=pa and carlist[1] >=pa) or (carlist[0]<=pb and carlist[1] >=pb)):
                    curNum +=1
            ans = max(ans,curNum)
    print ans

w =  np.random.randint(1,7,20)
v = np.random.randint(1,7,20)

#其实不算动态规划吧，只是个递归
def knapsackRec(i,j):
    if i>19:
        return 0
    elif w[i]>j:
        return knapsackRec(i+1,j)
    else:
        return max(knapsackRec(i+1,j-w[i])+v[i],knapsackRec(i+1,j))

def knapsack(lim):
    m = np.zeros((20,lim+1),int)
    for i in range(20)[::-1]:
        for j in range(lim+1):
            if w[i]>j:
                if i+1 <20:
                    m[i][j]= m[i+1][j]
            else:
                if i+1<20:
                    m[i][j] = max((m[(i+1),(j-w[i])]+v[i]),m[i+1,j])
                else:
                    m[i][j] = m[i][j]+v[i]
    return m[0][-1]

print knapsackRec(0,10)
print knapsack(10)

from sklearn.cluster import *

from scipy.spatial.distance import mahalanobis
from sklearn.neighbors import DistanceMetric

# from sklearn import datasets
# X1, y1=datasets.make_circles(n_samples=5000, factor=.6,
#                                       noise=.05)
# X2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2,1.2]], cluster_std=[[.1]],
#                random_state=9)
#
# X = np.concatenate((X1, X2))
from sklearn.datasets.samples_generator import *
X,y = make_blobs(n_samples=1500000,n_features=20,centers=16,cluster_std=1.3)
    #


# a = AgglomerativeClustering(10,affinity='mahalanobis',linkage='average').fit(X)#速度太慢
# labels = a.labels_
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import linalg
# colors = plt.cm.Spectral(np.linspace(0, 1, 10))
# for k, col in zip(np.arange(10), colors):
#
#     class_member_mask = (labels == k)
#
#     xy = X[class_member_mask]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=6)
#
# plt.title('Estimated number of clusters: %d' % 10)
# plt.show()
color_iter = plt.cm.Spectral(np.linspace(0, 1, 10))
    # itertools.cycle(['navy', 'c', 'cornflowerblue', 'gold',
    #                           'darkorange'])
def plot_results(X, Y_, means, covariances, index, title):
    splot = plt.subplot(2, 1, 1 + index)
    for i, (mean, covar, color) in enumerate(zip(
            means, covariances, color_iter)):
        v, w = linalg.eigh(covar)
        v = 2. * np.sqrt(2.) * np.sqrt(v)
        u = w[0] / linalg.norm(w[0])
        # as the DP will not use every component it has access to
        # unless it needs it, we shouldn't plot the redundant
        # components.
        if not np.any(Y_ == i):
            continue
        plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], .8, color=color)

        # Plot an ellipse to show the Gaussian component
        angle = np.arctan(u[1] / u[0])
        angle = 180. * angle / np.pi  # convert to degrees
        ell = mpl.patches.Ellipse(mean, v[0], v[1], 180. + angle, color=color)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)

    plt.xlim(-9., 5.)
    plt.ylim(-3., 6.)
    plt.xticks(())
    plt.yticks(())
    plt.title(title)
from sklearn import mixture
gmm = mixture.GaussianMixture(n_components=10, covariance_type='full').fit(X)
plot_results(X, gmm.predict(X), gmm.means_, gmm.covariances_, 0,
             'Gaussian Mixture')#数据量大就不可以了
# dpgmm = mixture.BayesianGaussianMixture(n_components=4,
#                                         covariance_type='full').fit(X)
# plot_results(X, dpgmm.predict(X), dpgmm.means_, dpgmm.covariances_, 1,
#              'Bayesian Gaussian Mixture with a Dirichlet process prior')
plt.show()

# plt.plot(X[a.labels_ == k].T, c=col, alpha=.5)
# plt.axis('tight')
# plt.axis('off')
# plt.suptitle("AgglomerativeClustering(affinity=%s)" % metric, size=20)

# a = DBSCAN(metric=DistanceMetric.get_metric( 'mahalanobis',VI = v) ,algorithm='brute').fit(X)
    # DBSCAN(metric='mahalanobis').fit(X)
