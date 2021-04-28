from pixeldifferencemap import *

import numpy as np

from PIL import Image

import os

def adder(X, c, folder_name, N, IP):

    li = pixeldifmap(c, N)

    I = np.identity(X.shape[1])

    H_1 = li[0]
    H_2 = li[0] * li[0]

    V_1 = li[1]
    V_2 = li[1] * li[1]

    H_1_V_1 = H_1 * V_1

    PIXEL_DIFFERENCE_MAP_R = X * li[0]
    PIXEL_DIFFERENCE_MAP_R_2 = PIXEL_DIFFERENCE_MAP_R * li[0]

    L_PIXEL_DIFFERENCE_MAP = li[1] * X
    L_2_PIXEL_DIFFERENCE_MAP = li[1] * L_PIXEL_DIFFERENCE_MAP

    #L_PIXEL_DIFFERENCE_MAP_R = li[1] * PIXEL_DIFFERENCE_MAP_R
    L_1_PIXEL_DIFFERENCE_MAP_R_2 = li[1] * PIXEL_DIFFERENCE_MAP_R_2
    L_2_PIXEL_DIFFERENCE_MAP_R_2 = li[1] * L_1_PIXEL_DIFFERENCE_MAP_R_2
    
    
    G9 = X - PIXEL_DIFFERENCE_MAP_R_2 + X - L_2_PIXEL_DIFFERENCE_MAP_R_2 + X - L_2_PIXEL_DIFFERENCE_MAP + (X * H_2) - (V_2 * X) + X - (X * H_1) + X - (X * H_1_V_1) + X - (V_1 * X) + (X * H_1) - (V_1 * X)
    #imgg9 = Image.fromarray(np.array(G9, dtype=np.uint8))
    '''print(IP, "{}/{}/{}/{}_cell_direction.png".format(os.getcwd(), IP, folder_name, folder_name))
    input()'''
    #imgg9.save("{}/{}/{}/{}_cell_direction.png".format(os.getcwd(), IP, folder_name, folder_name))
    return(G9)
    #return(PIXEL_DIFFERENCE_MAP_R + L_PIXEL_DIFFERENCE_MAP + L_PIXEL_DIFFERENCE_MAP_R)
