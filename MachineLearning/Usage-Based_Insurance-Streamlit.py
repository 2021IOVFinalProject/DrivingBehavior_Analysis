#Import modules
import pandas as pd
from PIL import Image
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

#Title for Streamlit App
title = st.title("Usage Based Insurance Analysis and Benefits")

#Load dataset
df = pd.read_csv('./MachineLearning/DrivingBehavior_Final_Dataset.csv')
print(df.columns)

#Description of the project
description = st.markdown("""
## What is Usage Based Insurance?
Usage-Based Insurance, referred to as pay-per-mile, pay-as-you-drive, or pay-as-you-go, is
a type of auto insurance that, depending on the specific insurer’s program, can measure how far
and how a driver drive their vehicle.

### How does Usage-Based Insurance work?
This type of insurance works by having a device installed on a vehicle (OBD II) where it collects
informations such as mileage, vehicle speed, engine rpm, etc.
""")


#Add Reference