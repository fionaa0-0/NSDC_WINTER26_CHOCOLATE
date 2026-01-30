#HI GUYS lets check if this works (each person write their name below as a comment, commit, then push to main!)
#fiona
#kavya

import pandas as pd

data = pd.read_csv("flavors_of_cacao.csv")
data.head()
data.info()

data = data.drop(columns=["REF", "Review\nDate", "Bean\nType"])