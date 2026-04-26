# Import necessary libraries
import numpy as np
import joblib  # For loading the serialized model
import pandas as pd  # For data manipulation
from flask import Flask, request, jsonify  # For creating the Flask API
from flask.json.provider import DefaultJSONProvider

class NumpyJSONProvider(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, (np.float32, np.float64)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

# Initialize the Flask application
product_sales_predictor_api = Flask("SuperKart Product Sales Predictor")
product_sales_predictor_api.json = NumpyJSONProvider(product_sales_predictor_api)

# Load the trained machine learning model
model = joblib.load("product_sales_prediction_model_v1_0.joblib")

# Define a route for the home page (GET request)
@product_sales_predictor_api.get('/')
def home():
    """
    This function handles GET requests to the root URL ('/') of the API.
    It returns a simple welcome message.
    """
    return "Welcome to the SuperKart Sales Prediction API!"

# Define a route for the home page (GET request)
@product_sales_predictor_api.get('/v1/test')
def test():
    """
    This function handles GET requests to the test URL ('/v1/test') of the API.
    It returns a simple welcome message.
    """
    return "Testing testing 1 2 3"

# Define an endpoint for single property prediction (POST request)
@product_sales_predictor_api.post('/v1/sales')
def predict_product_sales():
    # print("predict_product_sales called...")
    """
    This function handles POST requests to the '/v1/sales' endpoint.
    It expects a JSON payload containing property details and returns
    the predicted sales projection as a JSON response.
    """
    # Get the JSON data from the request body
    property_data = request.get_json()
    print("got property data from request")
    # Extract relevant features from the JSON data
    sample = {
        'Product_Weight': property_data['Product_Weight'],
        'Product_Allocated_Area': property_data['Product_Allocated_Area'],
        'Product_MRP': property_data['Product_MRP'],
        # 'Product_Store_Sales_Total': property_data['Product_Store_Sales_Total'],
        'Product_Sugar_Content': property_data['Product_Sugar_Content'],
        'Product_Type': property_data['Product_Type'],
        'Store_Id': property_data['Store_Id'],
        'Store_Establishment_Year': property_data['Store_Establishment_Year'],
        'Store_Size': property_data['Store_Size'],
        'Store_Location_City_Type': property_data['Store_Location_City_Type'],
        'Store_Type': property_data['Store_Type'],
    }

    # Convert the extracted data into a Pandas DataFrame
    input_data = pd.DataFrame([sample])

    # Predict sales
    predicted_sales = model.predict(input_data)[0]

    # Convert predicted_price to Python float
    # predicted_price = round(float(predicted_price), 2)
    # The conversion above is needed as we convert the model prediction (log price) to actual price using np.exp, which returns predictions as NumPy float32 values.
    # When we send this value directly within a JSON response, Flask's jsonify function encounters a datatype error

    # Return the actual sales
    return jsonify({'Predicted Sales (in dollars)': predicted_sales})


# Define an endpoint for batch prediction (POST request)
@product_sales_predictor_api.post('/v1/salesbatch')
def predict_product_sales_batch():
    """
    This function handles POST requests to the '/v1/salesbatch' endpoint.
    It expects a CSV file containing property details for multiple properties
    and returns the predicted sales prediction as a dictionary in the JSON response.
    """
    # Get the uploaded CSV file from the request
    file = request.files['file']

    # Read the CSV file into a Pandas DataFrame
    input_data = pd.read_csv(file)

    # Make predictions for all properties in the DataFrame 
    predicted_sales = model.predict(input_data).tolist()

    # Calculate actual prices
    # predicted_prices = [round(float(np.exp(log_price)), 2) for log_price in predicted_log_prices]

    # Create a dictionary of predictions with property IDs as keys
    product_ids = input_data['Product_Id'].tolist()  # Assuming 'Product_Id' is the property ID column
    output_dict = dict(zip(product_ids, predicted_sales))  # Use actual prices

    # Return the predictions dictionary as a JSON response
    return output_dict

# Run the Flask application in debug mode if this script is executed directly
if __name__ == '__main__':
    product_sales_predictor_api.run(debug=True)
