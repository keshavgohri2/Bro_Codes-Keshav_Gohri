# Bro_Codes-Keshav_Gohri
Space Weather Classification is a Python project that utilizes a Random Forest Classifier to predict space weather events. By analyzing features such as solar wind speed, proton density, and magnetic field strength, the model aims to identify whether an event occurred. 


Overview
The project includes the following components:

1. Data Loading and Preprocessing: Load a dataset and prepare it for training.
2. Model Training: Train a Random Forest Classifier on the dataset.
3. Model Evaluation: Evaluate the model's performance and display feature importances.
4. Image Visualization: Display images related to the space weather data.

Requirements
1. Python 3.x
2. pandas
3. scikit-learn
4. matplotlib
5. Pillow

Usage
Prepare Your Dataset

Make sure you have a dataset named space_weather_data.csv with the following columns:

1. solar_wind_speed
2. proton_density
3. magnetic_field_strength
4. event_occurred (label)

Review the Outputs
1. Model Performance: The script will output the accuracy and a classification report of the model.
2. Feature Importances: It will also print the importance of each feature used by the model.
3. Image Visualizations: The script will display images related to space weather (replace image paths as needed).


Script Details
1. Data Loading: The dataset is loaded using pandas.
2. Model Training: A Random Forest Classifier from scikit-learn is used.
3. Evaluation: Model accuracy and classification report are printed.
4. Feature Importance: Displays the importance of each feature.
5. Image Visualization: Uses matplotlib and Pillow to display images.

Images
1. mag.png - Replace with your image file related to magnetic field strength.
2. solar.png - Replace with your image file related to solar wind speed.
3. proton.png - Replace with your image file related to proton density.
