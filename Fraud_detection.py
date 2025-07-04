import streamlit as st
import pandas as pd
import joblib
model=joblib.load('Fraud Detection.pkl')
st.title('Fraud_detection_Pred')
st.markdown("Please enter the Transaction detail")
st.divider()
transcation_type=st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER","CASH_OUT","DEPOSITE"])
amount= st.number_input('Amount',min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input('Old Balance(Sender)',min_value=0.0,value=10000.0)
newbalanceOrig=st.number_input('New Balance(Sender)',min_value=0.0,value=9000.0)
oldbalanceDest=st.number_input('Old Balance(Receiver)',min_value=0.0,value=0.0)
newbalanceDest=st.number_input('New Balance(Receiver)',min_value=0.0,value=0.0)

if st.button("Predict"):
    input_data=pd.DataFrame([{
        'type': transcation_type,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
    }])
    
    prediction= model.predict(input_data)[0]
    
    st.subheader(f"Prediction: '{int(prediction)}'")
    
    if prediction==1:
        st.error('This transaction can be fraud')
    else:
        st.success('This transaction looks like it is not a fraud')
        