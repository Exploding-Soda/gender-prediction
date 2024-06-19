from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model and feature names
model_path = './model/model.pkl'
with open(model_path, 'rb') as model_file:
    model, feature_names = pickle.load(model_file)

# Expected fields in the request
EXPECTED_FIELDS = {'Age', 'Height (cm)', 'Weight (kg)', 'Occupation', 'Education Level', 'Marital Status', 'Favorite Color'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()

    # Validate the input data
    if set(data.keys()) != EXPECTED_FIELDS:
        return jsonify({"error": "Invalid input format. Expected fields: Age, Height (cm), Weight (kg), Occupation, Education Level, Marital Status, Favorite Color."}), 400

    # Check if any field is empty
    for key in EXPECTED_FIELDS:
        if data[key].strip() == '':
            return jsonify({"error": f"Field '{key}' cannot be empty."}), 400

    input_data = pd.DataFrame([data])

    # Preprocess the input data
    input_data.columns = input_data.columns.str.strip()
    input_data_encoded = pd.get_dummies(input_data, columns=['Occupation', 'Education Level', 'Marital Status', 'Favorite Color'])

    # Align input data with training data columns
    for col in feature_names:
        if col not in input_data_encoded.columns:
            input_data_encoded[col] = 0
    input_data_encoded = input_data_encoded[feature_names]

    # Make predictions
    prediction = model.predict(input_data_encoded)

    # Return the result
    result = 'Female' if prediction[0] == 1 else 'Male'
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
