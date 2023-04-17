import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
#------------------#
current_path = os.getcwd()
code_path = r'\code'
model_path = r'\model'
model_filename = r'\model.sav'
src_path = r'\src'
image_file = r'\catalytic-reformer.jpg'
#---------------------------------#
rf = joblib.load(os.path.join(current_path,model_path,model_filename))
im = Image.open(os.path.join(current_path,src_path,image_file))
with st.sidebar:
    st.markdown('Catalytic Reformer')
    st.image(im,width=300)
    start = st.date_input('Start Date')
    end = st.date_input('End Date')
