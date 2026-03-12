import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------
# Load Model
# -------------------------
with open("car_price_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
features = model_data["features"]

# -------------------------
# UI
# -------------------------
st.set_page_config(page_title="Car Price Predictor", layout="centered")

st.title("🚗 Car Price Prediction")
st.write("Enter the car details below to estimate its price.")

# -------------------------
# Inputs
# -------------------------

year = st.number_input("Year of Manufacture", 1995, 2025, 2018)

kilometer = st.number_input("Kilometers Driven", 0, 500000, 50000)

engine = st.number_input("Engine Capacity (CC)", 600, 5000, 1200)

power = st.number_input("Max Power", 30, 500, 100)

seats = st.number_input("Seating Capacity", 2, 10, 5)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "LPG"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner",
    ["First", "Second", "Third", "Fourth & Above"]
)

seller = st.selectbox(
    "Seller Type",
    ["Individual", "Dealer"]
)

# -------------------------
# Feature Engineering
# -------------------------

current_year = 2025
car_age = current_year - year

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Price"):

    # Create empty dataframe with training columns
    input_df = pd.DataFrame(columns=features)
    input_df.loc[0] = 0

    # Numeric features
    if "Kilometer" in features:
        input_df.at[0, "Kilometer"] = kilometer

    if "Engine" in features:
        input_df.at[0, "Engine"] = engine

    if "Max Power" in features:
        input_df.at[0, "Max Power"] = power

    if "Seating Capacity" in features:
        input_df.at[0, "Seating Capacity"] = seats

    if "Car Age" in features:
        input_df.at[0, "Car Age"] = car_age

    # Categorical encoding
    fuel_col = f"Fuel Type_{fuel}"
    if fuel_col in features:
        input_df.at[0, fuel_col] = 1

    transmission_col = f"Transmission_{transmission}"
    if transmission_col in features:
        input_df.at[0, transmission_col] = 1

    owner_col = f"Owner_{owner}"
    if owner_col in features:
        input_df.at[0, owner_col] = 1

    seller_col = f"Seller Type_{seller}"
    if seller_col in features:
        input_df.at[0, seller_col] = 1

    # Prediction
    prediction_log = model.predict(input_df)

    prediction = np.expm1(prediction_log)

    st.success(f"💰 Estimated Car Price: ₹ {int(prediction[0]):,}")
