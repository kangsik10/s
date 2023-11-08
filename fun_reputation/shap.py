# !pip install shap
# Importing necessary libraries
# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import shap

# Initialize a seed for reproducibility
np.random.seed(0)

# Create a basic dataset
X = np.random.rand(100, 1)  # 100 samples with a single feature
y = 5 * X.squeeze() + np.random.randn(100) * 0.5  # Linear relationship with noise

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Use SHAP to explain the model
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Plotting SHAP values for the first prediction
shap.initjs()  # Initialize JavaScript visualization in the Jupyter notebook
shap.force_plot(explainer.expected_value, shap_values.values[0], X_test[0])
