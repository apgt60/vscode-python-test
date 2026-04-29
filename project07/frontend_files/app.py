import streamlit as st
import pandas as pd
import requests

# Set the title of the Streamlit app
st.title("Superkart Product Sales Prediction")

# Section for online prediction
st.subheader("Online Prediction")

# Collect user input for property features
sugar_content = st.selectbox("Product_Sugar_Content", ['Low Sugar','Regular','No Sugar','reg'])
product_type = st.selectbox("Product Type", ['Frozen Foods','Dairy','Canned','Baking Goods','Health and Hygiene',
 'Snack Foods','Meat','Household','Hard Drinks','Fruits and Vegetables',
 'Breads','Soft Drinks','Breakfast','Others','Starchy Foods','Seafood'])
store_id = st.selectbox("Store ID", ['OUT004','OUT003','OUT001','OUT002'])
store_est_year = st.selectbox("Store Establishment Year", ['2009','1999','1987','1998'])
store_size = st.selectbox("Store Size", ['Medium','High','Small'])
store_city_type = st.selectbox("Store Location City Type", ['Tier 2','Tier 1','Tier 3'])
store_type = st.selectbox("Store Type", ['Supermarket Type2','Departmental Store','Supermarket Type1','Food Mart'])
product_weight = st.number_input("Product Weight")
product_allocated_area = st.number_input("Product Allocated Area")
product_mrp = st.number_input("Product Max Retail Price")


# Convert user input into a DataFrame
input_data = pd.DataFrame([{
    'Product_Sugar_Content': sugar_content,
    'Product_Type': product_type,
    'Store_Id': store_id,
    'Store_Establishment_Year': store_est_year,
    'Store_Size': store_size,
    'Store_Location_City_Type': store_city_type,
    'Store_Type': store_type,
    'Product_Weight': product_weight,
    'Product_Allocated_Area': product_allocated_area,
    'Product_MRP': product_mrp
}])

# Make prediction when the "Predict" button is clicked
if st.button("Predict"):
    response = requests.post("https://apgt60-superkart.hf.space/v1/sales", json=input_data.to_dict(orient='records')[0])  # Send data to Flask API
    if response.status_code == 200:
        prediction = response.json()['Predicted Sales (in dollars)']
        st.success(f"Predicted Product Sales (in dollars): {prediction}")
    else:
        errormessage = "Error making prediction.  Got response code " + str(response.status_code)
        st.error(errormessage)

# Section for batch prediction
st.subheader("Batch Prediction")

# Allow users to upload a CSV file for batch prediction
uploaded_file = st.file_uploader("Upload CSV file for batch prediction", type=["csv"])

# Make batch prediction when the "Predict Batch" button is clicked
if uploaded_file is not None:
    if st.button("Predict Batch"):
        response = requests.post("https://apgt60-superkart.hf.space/v1/salesbatch", files={"file": uploaded_file})  # Send file to Flask API
        if response.status_code == 200:
            predictions = response.json()
            st.success("Batch predictions completed!")
            st.write(predictions)  # Display the predictions
        else:
            errormessage = "Error making batch prediction.  Got response code " + str(response.status_code)
            st.error(errormessage)
