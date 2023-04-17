import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import pickle
#------------------#
path = r'..\src'
model_path = r'..\model'
model_filename = r'\model.pkl'
#---------------------------------#
with open(model_path+model_filename,'rb') as file:
    rf = pickle.load(file)
im = Image.open(path+'\catalytic-reformer.jpg')
with st.sidebar:
    st.markdown('#Catalytic Reformer')
    st.image(im,width=300)
    start = st.date_input('Start Date')
    end = st.date_input('End Date')
