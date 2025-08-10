import sys
import sklearn
print("Python executable:", sys.executable)
print("scikit-learn version:", sklearn.__version__)

import streamlit as st
import pandas as pd
import joblib 

model=joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")
st.markdown("Please eneter the transaction details and uuse the predict button")
st.divider()
transaction_type=st.selectbox("Transaction Type",["Payment","Transfer","CASH_OUT","DEPOSIT"])
amount=st.number_input("Amount",min_value=0.0, value=1000.0)
oldbalanceOrg=st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)
newbalanceOrig=st.number_input("New Balance (Sender)", min_value=0.0, value=900.0)
oldbalanceDest=st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest=st.number_input("NewBalance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction=model.predict(input_data)[0]
    st.subheader(f"Predicition:'{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction is fraud")
    else:
        st.success("This transaction looks like it is not a fraud")
