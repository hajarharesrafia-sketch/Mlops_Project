import streamlit as st
import joblib
import numpy as np

# charger modèle
model = joblib.load("model.pkl")

st.title("💳 Loan Default Prediction App")

st.write("Enter client information to predict default risk")

# inputs utilisateur
credit_lines = st.number_input("Credit Lines Outstanding", min_value=0, value=1)
loan_amt = st.number_input("Loan Amount Outstanding", min_value=0, value=1000)
total_debt = st.number_input("Total Debt Outstanding", min_value=0, value=500)
income = st.number_input("Income", min_value=0, value=30000)
years_employed = st.number_input("Years Employed", min_value=0, value=1)
fico_score = st.number_input("FICO Score", min_value=300, max_value=850, value=650)

# bouton prédiction
if st.button("Predict"):

    features = np.array([[ 
        credit_lines,
        loan_amt,
        total_debt,
        income,
        years_employed,
        fico_score
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ High Risk: Client likely to default")
    else:
        st.success("✅ Low Risk: Client likely to repay")