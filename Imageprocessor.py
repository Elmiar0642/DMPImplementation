from adder import *

import numpy as np

from PIL import Image

from pathlib import Path

import sys, os

def resizeimg(i):

    d_s = 300

    o_s = i.size

    ratio = float(d_s)/max(o_s)

    n_s = tuple([int(x*ratio) for x in o_s])

    i = i.resize(n_s, Image.ANTIALIAS)

    n_i = Image.new("RGB", (d_s, d_s))

    n_i.paste(i, ((d_s - n_s[0])//2, 
                    (d_s - n_s[1])//2))

    return (n_i)


def imgprcwithpath(image_path, folder_name):

    image_path = image_path.split('.')

    image_path = image_path[0]

    img = Image.open(image_path + ".png", 'r')         #.convert('L')

    foldername = image_path.split("\\")

    foldername = foldername[-3]

    image = resizeimg(img)

    X = np.array(image)

    N = X.shape[0]

    img = Image.fromarray(np.array(X, dtype=np.uint8))

    if(foldername not in os.listdir(os.getcwd())):
        
        os.mkdir(foldername)

    if(folder_name not in os.listdir(foldername)):
        
        os.mkdir("{}/{}".format(foldername, folder_name))

    img.save("{}/{}/{}.png".format(foldername, folder_name, Path(image_path).stem))

    D = 0

    for x in range(N+1):

        D += adder(X, x, folder_name, N, foldername)
        
        #img2 = Image.fromarray(np.array(D, dtype=np.uint8))

        #img2.save("{}/{}/{}/{}_Filtered{}.png".format(os.getcwd(), foldername, folder_name, Path(image_path).stem, x))

    img2 = Image.fromarray(np.array(D, dtype=np.uint8))

    img2.save("{}/{}/{}/{}_DMP.png".format(os.getcwd(), foldername, folder_name, Path(image_path).stem))

    return(np.array(D, dtype=np.uint8))
    

def imgprc(single_image, folder_name):

    image = Image.open(single_image + ".png", 'r')         #.convert('L')

    X = np.array(image)

    N = X.shape[0]

    img = Image.fromarray(np.array(X, dtype=np.uint8))

    foldername = single_image.split("\\")

    foldername = foldername[-3]

    os.mkdir("{}/{}".format(foldername, folder_name))

    img.save("{}/{}/{}.png".format(foldername, folder_name, folder_name))

    D = 0

    for x in range(8):   #N+1

        D += adder(X, x, folder_name, N, foldername)
        
        img2 = Image.fromarray(np.array(D, dtype=np.uint8))

        img2.save("{}/{}/{}/{}_Filtered{}.png".format(os.getcwd(), foldername, folder_name, folder_name, x))

    img2 = Image.fromarray(np.array(D, dtype=np.uint8))

    img2.save("{}/{}/{}/{}_DMP.png".format(os.getcwd(), foldername, folder_name, folder_name))

def dataset_getter(Datapath, foldername):

    imgprc(Datapath, foldername)

if __name__ == "__main__":

    sys.exit(0)