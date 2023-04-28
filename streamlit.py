import streamlit as st
import pickle

import pandas as pd

with open("model.pkl",'rb') as file:
    best_model=pickle.load(file)
    

df=pd.read_csv("cleaned_data.csv")

st.title("Estimation du prix d'une voiture en fonction de paramètres choisi")

# definition des catégories d'entrées
symboling_options = sorted(df['symboling'].unique())
cylindernumber_options = sorted(df['cylindernumber'].unique())
fueltype_options = sorted(df['fueltype'].unique())
aspiration_options = sorted(df['aspiration'].unique())
doornumber_options = sorted(df['doornumber'].unique())
carbody_options = sorted(df['carbody'].unique())
drivewheel_options = sorted(df['drivewheel'].unique())
enginelocation_options = sorted(df['enginelocation'].unique())
enginetype_options = sorted(df['enginetype'].unique())
fuelsystem_options = sorted(df['fuelsystem'].unique())
marque_options = sorted(df['marque'].unique())

df['modele'] = df['modele'].fillna("")
modele_options = sorted(df['modele'].unique())

# traitement des entrees de l'utilisateur
symboling = st.selectbox("Symboling", symboling_options)
cylindernumber = st.selectbox("Cylindernumber", cylindernumber_options)
fueltype = st.selectbox("Fueltype", fueltype_options)
aspiration = st.selectbox("Aspiration", aspiration_options)
doornumber = st.selectbox("Doornumber", doornumber_options)
carbody = st.selectbox("Carbody", carbody_options)
drivewheel = st.selectbox("Drivewheel", drivewheel_options)
enginelocation = st.selectbox("Enginelocation", enginelocation_options)
enginetype = st.selectbox("Enginetype", enginetype_options)
fuelsystem = st.selectbox("Fuelsystem", fuelsystem_options)
marque = st.selectbox("Marque", marque_options)
modele = st.selectbox("Modele", modele_options)

wheelbase = st.number_input("Wheelbase", value=0.0)
carlength = st.number_input("Carlength", value=0.0)
carwidth = st.number_input("Carwidth", value=0.0)
carheight = st.number_input("Carheight", value=0.0)
curbweight = st.number_input("Curbweight", value=0.0)
enginesize = st.number_input("Enginesize", value=0.0)
boreratio = st.number_input("Boreratio", value=0.0)
stroke = st.number_input("Stroke", value=0.0)
compressionratio = st.number_input("Compressionratio", value=0.0)
horsepower = st.number_input("Horsepower", value=0.0)
peakrpm = st.number_input("Peakrpm", value=0.0)
citympg = st.number_input("Citympg", value=0.0)
highwaympg = st.number_input("Highwaympg", value=0.0)

#
user_input = {'symboling': symboling, 
              'cylindernumber': cylindernumber,
              'fueltype': fueltype,
              'aspiration': aspiration,
              'doornumber': doornumber,
              'carbody': carbody,
              'drivewheel': drivewheel,
              'enginelocation': enginelocation,
              'enginetype': enginetype,
              'fuelsystem': fuelsystem,
              'marque': marque,
              'modele': modele,
              'wheelbase': wheelbase,
              'carlength': carlength,
              'carwidth': carwidth,
              'carheight': carheight,
              'curbweight': curbweight,
              'enginesize': enginesize,
              'boreratio': boreratio,
              'stroke': stroke,
              'compressionratio': compressionratio,
              'horsepower': horsepower,
              'peakrpm': peakrpm,
              'citympg': citympg,
              'highwaympg': highwaympg}


user_df = pd.DataFrame([user_input])

predicted_price = best_model.predict(user_df)

st.write(f"Predicted price: {predicted_price[0]:,.2f}")
