import streamlit as st
from Prediction import predict_price

st.title("🚗 Used Car Price Prediction")

st.write("Enter car details below")

kilometer = st.number_input("Kilometers Driven", 0)
engine = st.number_input("Engine Capacity (cc)", 500)
max_power = st.number_input("Max Power (bhp)", 20)
max_torque = st.number_input("Max Torque (Nm)", 50)

length = st.number_input("Length (mm)", 3000)
width = st.number_input("Width (mm)", 1400)
height = st.number_input("Height (mm)", 1200)

seating_capacity = st.selectbox("Seating Capacity",[2,4,5,6,7])
fuel_tank = st.number_input("Fuel Tank Capacity",20)

car_age = st.slider("Car Age",0,20,5)

transmission = st.selectbox("Transmission",["Manual","Automatic"])
owner = st.selectbox("Owner",["First","Second","Third","Fourth+"])

make = st.selectbox("Brand",[
"Maruti Suzuki","Hyundai","Honda","Toyota",
"Mahindra","Tata","BMW","Mercedes-Benz","Audi"
])

fuel_type = st.selectbox("Fuel Type",[
"Petrol","Diesel","CNG","Electric","Hybrid"
])

seller_type = st.selectbox("Seller Type",[
"Individual","Dealer"
])

drivetrain = st.selectbox("Drivetrain",[
"FWD","RWD","AWD"
])

# Convert UI inputs to model format
if transmission == "Manual":
    transmission = 0
else:
    transmission = 1

owner_map = {"First":0,"Second":1,"Third":2,"Fourth+":3}
owner = owner_map[owner]

if st.button("Predict Price"):

    user_input = {
        "Kilometer":kilometer,
        "Engine":engine,
        "Max Power":max_power,
        "Max Torque":max_torque,
        "Length":length,
        "Width":width,
        "Height":height,
        "Seating Capacity":seating_capacity,
        "Fuel Tank Capacity":fuel_tank,
        "Car_Age":car_age,
        "Transmission":transmission,
        "Owner":owner,
        "Make":make,
        "Fuel Type":fuel_type,
        "Seller Type":seller_type,
        "Drivetrain":drivetrain
    }

    price = predict_price(user_input)

    st.success(f"Estimated Price: ₹ {price:,.2f}")