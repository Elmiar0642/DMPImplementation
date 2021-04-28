import numpy as np

from PIL import Image, ImageOps

import matplotlib.pyplot as plt

import h5py, random

from pathlib import Path

from datetime import datetime

start_time = datetime.now()

print("STARTED AT : ", start_time)

P = []*0

DIR = "A:\\Arima\\PROJECTS\\Outbox\\Test5\\a\\weight_data.h5"

TEST = "A:\\Arima\\PROJECTS\\Outbox\\Test5\\a\\train_data.h5"

files = h5py.File(TEST, 'r')

category = random.choice(list(files.keys()))

subcategory = random.choice(list(files[category].keys()))

print(category, subcategory)

data = files[category][subcategory][:, :, :]

print(data.shape)

wtfile = h5py.File(DIR, 'r+')

dataset = list(wtfile.keys())

wt = np.array(wtfile[dataset[0]])

print(wt.shape)

wt = wt.transpose(3, 0, 1, 2)

print(wt.shape)

#wtl = wt[:, :, :, 0]
#wtra = wt[:, :, :, :] * wtl[:, :, :, None]
#wtra = np.array(wtra[:, :, :, 0])
#print(wtra.shape)

scores = []*0

weightkeys = []*0

for i in range(wt.shape[0]):

    #print(wt[i])

    #input()
    
    y_score = data[:, :, :] * wt[i][:, :, :]

    y_score = np.abs(np.mean(y_score[:, :, 0]))

    #print(y_score)

    while (y_score<0.1):

        y_score *= 10

    scores.append(round(y_score, 2))
    weightkeys.append(i)

print(scores, len(scores))

print(max(scores)*100, int(subcategory[:3]), scores.index(max(scores)))

end_time = datetime.now()

print("STARTED AT : ", end_time)

print("STARTED AT : ", end_time - start_time)

