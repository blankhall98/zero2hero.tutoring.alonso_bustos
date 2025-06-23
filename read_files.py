# read_files.py

#import pandas
import pandas as pd

#define route
file_route = './data/'
file_name = 'stocks.csv'
route = file_route+file_name

#read the file
file = pd.read_csv(route)

#first 5 rows
file.head()

#describe the file
file.describe()

#select one column
price = file['Price']

#remove comma from price column
price = []
for p in file['Price']:
    if ',' in p:
        p_split = p.split(',')
        p_ = p_split[0]+p_split[1]
        price.append(float(p_))
    else:
        price.append(float(p))
file['Price'] = price