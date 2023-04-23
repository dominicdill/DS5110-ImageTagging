from fastbook import *
from fastai.vision.widgets import *

import itertools
import pandas as pd

#import model
learn_inf = load_learner('export.pkl')


# create dataframe of the predictions
folder_dir = "data/all_images/"
tensors = []
for image in os.listdir(folder_dir):
  prediction = learn_inf.predict(f"{folder_dir}{image}")
  tensors.append(list(prediction))

photos = [[i] for i in os.listdir(folder_dir)]
zipped = [list(e) for e in zip(tensors,photos)] 

list_tensors = []

for row in zipped:
  temp = list(itertools.chain.from_iterable(row))
  list_tensors.append(temp)

for pred in list_tensors:
  temp = pred[2].tolist()
  pred.append(temp)

df = pd.DataFrame(list_tensors, columns = ["prediction","tensor binary","tensorprobs","image_name","probs"])
df[['prob skyline','prob person']] = pd.DataFrame(df.probs.tolist(), index= df.index)