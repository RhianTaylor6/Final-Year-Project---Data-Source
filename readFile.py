import pandas as pd

drugsFDAdf = pd.read_csv("tmpfdazip/products.txt", delimiter='~')
patentFDAdf = pd.read_csv("tmpfdazip/patent.txt", delimiter='~')
exclusivityFDAdf = pd.read_csv("tmpfdazip/exclusivity.txt", delimiter='~')

# print(drugsFDAdf.head)
print(list(drugsFDAdf))
print(list(patentFDAdf))
print(list(exclusivityFDAdf))

patentFDAdfCleaned = patentFDAdf[['Appl_No', 'Product_No', 'Patent_No', 'Submission_Date']]
exclusivityFDAdfCleaned = exclusivityFDAdf[['Appl_No', 'Exclusivity_Code','Exclusivity_Date']]
drugsFDAdfCleaned = drugsFDAdf[['Appl_No', 'Trade_Name', 'Ingredient', 'Applicant', 'Approval_Date', 'Type']]

FDAdf = pd.merge(patentFDAdfCleaned, exclusivityFDAdfCleaned, on='Appl_No')
FDAdf = pd.merge(drugsFDAdfCleaned, FDAdf,  on='Appl_No')
#drugsFDAdfCleaned = drugsFDAdfCleaned.drop_duplicates()
#drugsFDAdfCleaned = drugsFDAdfCleaned.groupby('Applicant')
print(FDAdf)
#print(drugsFDAdfCleaned)
# for key, items in drugsFDAdfCleaned:
# print(drugsFDAdfCleaned.get_group(key))
