import pickle
import pandas as pd

# Load model and columns once
model = pickle.load(open("car_price_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

def predict_price(user_input):
    
    # Convert input dictionary to dataframe
    input_df = pd.DataFrame([user_input])
    
    # Apply same one-hot encoding used in training
    input_df = pd.get_dummies(
        input_df,
        columns=['Make','Fuel Type','Seller Type','Drivetrain']
    )
    
    # Align with training columns
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    
    # Predict
    prediction = model.predict(input_df)
    
    return prediction[0]