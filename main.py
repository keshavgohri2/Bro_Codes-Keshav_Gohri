import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


data = pd.read_csv('space_weather_data.csv')


X = data[['solar_wind_speed', 'proton_density', 'magnetic_field_strength']]
y = data['event_occurred']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

importances = model.feature_importances_
feature_names = X.columns
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)

print("Feature Importances:\n", importance_df)


import matplotlib.pyplot as plt
from PIL import Image

image_path = 'mag.png'  
image = Image.open(image_path)


plt.figure(figsize=(8, 8))
plt.imshow(image)
plt.axis('off')  
plt.show()

# __________________________________________
image_path = 'solar.png'  
image = Image.open(image_path)


plt.figure(figsize=(8, 8))
plt.imshow(image)
plt.axis('off')  
plt.show()

# ______________________________________________________
image_path = 'proton.png'  
image = Image.open(image_path)


plt.figure(figsize=(8, 8))
plt.imshow(image)
plt.axis('off')  
plt.show()

