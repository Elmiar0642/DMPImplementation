from training_model2 import train_model

import datetime, os

start_time = datetime.datetime.now()

print("started at : {}".format(start_time))

train_model()

end_time = datetime.datetime.now()

print("ended at : {}".format(end_time))

print("Execution Time : ", end_time - start_time)
