import os
import pandas as pd
from datetime import datetime
import deepface.detectors.FaceDetector as FD
from deepface.commons.functions import load_image


img_path='./data/all_images/'
out_path = './data/deepface_tags/face_counts/'

detector_backend = 'opencv'
face_detector = FD.build_model(detector_backend)

file_dict={}
faces_list=[]
for entry in os.scandir(img_path):
    if entry.is_file():
        if entry.name.startswith('.'):
            continue
        if entry.name.endswith('Verso.tif'):
            continue
        img=load_image(entry.path)
        faces = FD.detect_faces(face_detector, detector_backend, img, align=True)
        file_dict[entry.name]=len(faces)

df=pd.DataFrame(file_dict.items(),columns=['FileName','#DetectedFaces'])

now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d_%H%M%S")
filename ='FaceCount_'+date_time_str+'.csv'
df.to_csv(os.path.join(out_path,filename))

