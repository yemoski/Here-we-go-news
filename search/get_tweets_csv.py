import pandas as pd
import re
def get_tweet():
	df  = pd.read_csv('tweets.csv',header=None , names=['tweet','likes','time','url','img'] )

	df = df.iloc[1:,:]
	#for x in df['img']:
		#print(x.strip("[]'"))

	return df

