import csv
import pandas as pd
import numpy as np
import datetime
import calendar
from collections import Counter
from itertools import groupby
import statistics
import pandas as pd

#This Module performs the data manipulation on the complete data set for the charts on the website
dtype_dic = {' Use Code': str,
             'Use': str,
             'Appl_No': str,
             'Product_No': str,
             'Type' : str,
             'Patent_No' : str,
             'Therapeutic_Area' : str
             }

fdadf = pd.read_csv("FDA_Module/complete_FDA_dataset.csv", dtype=dtype_dic)
fdadf = fdadf.drop_duplicates('Appl_No')
fdadf['Approval_Date']=pd.to_datetime(fdadf['Approval_Date'])
fdadf = fdadf.assign(Approval_Month=fdadf.Approval_Date.dt.month)
fdadf = fdadf.assign(Approval_Year=fdadf.Approval_Date.dt.year)

def num_approved_by_company(df):
    return None

def num_approved_in_therapy_area_by_top_ten_company(df):
    appDate_therapy = df.groupby(['Applicant','Therapeutic_Area'])['Appl_No'].count()
    appDate_therapy = appDate_therapy.to_frame(name = 'count')
    appDate_therapy=appDate_therapy.sort_values(by='count',ascending=False).head(11)
    pivot2 = appDate_therapy.pivot_table(index='Applicant', columns='Therapeutic_Area', values='count')
    pivot2.dropna()
    pivot2= pivot2.head(10)
    pivot2[np.isnan(pivot2)] = 0
    (pivot2).to_csv('FDA_Module/Data_Manipulation/num_approved_in_therapy_area_by_top_ten_company.csv')
    return None

def num_approved_a_year_by_top_ten_company(df):
    appDate_therapy = df.groupby(['Applicant','Approval_Year'])['Appl_No'].count()
    appDate_therapy = appDate_therapy.to_frame(name = 'count')
    appDate_therapy=appDate_therapy.sort_values(by='count',ascending=False).head(11)
    pivot2 = appDate_therapy.pivot_table(index='Applicant', columns='Approval_Year', values='count')
    pivot2.dropna()
    pivot2[np.isnan(pivot2)] = 0
    (pivot2).to_csv('FDA_Module/Data_Manipulation/num_approved_a_year_by_top_ten_company.csv')
    return None

def num_approved_by_company_per_therapy_area(df):
    return None

def num_approved_in_therapy_area_by_year(df):
    appDate_therapy = df.groupby(['Therapeutic_Area','Approval_Year'])['Appl_No'].count()
    appDate_therapy = appDate_therapy.to_frame(name = 'count')
    pivot = appDate_therapy.pivot_table(index='Therapeutic_Area', columns='Approval_Year', values='count')
    pivot[np.isnan(pivot)] = 0

    (pivot).to_csv('FDA_Module/Data_Manipulation/approved_a_year_by_therapy.csv')


    return None

def num_FDA_approvals_by_year():
    approvals_a_year = fdadf.groupby('Approval_Year')['Applicant'].count()
    
    data = []
    label =[]

    for index, val in approvals_a_year.items():
        data.append(val)
        label.append(index)
    with open('FDA_Module/Data_Manipulation/approval_a_year_data.csv', mode='w') as FDA_file:
        use_writer = csv.writer(FDA_file,delimiter='\\')
        for d in data:
            use_writer.writerow(str(d))
    with open('FDA_Module/Data_Manipulation/approval_a_year_label.csv', mode='w') as FDA_file:
        use_writer = csv.writer(FDA_file, delimiter='\\')
        for l in label:
            use_writer.writerow(str(l))
    
   
num_approved_in_therapy_area_by_top_ten_company(fdadf)  
num_approved_a_year_by_top_ten_company(fdadf)  
num_approved_in_therapy_area_by_year(fdadf)
num_FDA_approvals_by_year()