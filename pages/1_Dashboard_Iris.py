import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "iris.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "iris.csv")

#display starts
st.title("Dashboard - Iris Data")

img = image.imread(IMAGE_PATH) #img reads image path
st.image(img) #displays image

df = pd.read_csv(DATA_PATH) #df reads data path
st.dataframe(df) #displays dataframe

species = st.selectbox("Select the Species:", df['Species'].unique()) #selectbox displays all unique values from the Species column of df

col1, col2 = st.columns(2) #lays out following graphs side by side

fig_1 = px.histogram(df[df['Species'] == species], x = 'SepalLengthCm') #histogram of species selected from selectbox gets displayed according to the sepal length
col1.plotly_chart(fig_1, use_container_width = True) 

fig_2 = px.box(df[df['Species'] == species], y = "SepalLengthCm") #displays boxplot for species selected from selectbox based on sepal length
col2.plotly_chart(fig_2, use_container_width = True)
