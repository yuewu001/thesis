#! /usr/bin/env python
#################################################################################
#     File Name           :     weakly.py
#     Created By          :     yuewu
#     Creation Date       :     [2017-04-14 10:59]
#     Last Modified       :     [2017-04-15 11:44]
#     Description         :      
#################################################################################

import numpy as np

def func(dist):
    if type(dist) is list:
        dist = np.array(dist)
    return dist * np.square(np.exp(-dist/0.01))

if __name__ == '__main__':
    dim = 1000
    x = sorted(np.random.random(dim) / 15)
    y =  func(x)

    with open('temp.txt', 'w') as fh:
        for i in xrange(dim):
            fh.write('%f\t%f\n' %(x[i], y[i]))
