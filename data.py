#annualmvpop_dataset.csv
import csv
import pandas as pd

data_doc = open("annualmvpop_dataset.csv")                              #opening the csv file
header = data_doc.readline()
pop_data = pd.read_csv("annualmvpop_dataset.csv")

#print( pop_data['Fuel Type'], pop_data['2010'])
