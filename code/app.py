import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
#------------------#
current_path = os.getcwd()
st.write(os.listdir())
#path = r'/app/catref/src'
#model_path = r'/app/catref/model'
#model_filename = r'/model.sav'
#---------------------------------#
#try:
 #   rf = joblib.load(model_path+model_filename)
#except:
 #   st.write(os.getcwd())
#im = Image.open(path+'\catalytic-reformer.jpg')
with st.sidebar:
    st.markdown('Catalytic Reformer')
   # st.image(im,width=300)
    start = st.date_input('Start Date')
    end = st.date_input('End Date')
