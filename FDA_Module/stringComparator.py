import csv

import numpy as np
from sklearn.metrics import jaccard_similarity_score
import pandas as pd
import re
import difflib
import nltk.classify.util
import sklearn as sk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#This module applies fuzzy logic to the strings gathered from useCode.py and therapy_are.py
#Through calculating the WRatio of the two strings it is possible to assign generalised therapy groups to the FDA use codes
#TAKES A WHILE TO RUN

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
stop = stopwords.words('english')


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
therapyDrugs["treatment"] = therapyDrugs["treatment"].str.lower()



treatments = therapyDrugs[['treatment','Therapy_area']]
treatments['treatment'] = treatments['treatment'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
new2 = treatments['treatment'].str.split(", approved", expand = True)
treatments['treatment'] = new2[0]
treatments['treatment'] = treatments['treatment'].str.upper()
use_codes['Use']=use_codes['Use'].str.lower()
use_codes['Use'] = use_codes['Use'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
use_codes['Use'] =use_codes['Use'].str.upper()

# RATIO COMPARISON IMPORTANT
highest_WRatio = 0
highest_PRatio = 0
highest_TSortRatio = 0
highest_TSetRatio = 0
highest_Ratio = 0
use_therapy = pd.DataFrame({" Use Code":[], "Therapeutic_Area":[],"Use_Treatment_WRatio":[]})   

with open('FDA_Module/therapeuticGroupsTRY.csv', mode='w') as FDA_file:
    use_writer = csv.writer(FDA_file, delimiter=',')
    use_writer.writerow([ ' Use Code', 'Use','Treatment' 'Therapeutic_Area', 'Use_Treatment_WRatio','Use_Treatment_PRatio','Use_Treatment_TSortRatio','Use_Treatment_TSetRatio','Use_Treatment_TSetRatio'])   
    
    for indexB,row in use_codes.iterrows():
        useSTR = row.Use
        for indexA, row in treatments.iterrows():
            treatmentSTR = row.treatment
            WRatio = fuzz.WRatio(treatmentSTR, useSTR)
            PRatio = fuzz.partial_ratio(treatmentSTR, useSTR)
            TSortRatio = fuzz.token_sort_ratio(treatmentSTR, useSTR)
            TSetRatio = fuzz.token_set_ratio(treatmentSTR, useSTR)
            Ratio = fuzz.ratio(treatmentSTR, useSTR)
            if Ratio >= highest_Ratio and WRatio >= highest_WRatio and PRatio >= highest_PRatio and TSetRatio >= highest_TSetRatio and TSortRatio >= highest_TSortRatio :
                highest_WRatio = WRatio
                highest_PRatio = PRatio
                highest_TSortRatio = TSortRatio
                highest_TSetRatio = TSetRatio
                highest_Ratio = Ratio
                useCode = use_codes[' Use Code'][indexB]
                tarea = treatments['Therapy_area'][indexA]
        use_writer.writerow([useCode, useSTR, treatmentSTR, tarea, highest_WRatio, highest_PRatio, highest_TSortRatio,highest_TSetRatio,highest_Ratio])
                #use_therapy.append({" Use Code":[use_codes[' Use Code'][indexB]],"Therapeutic_Area":[treatments['Therapy_area'][indexA]], "Use_Treatment_WRatio": [str(highest_WRatio)],"Use_Treatment_PRatio": [str(highest_PRatio)]},ignore_index=True)
                #NEED THIS#print([use_codes[' Use Code'][indexB], use_codes['Use'][indexB],treatments['Therapy_area'][indexA], str(highest_WRatio), str(highest_PRatio), str(highest_TSortRatio),str(highest_TSetRatio),str(highest_Ratio)])
        print( useCode, useSTR,treatmentSTR,  tarea,  highest_PRatio, highest_WRatio, highest_Ratio, highest_TSetRatio, highest_TSortRatio)

#use_codes = pd.merge(use_codes,use_therapy, on = [' Use Code'])
#write_use_list(use_codes)



