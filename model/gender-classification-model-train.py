import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
csv_file_path = 'gender.csv'
gender_data = pd.read_csv(csv_file_path)

# Drop irrelevant columns
gender_data = gender_data.drop(columns=['Unnamed: 9'])

# Strip column names to remove leading and trailing spaces
gender_data.columns = gender_data.columns.str.strip()

# Convert categorical variables to numerical using one-hot encoding
gender_data_encoded = pd.get_dummies(gender_data, columns=['Gender', 'Occupation', 'Education Level', 'Marital Status', 'Favorite Color'])

# Define features and target variable
X = gender_data_encoded.drop(columns=['Gender_female', 'Gender_male'])
y = gender_data_encoded['Gender_female']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# Save the trained model and feature names as a pickle file
model_path = 'model.pkl'
with open(model_path, 'wb') as model_file:
    pickle.dump((clf, X_train.columns), model_file)
