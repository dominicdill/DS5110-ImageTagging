import os
import bs4
from bs4 import BeautifulSoup
def preprocess():
	'''
	preprpocess: Takes the meta data and tries to get any useful data
	There are two different methods of meta data in the data set so there are some problems
	
	'''
	dir_list=os.listdir("data/metadata/")
	meta_list=[] #This is the desription of the image 
	uasc_list=[] #This is the image name
	for i in dir_list:
	    with open(f'data/metadata/{i}', 'r') as f:
	        try: #Used to not stop the program if there is some sort of error
	            data = f.read() 
	        except:
	            continue
	    xml_data = BeautifulSoup(data, "xml") #XML parser
	    title= xml_data.find_all('mods:title') 
	    asi= xml_data.find_all('mods:identifier')

	    #sorts out meta data without image desccription
	    if (type(title) == bs4.element.ResultSet) and len(title) >0:
	    	#The two types of meta data are differentiated by the first title tag haviing "M142" in it
	        if "M142" in str(list(title)[0]):
	            try:
	            		#Some of the meta data is not complete, so we need to sort out
	                    if str(xml_data.find('mods:topic')) != "None":
	                        uasc_list.append(str(list(title)[0]).split(">")[1].split("<")[0]+"_Front.tif")
	                        meta_list.append(str(xml_data.find('mods:topic')).split(">")[1].split("<")[0])
	            except:
	                    pass

	           
	        if "M142" not in str(list(title)[0]) and str(asi) != "None":
	            try:
	                for i in list(asi):
	                	#Need to find the image files
	                    if "tif" in str(i) and "displayLabel" not in str(i):
	#                         print(i,"\n")
	                        meta_list.append(str(list(title)[0]).split(">")[1].split("<")[0])
	                        uasc_list.append(str(i).split(">")[1].split("<")[0])

	            except:
	                continue
	return meta_list, uasc_list


if __name__=="__main__":
	meta_list, uasc_list=preprocess()
	print(meta_list[:10], uasc_list[:10])


