import numpy as np

from PIL import Image, ImageOps

import matplotlib.pyplot as plt

import h5py

from datetime import datetime

start_time = datetime.now()

print("STARTED AT : ", start_time)

P = []*0

DIR = "/content/data.h5"

#WEIGHT = "/content/trainedweigtsforbees.h5" 

files = h5py.File(DIR, 'r')

#weight = h5py.File(WEIGHT, 'w')

predcat, predsubcat = "c2", "031_002"

#print(files["c2"]["031_002"][:, :, :-1].nbytes)

predimg = np.array([1])

predimg = np.append(predimg, files["c2"]["031_002"][100:201, 100:200, :-1].flatten())

#print(predimg.nbytes)

#input()

labels = []*0

x_rgb, y_label = []*0, []*0

for category in files.keys():

    for subcategory in files[category].keys():         

        if subcategory[:3] not in labels:

            labels.append(subcategory[:3])

        #replacementval = labels.index(subcategory[:3])+1

        #files[category][subcategory][:, :, -1] = replacementval

        #shape = files[category][subcategory][:, :, :].shape
        #for j in range(shape[1]):

            #files[category][subcategory][:, j, :] = np.roll(files[category][subcategory][:, j, :], 1)

        #img = files[category][subcategory][:, :, :]

        #P.append(img)

        dmpimg = np.array([1])

        dmpimg = np.append(dmpimg, files[category][subcategory][100:201, 100:200, :-1].flatten())
        
        x_rgb.append(dmpimg)
        
        y_label.append(files[category][subcategory][100:201, 100:200, -1][-1][-1])

        #break

    
#P = np.array(P)
x_rgb = np.array(x_rgb, dtype = np.uint8)

#print(x_rgb.shape)

y_label = np.array(y_label)

#print(x_rgb, len(x_rgb), y_label, len(y_label))

c = x_rgb

#c = c.T

print(c.nbytes)

print(c.shape)

#input()

#input()

ct = c.T

#print(ct)

print(ct.shape)

cf = np.matmul(c, ct)

#cf = cf.astype('float32')

#input()

#cf = cf.flatten()

#print(cf)

print(cf.shape)

trdata = "/content/trdata.h5"

traininghalf = h5py.File(trdata, 'w')

traininghalf.create_dataset("before_inversion", data = cf)

traininghalf.close()

import tensorflow as tf

import numpy as np

import h5py

traininghalf = h5py.File("/content/trdata.h5", 'r')

cf = traininghalf["before_inversion"][:, :]

print(cf.shape)

cf = cf.astype('float64')

#rhs = np.ones((cf.shape[0], cf.shape[1]))

ci = np.linalg.inv(cf)

#print(ci)

print(ci.shape)

#ci = np.abs(ci)

#print(ci)

#print(ci.shape)

alp = np.matmul(ci, c)

alp = np.abs(alp)

#print(alp)

print(alp.shape)

alpha = alp * y_label[:, None]

#print(alpha)

print(alpha.shape)

WEIGHT = "/content/trainedweigtsforbees.h5" 

weight = h5py.File(WEIGHT, "w")

weight.create_dataset("weight_alpha", data = alpha)

weight.close()

end_time = datetime.now()

print("ENDED AT : ", end_time)

print("EXECUTION TIME : ", end_time - start_time)
