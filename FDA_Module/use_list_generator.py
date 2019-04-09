import csv

import pandas as pd



dtype_dic = {'Appl_No': str,
             'Product_No': str,
             'Type' : str,
             'Patent_No' : str,
             'Trade_Name' : str,
             'Drug' : str,
             'Therapy_area' : str
             }

fdadf = pd.read_csv("FDA_Module/fda.csv", dtype=dtype_dic)
fdadf = fdadf.drop_duplicates()
drugs = pd.read_csv("FDA_Module/therapydrugs.csv", dtype=dtype_dic)
therapy_area = pd.read_csv("FDA_Module/therapyurls.csv", dtype=dtype_dic)

def write_use_list(df):
    with open('FDA_Module/'+df.name+'.csv', mode='w') as FDA_file:
        use_writer = csv.writer(FDA_file, delimiter=',')
        use_writer.writerow([ ' Use Code', 'Use'])
        for index, row in df.iterrows():
            use_writer.writerow([row[' Use Code'], row['Use']])


use_codes = fdadf[[' Use Code', 'Use']]
use_codes = use_codes.drop_duplicates()
use_codes[' Use Code'].replace(r'\s+|\\n', ' ', regex=True, inplace=True) 
use_codes.name = 'uses_list'

new = drugs["Drug"].str.split(";", expand = True)
drugs["Drug"] = drugs["Drug"].str.split(";", expand = True)
drugs["Drug"] = drugs["Drug"].str.upper()
therapy_area["Therapy_area"] = therapy_area["Therapy_area"].str.upper()
drugs["treatment"] = new[2]
therapyDrugs = pd.merge(drugs,therapy_area, on = ['URL'])


trying = fdadf["Trade_Name"].str.contains("ZOSYN")

print(therapyDrugs)
