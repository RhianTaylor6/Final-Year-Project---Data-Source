import pandas as pd
drugsFDAdf = pd.read_csv("tmpfdazip/products.txt", delimiter='~')
patentFDAdf = pd.read_csv("tmpfdazip/patent.txt", delimiter='~')
exclusivityFDAdf = pd.read_csv("tmpfdazip/exclusivity.txt", delimiter='~')


def createFDA_df():

    patentFDAdfCleaned = patentFDAdf[['Appl_No', 'Product_No', 'Patent_No','Patent_Use_Code','Submission_Date', 'Appl_Type']]
    exclusivityFDAdfCleaned = exclusivityFDAdf[['Appl_No', 'Exclusivity_Code','Exclusivity_Date']]
    drugsFDAdfCleaned = drugsFDAdf[['Appl_No', 'Trade_Name', 'Ingredient', 'Applicant', 'Approval_Date', 'Type']]

    FDAdf = pd.merge(patentFDAdfCleaned, exclusivityFDAdfCleaned, on='Appl_No')
    FDAdf1 = pd.merge(drugsFDAdfCleaned, FDAdf,  on='Appl_No')
    
    return FDAdf1


def useSearch():
    patentFDAdfCleaned = patentFDAdf[[ 'Product_No','Appl_No', 'Appl_Type','Patent_Use_Code']]

    return patentFDAdfCleaned