import pandas as pd

frame = pd.read_csv("lego_setsHB.csv")

#1.Use the .info() and .describe() functions to have an overall description of the dataset
print("\n--------------1---------------\n")
print(frame.info(), "\n")
print(frame.describe())

#2. Use boolean operators find the Lego sets which have star_rating greater than or equal to 4.
print("\n--------------2---------------\n")
print(frame.loc[frame["star_rating"] >= 4, ["prod_id"]])

#3. Find the number of Lego sets whose star_rating greater than or equal to 4. (Hint: conside using .count( ) on the specified column)
print("\n--------------3---------------\n")
print(frame.loc[frame["star_rating"] >= 4, ["star_rating"]].count())

#4. Find the average list price for the Lego sets whose star_rating greater than or equal to 4. (Hint: consider specifying the list_price column after obtaining data and before taking the average)
print("\n--------------4---------------\n")
print(frame.loc[frame["star_rating"] >= 4, ["list_price"]].mean())