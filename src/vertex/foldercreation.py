from class_df_maker import class_df_maker
import pandas as pd
import shutil
import os



def foldercreation():
	'''
	foldercreation: create foldders and seperates the images into these folders
	'''
	class_df=class_df_maker()
	newclasses = ["HighSchool", "Skyline", "Police", "Busing", "Court", "Low-income","Celtics","Lawyer", "arrest", "Protest", "housing", "Fire"  ]

	src_dir='data/all_images/'
	class_dir="data/classes/"


	for i in newclasses: 
		i_df=class_df[class_df["class"]==i] #makes a pandas data frame for the classs
		path = os.path.join(class_dir, i) #creates the path to the class
		if not os.path.isdir(path):
			os.mkdir(path)


		for j in i_df["Id"]:
			try:
				src = os.path.join(src_dir, j) #finds the image in the all image folder
				dst=path+"/"+ j # creates a new path for the class image
				shutil.copyfile(src, dst) #moves the image
			except Exception as e:
				print(e)
				continue
if __name__ == "__main__":
	foldercreation()