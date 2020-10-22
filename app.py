#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingRegressor


st.write("""
# Salary Prediction App
This app predicts the salary based on job type, degree, major, industry and etc.
""")

st.sidebar.header('User Input Features')

# Collects user input features into dataframe

def user_input_features():
    
    job_type = st.sidebar.selectbox('Job Type',('CFO', 'CEO', 'VICE_PRESIDENT', 
                                                    'MANAGER', 'JUNIOR', 'JANITOR',
                                                    'CTO', 'SENIOR'))
    degree = st.sidebar.selectbox('Degree',('MASTERS', 'HIGH_SCHOOL', 
                                                'DOCTORAL', 'BACHELORS', 'NONE'))
    major = st.sidebar.selectbox('Major',('MATH', 'NONE', 'PHYSICS', 'CHEMISTRY', 
                                              'COMPSCI', 'BIOLOGY','LITERATURE', 
                                              'BUSINESS', 'ENGINEERING'))
    industry = st.sidebar.selectbox('industry',('HEALTH', 'WEB', 'AUTO', 'FINANCE', 
                                                 'EDUCATION', 'OIL', 'SERVICE'))
       
    years_experience = st.sidebar.slider('years of experience', 0.0, 24.0, 12.0)
    
    miles_from_metropolis = st.sidebar.slider('miles from metropolis', 0.0, 99.0, 50.0 )
    
    data = {'job_type': job_type,
            'degree': degree,
            'major': major,
            'industry': industry,
            'years_experience': years_experience,
            'miles_from_metropolis': miles_from_metropolis}
    
    features = pd.DataFrame(data, index=[0])
    
    return features

df = user_input_features()


# In[45]:


encode_dict = {'job_type': {'CEO': 145.31143310519482,
                            'CFO': 135.45854674396352,
                            'CTO': 135.47998336612127,
                            'JANITOR': 70.81304462635332,
                            'JUNIOR': 95.3315568968008,
                            'MANAGER': 115.36759616691043,
                            'SENIOR': 105.48777465325772,
                            'VICE_PRESIDENT': 125.36762885774743},
                'degree': {'BACHELORS': 125.45466252599789,
                           'DOCTORAL': 135.4894334070847,
                           'HIGH_SCHOOL': 101.92065863209777,
                           'MASTERS': 130.50490271574517,
                           'NONE': 98.17646735963928},
                'major': {'BIOLOGY': 127.9326641429281,
                          'BUSINESS': 135.64897980108685,
                          'CHEMISTRY': 129.07208492569004,
                          'COMPSCI': 132.0756054948443,
                          'ENGINEERING': 138.43661683391358,
                          'LITERATURE': 124.42309658509986,
                          'MATH': 133.31973495268247,
                          'NONE': 102.58348094786373,
                          'PHYSICS': 130.37243622667353},
                'industry': {'AUTO': 109.4336903520984,
                             'EDUCATION': 99.44838571898697,
                             'FINANCE': 130.74674347470025,
                             'HEALTH': 115.7355399110364,
                             'OIL': 130.9529456262126,
                             'SERVICE': 104.44682029458984,
                             'WEB': 121.64451908439591}}



encode_cols = ['job_type', 'degree', 'major', 'industry']

for col in encode_cols:
    df[col] = df[col].map(encode_dict[col])

# Displays the user input features
st.subheader('User Input features')


st.write(df)

# Reads in saved classification model
model = pickle.load(open('salary_prediction.pkl', 'rb'))

# Apply model to make predictions
prediction = model.predict(df)

st.subheader('Predicted Salary')
st.write(prediction)

