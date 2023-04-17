from class_df_maker import class_df_maker




def jsonl_maker():
	class_df=class_df_maker()
	newclasses = ["HighSchool", "Skyline", "Police", "Busing", "Court", "Low-income","Celtics","Lawyer", "arrest", "Protest", "housing", "Fire"  ]

	src_dir='data/all_images/'
	par_dir="data/classes/"
	for i in newclasses:   
		i_df=class_df[class_df["class"]==i]
		print(i_df)
		# length=i_df.shape[0]
  #   	count=0
  #   	for  in df[df["class"]==i]
  #   	path = os.path.join(par_dir, i)




if __name__ == "__main__":
	jsonl_maker()