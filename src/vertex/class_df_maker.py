from preprocess import preprocess
import pandas as pd

def classified(x,i,classes):
	'''
	classified: lambda function to create a class function based on string comparison
	'''
	for i in classes:
		if i.lower() in x.lower():
			return i.replace(" ","")
	else:
		return -1

def class_df_maker():
	'''
	class_df_maker: creates a dataframe with labeled data and meta data image names
	'''

	classes = ["High School", "Skyline", "Police", "Busing", "Court", "Low-income","Celtics","Lawyer", "arrest", "Protest", "housing", "Fire"  ]


	meta_list, uasc_list=preprocess()
	
	df =pd.DataFrame(list(zip(uasc_list,meta_list )), columns =['Id', 'Meta'])
	for i in classes:
		df["class"]=df['Meta'].apply(lambda x: classified(x,i,classes))
	class_df=df[df["class"]!=-1]


	return class_df




if __name__ == "__main__":
	print(class_df_maker())