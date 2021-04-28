import sys

import numpy as np

def pixel_len(a, N):

    l = a

    ITL, IBR = [[0 for i in range(l)] for i in range(N-l)], [[0 for i in range(N-l)] for i in range(l)] 

    ITR, IBL = []*0, []*0

    for j in range(N-l):

        ITR.append([]*0)

    for j in range(l):

        IBL.append([]*0)

    for j in range(len(ITR)):

        for k in range(len(ITR)):

            if j==k:

                ITR[j].insert(k, 1)
            
            else:

                ITR[j].insert(k, 0)

    for j in range(len(IBL)):

        for k in range(len(IBL)):

            if j==k:

                IBL[j].insert(k, 1)
            
            else:

                IBL[j].insert(k, 0)

    Rows = []*0

    for i in range(len(ITR)):
            
        Rows.append(ITL[i]+ITR[i])
        
    for i in range(len(IBR)):
        
        Rows.append(IBL[i]+IBR[i])
        
    return(Rows)

if __name__ == "__main__":

    sys.exit(0)