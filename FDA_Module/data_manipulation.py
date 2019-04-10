import csv

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