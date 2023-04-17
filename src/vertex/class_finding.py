from preprocess import preprocess
from collections import Counter
import pandas as pd

def class_findng():
	'''
	class_findng: Takes the list of meta data and then see if there are any communalities in order to 
	find classes. This is done by using a counter and then manually choosing potential targets  
	'''
	meta_list, uasc_list=preprocess()

	#This makes a list of all words to see which appear the most
	word_list =[]

	#These words do not give us anything of value
	stopwords = ['the', 'is', 'at','a','of','in', 'which', 'and', 'on', 'with', 'that']


	#Splits the words for each meta data line
	for i in meta_list:
		word_list=word_list+i.split(" ")

	#Makes a counter to count frequencies and then deletes the stop words
	counter = Counter(word_list)
	for sword in stopwords:
		del counter[sword]


	df = pd.DataFrame.from_dict(counter, orient='index').reset_index()
	df = df.rename(columns={'index':'word', 0:'count'})
	print(df.sort_values(by='count', ascending=False).head(50))



if __name__ == "__main__":
	class_findng()
