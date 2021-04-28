import numpy as np

from PIL import Image, ImageOps

import matplotlib.pyplot as plt

import h5py

from datetime import datetime

start_time = datetime.now()

print("STARTED AT : ", start_time)

P = []*0

DIR = "A:\\Arima\\PROJECTS\\Outbox\\Test5\\a\\train_data.h5"

WEIGHT = "weight_data.h5"

files = h5py.File(DIR, 'r+')

wt_file = h5py.File(WEIGHT, 'w')

labels = []*0

for category in files.keys():

    for subcategory in files[category].keys():

        if subcategory[:3] not in labels:

            labels.append(subcategory[:3])

        replacementval = labels.index(subcategory[:3])+1

        files[category][subcategory][:, :, -1] = replacementval

        shape = files[category][subcategory][:, :, :].shape

        for j in range(shape[1]):

            files[category][subcategory][:, j, :] = np.roll(files[category][subcategory][:, j, :], 1)

        img = files[category][subcategory][:, :, :]

        P.append(img)

P = np.array(P)

print(P.shape)

P = P.transpose(1, 2, 3, 0)

print(P.shape)

PT = P.transpose(1, 0, 2, 3)

print(P.shape, PT.shape)

PIPT = P * PT

I = np.random.normal(0,1,(PIPT.shape[0], PIPT.shape[1], PIPT.shape[2], PIPT.shape[3]))

print(PIPT.shape, I.shape)

PIPTPI = PIPT + I

print(PIPTPI.shape)

PIPTPII = np.linalg.inv(PIPTPI.T)

print(PIPTPII.shape)

alpha = PIPTPII.T * PT

print(alpha.shape)

wt_file.create_dataset("weight_alpha", data = alpha)

wt_file.close()

end_time = datetime.now()

print("ENDED AT : ", end_time)

print("EXECUTION TIME : ", end_time - start_time)
