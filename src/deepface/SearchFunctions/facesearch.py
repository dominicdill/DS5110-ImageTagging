from deepface import DeepFace
import os
import pandas as pd
from datetime import datetime


#the DeepFace.find method will not recognize .tif files in db_path. 
#can edit line 463 of DeepFace.py source file to include .tif files, or just don't include tif files in db_path

db_path = './data/all_images' #images to search for known face
known_face_db = './data/deepface_known_faces' #images of known faces we want to look for in db_path
out_path = './data/deepface_tags/face_search' #output file location

detectors = ['opencv', 'retinaface', 'mtcnn', 'ssd', 'dlib', 'mediapipe']
models = ['VGG-Face','Facenet', 'Facenet512', 'OpenFace', 'DeepFace', 'DeepID', 'Dlib', 'ArcFace', 'SFace', 'Ensemble']

dfs={}
#loop through the known faces we want to search our database for
for entry in os.scandir(known_face_db):
    if entry.is_file():
        if (
            (entry.name.lower().endswith('.jpg'))
            or (entry.name.lower().endswith('.jpeg'))
            or (entry.name.lower().endswith('.png'))
            or (entry.name.lower().endswith('.tif'))        
        ):
            dfs[entry.name] = DeepFace.find(entry.path,db_path,enforce_detection=False,detector_backend=detectors[0],model_name=models[0])



df=pd.DataFrame()
for i in dfs.keys():
    dfs[i][0]['KnownFaceFile']=i
    df=pd.concat([df,dfs[i][0]],axis=0)

now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d_%H%M%S")
filename ='FaceSearch_'+date_time_str+'.csv'
df.to_csv(os.path.join(out_path,filename))