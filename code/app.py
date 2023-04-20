def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['Install',package])
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import os
import matplotlib.pyplot as plt
install_and_import('pyodbc') 
#------------------#
#path = os.getcwd()
#path = /app/catref
os.chdir(src)
#---------------------------------#
im = Image.open('catalytic-reformer.jpg')
with st.sidebar:
    st.header('Catalytic Reformer')
    st.image(im,width=300)
    start = st.date_input('Start Date')
    end = st.date_input('End Date')
    st.text_input('Enter the days')

cnxn = pyodbc.connect('DRIVER={SQl Server};SERVER=192.168.1.103;Database=demo-db;Port=1433;UID=sa;PWD=server@123')
cursor = cnxn.cursor()

cursor.execute("SELECT _VALUE FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.FEED FLOW VOLUME'")
feed_flow = cursor.fetchall()
#----------------#
cursor.execute("SELECT _VALUE FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.H2HC RATIO MOI/MOI'")
h2hc_ratio = cursor.fetchall()
#-------------------------------#
cursor.execute("SELECT _VALUE FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.PRODUCT-SEPARATOR-TEMP'")
product_sep_temp = cursor.fetchall()
#-----------------------------------#
cursor.execute("SELECT _VALUE FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.R1-INLET-TEMP'")
r1_inlet_temp = cursor.fetchall()
#---------------------------#
cursor.execute("SELECT _VALUE FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.R2-INLET-TEMP'")
r2_inlet_temp = cursor.fetchall()
#----------------#
cursor.execute("SELECT _VALUE FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.R3-INLET-TEMP'")
r3_inlet_temp = cursor.fetchall()
#---Time-----------------#
cursor.execute("SELECT _TIMESTAMP FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.FEED FLOW VOLUME'")
feed_timestamp = cursor.fetchall()

cursor.execute("SELECT _TIMESTAMP FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.H2HC RATIO MOI/MOI'")
ratio_timestamp = cursor.fetchall()

cursor.execute("SELECT _TIMESTAMP FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.PRODUCT-SEPARATOR-TEMP'")
product_timestamp = cursor.fetchall()

cursor.execute("SELECT _TIMESTAMP FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.R1-INLET-TEMP'")
r1_timestamp = cursor.fetchall()

cursor.execute("SELECT _TIMESTAMP FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.R2-INLET-TEMP'")
r2_timestamp = cursor.fetchall()

cursor.execute("SELECT _TIMESTAMP FROM [Equipment-1-TABLE-6] where _NAME = 'demo.equipment-1.R3-INLET-TEMP'")
r3_timestamp = cursor.fetchall()

feed_flow = [int(x[0]) for x in feed_flow]
h2hc_ratio = [int(x[0]) for x in h2hc_ratio]
product_sep_temp = [int(x[0]) for x in product_sep_temp]
r1_inlet_temp = [int(x[0]) for x in r1_inlet_temp]
r2_inlet_temp = [int(x[0]) for x in r2_inlet_temp]
r3_inlet_temp = [int(x[0]) for x in r3_inlet_temp]
#timestamp
feed_timestamp = pd.to_datetime([x[0] for x in feed_timestamp])
ratio_timestamp = pd.to_datetime([x[0] for x in ratio_timestamp])
product_timestamp = pd.to_datetime([x[0] for x in product_timestamp])
r1_timestamp = pd.to_datetime([x[0] for x in r1_timestamp])
r2_timestamp = pd.to_datetime([x[0] for x in r2_timestamp])
r3_timestamp = pd.to_datetime([x[0] for x in r3_timestamp])

data = {'DateTime':feed_timestamp,'Feed Volume Flow':feed_flow}
df1 = pd.DataFrame(data)

data2 = {'DateTime':ratio_timestamp,'H2HC Ratio':h2hc_ratio}
df2 = pd.DataFrame(data2)

data3 = {'DateTime':product_timestamp,'Product Separator Temp':product_sep_temp}
df3 = pd.DataFrame(data3)

data4 = {'DateTime':r1_timestamp,'R1 Inlet Temp':r1_inlet_temp}
df4 = pd.DataFrame(data4)

data5 = {'DateTime':r2_timestamp,'R2 Inlet Temp':r2_inlet_temp}
df5 = pd.DataFrame(data5)

data6 = {'DateTime':r3_timestamp,'R3 Inlet Temp':r3_inlet_temp}
df6 = pd.DataFrame(data6)

df = pd.merge(df1,df2,on='DateTime',how='inner').merge(df3,on='DateTime',how='inner').merge(df4,on='DateTime',how='inner').merge(df5,on='DateTime',how='inner').merge(df6,on='DateTime',how='inner')

st.dataframe(df)
