#HI GUYS lets check if this works (each person write their name below as a comment, commit, then push to main!)
#fiona
#kavya

import pandas as pd

#read in data + get its info
data = pd.read_csv("flavors_of_cacao.csv")
data.head()
data.info()

#drop redundant columns
data = data.drop(columns=["REF", "Review\nDate", "Bean\nType"])
data.head()

#save the cleaned data to csv file
data.to_csv("cleaned_dataset_flavors_of_cacao.csv", index=False)

