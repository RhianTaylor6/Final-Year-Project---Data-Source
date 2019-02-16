import pandas as pd

drugsFDAdf = pd.read_csv("tmpfdazip/products.txt", delimiter='~')


# print(drugsFDAdf.head)
print(list(drugsFDAdf))

drugsFDAdfCleaned = drugsFDAdf[['Trade_Name', 'Applicant', 'Approval_Date']]
#drugsFDAdfCleaned = drugsFDAdfCleaned.drop_duplicates()
#drugsFDAdfCleaned = drugsFDAdfCleaned.groupby('Applicant')

print(drugsFDAdfCleaned)
# for key, items in drugsFDAdfCleaned:
# print(drugsFDAdfCleaned.get_group(key))
