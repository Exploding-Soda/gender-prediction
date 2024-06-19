import requests
import json
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5000/predict'

# Different test cases
test_cases = [
    {
        "Age": "30",
        "Height (cm)": "175",
        "Weight (kg)": "70",
        "Occupation": "Software Engineer",
        "Education Level": "Bachelor's Degree",
        "Marital Status": "Single",
        "Favorite Color": "Blue"
    },
    {
        "Age": "25",
        "Height (cm)": "160",
        "Weight (kg)": "55",
        "Occupation": "Doctor",
        "Education Level": "Master's Degree",
        "Marital Status": "Married",
        "Favorite Color": "Green"
    },
    {
        "Age": "40",
        "Height (cm)": "180",
        "Weight (kg)": "90",
        "Occupation": "Other",
        "Education Level": "Doctorate Degree",
        "Marital Status": "Single",
        "Favorite Color": "Red"
    },
    {
        "Age": "35",
        "Height (cm)": "170",
        "Weight (kg)": "75",
        "Occupation": "Lawyer",
        "Education Level": "Associate's Degree",
        "Marital Status": "Married",
        "Favorite Color": "Yellow"
    },
    {
        "Age": "",
        "Height (cm)": "175",
        "Weight (kg)": "70",
        "Occupation": "Software Engineer",
        "Education Level": "Bachelor's Degree",
        "Marital Status": "Single",
        "Favorite Color": "Blue"
    },
    {
        "Age": "20",
        "Height (cm)": "175",
        "Weight (kg)": "70",
        "Occupation": "Software Engineer",
    },
    {
        "Age": "20",
        "Height (cm)": "175",
        "Weight (kg)": "70",
        "Occupation": "Software Engineer",
        "Education Level": "Bachelor's Degree",
        "Marital Status": "Single",
        "Favorite Color": "Blue",
        "This Should Not Be Here" : ""
    }
]

# Function to extract prediction from HTML response
def extract_prediction(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    prediction_element = soup.find('h2', class_='card-title')
    if prediction_element:
        return prediction_element.get_text().split(':')[-1].strip()
    return None

# Function to run test cases
def run_test_cases():
    for i, test_case in enumerate(test_cases):
        response = requests.post(url, data=test_case)
        if response.status_code == 200:
            if 'text/html' in response.headers['Content-Type']:
                prediction = extract_prediction(response.content)
                if prediction:
                    print(f"Test Case {i+1}: Success")
                    print(f"Input: {json.dumps(test_case, indent=4)}")
                    print(f"Output: {prediction}\n")
                else:
                    print(f"Test Case {i+1}: Failed to extract prediction")
            else:
                try:
                    result = response.json()
                    print(f"Test Case {i+1}: Success")
                    print(f"Input: {json.dumps(test_case, indent=4)}")
                    print(f"Output: {result['prediction']}\n")
                except json.JSONDecodeError:
                    print(f"Test Case {i+1}: Failed to decode JSON")
        else:
            try:
                error = response.json().get('error')
                print(f"Test Case {i+1}: Failed")
                print(f"Input: {json.dumps(test_case, indent=4)}")
                print(f"Error: {error}\n")
            except json.JSONDecodeError:
                print(f"Test Case {i+1}: Failed to decode JSON")

if __name__ == '__main__':
    run_test_cases()
