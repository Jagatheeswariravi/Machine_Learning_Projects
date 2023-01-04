# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:49:00 2022

@author: jagar
"""

import streamlit as st
import pickle
import pandas as pd


final_model = pickle.load(open("model.pkl","rb"))

gender = st.number_input("enter ur gender (if male enter 0 if female enter1)")
age = st.number_input("enter your age")
Height = st.number_input("enter your height")
Weight = st.number_input("enter your weight")
Duration= st.number_input("enter how much time you have worked")
heart_rate=st.number_input("What is ur heart rate now")
Body_temp = st.number_input("what is ur body temp")


prediction = final_model.predict([[gender,age,Height,Weight,Duration,heart_rate,Body_temp]])[0]

st.header(prediction)