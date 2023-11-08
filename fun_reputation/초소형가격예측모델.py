import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Sample data, replace with your actual data
data = {
    'Artist': ['Fernando Laposse', 'Alice Adams', 'Valerio Adami', 'Adam Broomberg and Oliver Chanarin Studio'],
    'Artwork Genre': ['Abstract', 'Modern', 'Contemporary', 'Conceptual'],
    'Artwork Size': ['Medium', 'Small', 'Large', 'Large'],
    'Artwork Material': ['Bronze', 'Canvas', 'Paper', 'Mixed Media'],
    'Artwork Condition': ['Good', 'Excellent', 'Fair', 'Poor'],
    'Price': [10000, 600, 10000, 62]
}

df = pd.DataFrame(data)

# Define the feature columns and target column
feature_cols = ['Artist', 'Artwork Genre', 'Artwork Size', 'Artwork Material', 'Artwork Condition']
target_col = 'Price'

# Preprocessing for categorical data
categorical_cols = [cname for cname in feature_cols if df[cname].dtype == "object"]
numerical_cols = [cname for cname in feature_cols if df[cname].dtype in ['int64', 'float64']]

# Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='constant')

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Create the regression model
model = LinearRegression()

# Bundle preprocessing and modeling code in a pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', model)
                          ])

# Separate target from predictors
X = df.drop(target_col, axis=1)
y = df[target_col]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Preprocessing of training data, fit model 
pipeline.fit(X_train, y_train)

# Preprocessing of validation data, get predictions
preds = pipeline.predict(X_test)

# Evaluate the model
score = mean_squared_error(y_test, preds, squared=False)  # RMSE
print('RMSE:', score)

# Model is ready to make predictions on new data
# new_data = pd.DataFrame([new_data_point])
# predictions = pipeline.predict(new_data)
