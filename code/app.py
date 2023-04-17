import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import joblib
#------------------#
path = r'..\src'
model_path = r'..\model'
model_filename = r'\model.pkl'
#---------------------------------#
rf = joblib.load(r'/app/catref/model/model.sav')
im = Image.open(path+'\catalytic-reformer.jpg')
with st.sidebar:
    st.markdown('#Catalytic Reformer')
    st.image(im,width=300)
    start = st.date_input('Start Date')
    end = st.date_input('End Date')
