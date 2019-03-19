import csv

import pandas as pd

from readFile import createFDA_df

dtype_dic = {'Appl_No': str,
             'Product_No': str}

usesdf = pd.read_csv("FDA_Module/uses.csv", dtype=dtype_dic)
urlsdf = pd.read_csv("FDA_Module/urls.csv", dtype=dtype_dic)
urlsAndUsedf = pd.merge(urlsdf, usesdf, on='URL')
urlsAndUsedf = urlsAndUsedf.drop_duplicates()
urlsdf = urlsdf.drop_duplicates()

completedf = pd.merge(createFDA_df(), urlsAndUsedf, on=[
                      'Appl_No', 'Product_No', 'Appl_Type'])
completedf = completedf.drop_duplicates()
completedf.name = 'fda'


def writeCSV(df):
    with open('FDA_Module/'+df.name+'.csv', mode='w') as FDA_file:
        use_writer = csv.writer(FDA_file, delimiter=',')
        use_writer.writerow(['Appl_No', 'Trade_Name', 'Ingredient', 'Applicant', 'Approval_Date', 'Type', 'Product_No', 'Patent_No',
                             'Patent_Use_Code', 'Submission_Date', 'Appl_Type', 'Exclusivity_Code', 'Exclusivity_Date', 'URL', ' Use Code', 'Use'])
        for index, row in df.iterrows():
            use_writer.writerow([row['Appl_No'], row['Trade_Name'], row['Ingredient'], row['Applicant'], row['Approval_Date'], row['Type'], row['Product_No'], row['Patent_No'],
                                 row['Patent_Use_Code'], row['Submission_Date'], row['Appl_Type'], row['Exclusivity_Code'], row['Exclusivity_Date'], row['URL'], row[' Use Code'], row['Use']])


def Approval_Date():
    app_date = completedf.groupby('Approval_Date')
    app_date.name = 'approval_date_gb'
    return app_date

def Use_Group():
    use_group = completedf.groupby('Use')
    use_group.name = 'use_group_gb'
    return use_group

#writeCSV(completedf)
writeCSV(Approval_Date())
writeCSV(Use_Group())
