import csv

import numpy as np
from sklearn.metrics import jaccard_similarity_score
import pandas as pd
import re
import difflib
import nltk.classify.util
import sklearn as sk
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from IPython.display import display
from sklearn.model_selection import cross_val_score
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from sklearn.feature_extraction.text import TfidfVectorizer

#Classifies the uses with MultinomialNB

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

use_codes = fdadf[[' Use Code', 'Use']]
use_codes = use_codes.drop_duplicates()
use_codes[' Use Code'].replace(r'\s+|\\n', ' ', regex=True, inplace=True) 
use_codes.name = 'uses_list'
use_dic = dict(use_codes[[' Use Code', 'Use']].values)

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

use_codes['Use']=use_codes['Use'].str.lower()
use_codes['Use'] = use_codes['Use'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))


#CREATING TRAINING SET FROM TREATMENTS https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f
    #Creating therapy group IDs
treatments['therapy_area_id'] = treatments['Therapy_area'].factorize()[0]
therapy_id_df = treatments[['Therapy_area', 'therapy_area_id']].drop_duplicates().sort_values('therapy_area_id')
therapy_to_id = dict(therapy_id_df.values)
id_to_treatment = dict(therapy_id_df[['therapy_area_id', 'Therapy_area']].values)

     # getting TFIDF (Term Frequency, Inverse Document Frequency)
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

features = tfidf.fit_transform(treatments.treatment).toarray()
labels = treatments['therapy_area_id']
#print(features.shape)

    #find terms most correlated to each therapy area
N = 2
for Therapy_area, therapy_area_id in sorted(therapy_to_id.items()):
  features_chi2 = chi2(features, labels == therapy_area_id)
  indices = np.argsort(features_chi2[0])
  feature_names = np.array(tfidf.get_feature_names())[indices]
  unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
  bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
  #print("# '{}':".format(Therapy_area))
  #print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-N:])))
  #print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-N:])))

      #Fitting training set LOGISTIC REGRESSION
X_train, X_test, y_train, y_test = train_test_split(treatments['treatment'], treatments['Therapy_area'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#clf = MultinomialNB().fit(X_train_tfidf, y_train)
#clf = LinearSVC().fit(X_train_tfidf, y_train)
clf = LogisticRegression().fit(X_train_tfidf, y_train)
#clf = RandomForestClassifier().fit(X_train_tfidf, y_train)


    #Prediction LOGISTIC REGRESSION

with open('FDA_Module/therapeuticGroups.csv', mode='w') as FDA_file:
    use_writer = csv.writer(FDA_file, delimiter=',')
    use_writer.writerow([ ' Use Code', 'Use','Treatment' 'Therapeutic_Area'])
        
    for index, row in use_codes.iterrows():
        tarea = clf.predict(count_vect.transform([row.Use]))
        print(use_codes[' Use Code'][index], row.Use, tarea)
        use_writer.writerow([use_codes[' Use Code'][index], row.Use, tarea])

    #model selection
        #Comparing model accuracy
models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]

CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []
for model in models:
  model_name = model.__class__.__name__
  accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
  for fold_idx, accuracy in enumerate(accuracies):
    entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])

cv_df.groupby('model_name').accuracy.mean()
