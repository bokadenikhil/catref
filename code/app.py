import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
#------------------#
model_filename = 'model.sav'
image_file = 'catalytic-reformer.jpg'
#---------------------------------#
os.chdir('model')
rf = joblib.load(model_filename)
os.chdir('..')
os.chdir('src')
im = Image.open(image_file)
os.chdir('..')
with st.sidebar:
    st.markdown('Catalytic Reformer')
    st.image(im,width=300)
    start = st.date_input('Start Date')
    end = st.date_input('End Date')
