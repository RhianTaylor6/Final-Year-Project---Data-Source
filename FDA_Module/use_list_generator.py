import csv

import pandas as pd

from fuzzywuzzy import fuzz
from fuzzywuzzy import process


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
    with open('FDA_Module/therapeuticGroups.csv', mode='w') as FDA_file:
        use_writer = csv.writer(FDA_file, delimiter=',')
        use_writer.writerow([ ' Use Code', 'Use', 'Therapeutic_Area', 'Use_Treatment_WRatio'])
        for index, row in df.iterrows():
            use_writer.writerow([row[' Use Code'], row['Use'],row['Therapeutic_Area'], row['Use_Treatment_WRatio']])


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
therapyDrugs["treatment"].replace(r'\s+|\\n', ' ', regex=True, inplace=True) 
therapyDrugs["treatment"] = therapyDrugs["treatment"].str.upper()


treatments = therapyDrugs[['treatment','Therapy_area']]
highest_ratio = 0
use_therapy = pd.DataFrame({" Use Code":[], "Therapeutic_Area":[],"Use_Treatment_WRatio":[]})   

with open('FDA_Module/therapeuticGroups.csv', mode='w') as FDA_file:
    use_writer = csv.writer(FDA_file, delimiter=',')
    use_writer.writerow([ ' Use Code', 'Use', 'Therapeutic_Area', 'Use_Treatment_WRatio'])   
    for indexA, row in treatments.iterrows():
        treatmentSTR = row.treatment
        for indexB,row in use_codes.iterrows():
            useSTR = row.Use
            ratio = fuzz.WRatio(treatmentSTR, useSTR)
            if ratio >= highest_ratio:
                highest_ratio = ratio
                use_writer.writerow([use_codes[' Use Code'][indexB], use_codes['Use'][indexB],treatments['Therapy_area'][indexA], str(highest_ratio)])
                use_therapy.append({" Use Code":[use_codes[' Use Code'][indexB]],"Therapeutic_Area":[treatments['Therapy_area'][indexA]], "Use_Treatment_WRatio": [str(highest_ratio)]},ignore_index=True)
                print([use_codes[' Use Code'][indexB], use_codes['Use'][indexB],treatments['Therapy_area'][indexA], str(highest_ratio)])
                #print([use_codes[' Use Code'][indexB], use_codes['Use'][indexB],treatments['Therapy_area'][indexA], str(highest_ratio)])
#use_codes = pd.merge(use_codes,use_therapy, on = [' Use Code'])
#write_use_list(use_codes)



        
