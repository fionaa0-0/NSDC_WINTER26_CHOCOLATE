#HI GUYS lets check if this works (each person write their name below as a comment, commit, then push to main!)
#fiona
#kavya

import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

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


# Fiona visualization!
# trying a simple linear regression model to check if the rating is based on the cocoa percent
cleaned_flavors = pd.read_csv("cleaned_dataset_flavors_of_cacao.csv")

cleaned_flavors['Cocoa\nPercent'] = (
    cleaned_flavors['Cocoa\nPercent']
    .str.replace('%', '', regex=False)
    .astype(float)
)

X = cleaned_flavors[['Cocoa\nPercent']]
y = cleaned_flavors['Rating']

model = LinearRegression()
model.fit(X, y)

# Sort values so the line is not jagged
X_sorted = np.sort(X.values, axis=0)
y_pred = model.predict(X_sorted)

plt.figure()
plt.scatter(X, y)
plt.plot(X_sorted, y_pred)
plt.xlabel("Cocoa Percent")
plt.ylabel("Rating")
plt.title("Linear Regression: Rating vs Cocoa Percent")
plt.show()
#shows that people tend to like lower cocoa percentages!
