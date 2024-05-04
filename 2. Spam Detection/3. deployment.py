#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import streamlit as st
import pickle

st.title('Spam Detection')
st.sidebar.header('User Input Parameters')

# Create a text input field in the sidebar
user_input = st.sidebar.text_input("Enter text:")

st.subheader('User Input Parameters')
# Display the entered text
st.write(f'Text: {user_input}')

# Load the trained model
with open('trained_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
#prediction
prediction = model.predict([user_input])
if prediction == 1:
    result = 'Spam'
else:
    result = 'Ham'

#output
st.subheader('Prediction Result')
st.write(result)


# In[ ]:




