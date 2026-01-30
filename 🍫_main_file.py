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

whitespace_only = (data["Broad Bean\nOrigin"].astype(str).str.strip() == "").sum()
whitespace_only

#since there are only 73 out of our thousand obs that are NA, (less than 5% of our data), we can go ahead and just delete those rows 
#now we want to delete the rows 
data = data[data["Broad Bean\nOrigin"].astype(str).str.strip() != ""]
data.info()

#save the cleaned data to csv file
data.to_csv("cleaned_dataset_flavors_of_cacao.csv", index=False)

#now we want to read in the 2nd dataset!
data2 = pd.read_csv("Chocolate Sales.csv")
data.head()
data.info()

#check if we have all values 
data.isna().sum()

