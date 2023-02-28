import streamlit as st
from matplotlib import image
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import os

st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)



df = pd.read_csv(DATA_PATH) #df reads data path
df['age'] = df['age'].fillna(df['age'].mean()) #imputes mean value into missing age values
df['embark_town'] = df['embark_town'].dropna()
st.dataframe(df) #displays dataframe

st.subheader("Survival according to Age and Gender")
fig = px.scatter(
    df,
    x="age",
    y="sex",
    color="survived",
    color_continuous_scale="reds",
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
