# Gender Prediction Using Machine Learning

This project aims to predict the gender of a person based on various personal attributes using a machine learning model. The project includes a web interface for inputting data, a machine learning model for prediction, and a set of test cases to validate the model.

## Table of Contents

- [Gender Prediction Using Machine Learning](#gender-prediction-using-machine-learning)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Request Format](#api-request-format)
  - [Testing \& Making POST Requests](#testing--making-post-requests)

## Project Overview

The project uses a RandomForestClassifier to predict gender based on the following attributes:
- Age
- Height (cm)
- Weight (kg)
- Occupation
- Education Level
- Marital Status
- Favorite Color

The project includes:
- A Flask web application (`server.py`) for data input and prediction.
- An HTML form (`index.html`) for user inputs.
- A script (`request.py`) to test the model with various input cases.
- A pre-trained machine learning model saved as `model.pkl`.

## Installation

To run this project, you need to have Python installed on your machine. Follow the steps below to set up the project:

1. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask Server:**

    Start the Flask server to serve the web application:

    ```bash
    python server.py
    ```

2. **Open the Web Application:**

    Open your web browser and navigate to `http://127.0.0.1:5000/` to access the gender prediction form.

3. **Input Data and Get Predictions:**

    Fill out the form with the required attributes and submit to get the gender prediction.

## API Request Format

When making POST requests to the `/predict` endpoint of the Flask server, the request body should be a JSON object with the following structure:

```json
{
  "Age": "30",
  "Height (cm)": "175",
  "Weight (kg)": "70",
  "Occupation": "Software Engineer",
  "Education Level": "Bachelor's Degree",
  "Marital Status": "Single",
  "Favorite Color": "Blue"
}

```
## Testing & Making POST Requests

It is recommended to send a request to the server through the webpage. However, you can also send a POST request to the server by modifying the json request body in `request.py`
`request.py` contains some test cases for unit testing, which you can customize and modify.

To test the model with predefined test cases, run the `request.py` script:

```bash
python request.py
```