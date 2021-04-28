from identitymatrixgenerator import *

import numpy as np

import sys

def pixeldifmap(b, N):

    h_H_l = np.array(pixel_len(b, N), dtype = np.uint8)

    v_H_l = np.array(np.transpose(pixel_len(b, N)), dtype = np.uint8)

    I = np.identity(N)

    h_P_l = I - h_H_l

    h_P_l = np.array(h_P_l, dtype = np.uint8)

    h_P_l = h_P_l.reshape((h_P_l.shape[0], h_P_l.shape[1], 1))

    v_P_l = I - v_H_l

    v_P_l = np.array(v_P_l, dtype = np.uint8)

    v_P_l = v_P_l.reshape((v_P_l.shape[0], v_P_l.shape[1], 1))

    return([h_P_l, v_P_l])

if __name__ == "__main__":

    sys.exit(0)
