from class_df_maker import class_df_maker
import pandas as pd
import json


def jsonl_maker():
	'''
	jsonl_maker: creates a jsonl file that has the could storage path and if the data is test, trainging, or validation
	'''
	class_df=class_df_maker()
	newclasses = ["HighSchool", "Skyline", "Police", "Busing", "Court", "Low-income","Celtics","Lawyer", "arrest", "Protest", "housing", "Fire"  ]

	src_dir='data/all_images/'
	par_dir="data/classes/"

	
	for i in newclasses:   
		i_df=class_df[class_df["class"]==i]
		
		length=i_df.shape[0]
		count=0
		for j in i_df["Id"]:
			try:
				image=j
				if count<length*0.7:
					js={"imageGcsUri":f"gs://cloud-ai-platform-c15e02cf-fb21-4689-b624-5bb8c9f8ead9/{i}/{j}","classificationAnnotation": {"displayName": i}, "dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "test"}}
				elif count<length*0.9:
					js={"imageGcsUri":f"gs://cloud-ai-platform-c15e02cf-fb21-4689-b624-5bb8c9f8ead9/{i}/{j}","classificationAnnotation": {"displayName": i}, "dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "training"}}
				else:
					js={"imageGcsUri":f"gs://cloud-ai-platform-c15e02cf-fb21-4689-b624-5bb8c9f8ead9/{i}/{j}","classificationAnnotation": {"displayName": i}, "dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "valiation"}}
				with open("src/vertex/split.jsonl", "a") as f:
					json.dump(js,f)
					f.write('\n')
			except Exception as e:
				print(e)
				continue
			count=count+1

if __name__ == "__main__":
	jsonl_maker()