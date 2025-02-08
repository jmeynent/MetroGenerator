import pandas as pd 

#Import data to have training data
idf = pd.read_csv('data/idf.csv', sep=";")
marseille = pd.read_csv('data/marseille.csv', sep=";")

name_idf = idf['nom_long']
name_marseille = marseille['Long Name']

names = pd.concat([name_idf, name_marseille])