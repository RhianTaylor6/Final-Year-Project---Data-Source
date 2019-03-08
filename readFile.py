import pandas as pd
import useCode


dtype_dic= {'Appl_No': str, 
            'Product_No' : str}

drugsFDAdf = pd.read_csv("tmpfdazip/products.txt", delimiter='~', dtype = dtype_dic)
patentFDAdf = pd.read_csv("tmpfdazip/patent.txt", delimiter='~', dtype = dtype_dic)
exclusivityFDAdf = pd.read_csv("tmpfdazip/exclusivity.txt", dtype = dtype_dic)



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

def add_Use():
    usesFDAdf = pd.read_csv('uses.csv')
    print(usesFDAdf)

createFDA_df()
useSearch()
