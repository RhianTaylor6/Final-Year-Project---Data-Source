import csv

import pandas as pd

#Merges the file created by stringComparator (therapeuticGroup.csv) with the FDA csv to create a complete data set
dtype_dic = {' Use Code': str,
             'Use': str,
             'Appl_No': str,
             'Product_No': str,
             'Type' : str,
             'Patent_No' : str,
             'Therapeutic_Area' : str
             }
             

therapeuticGroupsdf = pd.read_csv("FDA_Module/therapeuticGroups.csv", dtype=dtype_dic)
therapeuticGroupsdf = therapeuticGroupsdf[[" Use Code", "Therapeutic_Area"]]
fdadf = pd.read_csv("FDA_Module/fda.csv", dtype=dtype_dic)
fdadf[' Use Code'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)
fdadf = pd.merge(fdadf, therapeuticGroupsdf, on=" Use Code", how ='left')

def writeCSVdf(df):
    with open('FDA_Module/complete_FDA_dataset.csv', mode='w') as FDA_file:
        use_writer = csv.writer(FDA_file, delimiter=',')
        use_writer.writerow(['Appl_No', 'Trade_Name', 'Ingredient', 'Applicant', 'Approval_Date', 'Type', 'Product_No', 'Patent_No',
                             'Patent_Use_Code', 'Submission_Date', 'Appl_Type', 'Exclusivity_Code', 'Exclusivity_Date', 'URL', ' Use Code', 'Use','Therapeutic_Area'])
        for index, row in df.iterrows():
            use_writer.writerow([row['Appl_No'], row['Trade_Name'], row['Ingredient'], row['Applicant'], row['Approval_Date'], row['Type'], row['Product_No'], row['Patent_No'],
                                 row['Patent_Use_Code'], row['Submission_Date'], row['Appl_Type'], row['Exclusivity_Code'], row['Exclusivity_Date'], row['URL'], row[' Use Code'], row['Use'], row['Therapeutic_Area']])

writeCSVdf(fdadf)