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

def num_approved_by_therapy_area(df):
    return None

def num_approved_by_company_by_date(df):
    return None

def num_approved_by_company_per_therapy_area(df):
    return None

def num_approved_by_therapy_area_by_date(df):
    return None

def num_FDA_approvals_by_year():
    approvals_a_year = fdadf.groupby('Approval_Year')['Applicant'].count()
    approvals_a_year.reset_index().to_csv('FDA_Module/Data_Manipulation/approval_a_year.csv')
   
   

num_FDA_approvals_by_year()