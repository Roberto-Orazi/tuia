# app.py
import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import QuantileTransformer, StandardScaler
from sklearn.cluster import KMeans
import os

seed = 42

selected_features = ['volatile_acidity', 'citric_acid', 'chlorides',
    'total_sulfur_dioxide','density', 'pH',
    'sulphates','alcohol', 'total_acidity',
    'acidity_to_pH_ratio','free_sulfur_dioxide_to_total_sulfur_dioxide_ratio',
    'alcohol_to_acidity_ratio', 'residual_sugar_to_citric_acid_ratio',
    'alcohol_to_density_ratio', 'total_alkalinity', 'total_minerals']

def feat_eng(df):
    df.columns = df.columns.str.replace(' ', '_')
    df['total_acidity'] = df['fixed_acidity'] + df['volatile_acidity'] + df['citric_acid']
    df['acidity_to_pH_ratio'] = df['total_acidity'] / df['pH']
    df['free_sulfur_dioxide_to_total_sulfur_dioxide_ratio'] = df['free_sulfur_dioxide'] / df['total_sulfur_dioxide']
    df['alcohol_to_acidity_ratio'] = df['alcohol'] / df['total_acidity']
    df['residual_sugar_to_citric_acid_ratio'] = df['residual_sugar'] / df['citric_acid']
    df['alcohol_to_density_ratio'] = df['alcohol'] / df['density']
    df['total_alkalinity'] = df['pH'] + df['alcohol']
    df['total_minerals'] = df['chlorides'] + df['sulphates'] + df['residual_sugar']

    df = df.replace([np.inf, -np.inf], 0)
    df = df.dropna()
    
    df = df[selected_features]
    
    return df
    
class CustomQuantileTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, random_state=None):
        self.random_state = random_state
        self.quantile_transformer = QuantileTransformer(output_distribution='normal', random_state=self.random_state)

    def fit(self, X_train, y=None):
        self.quantile_transformer.fit(X_train)
        return self

    def transform(self, X):
        X_transformed = self.quantile_transformer.transform(X)
        X = pd.DataFrame(X_transformed, columns=X.columns)
        return X

class CustomStandardScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.scaler = StandardScaler()

    def fit(self, X_train, y=None):
        self.scaler.fit(X_train)
        return self

    def transform(self, X):
        X_transformed = self.scaler.transform(X)
        X = pd.DataFrame(X_transformed, columns=X.columns)
        return X

class KMeansTransformer(BaseEstimator, TransformerMixin):
    
    def __init__(self, n_clusters=3, random_state=seed):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
   
    def fit(self, X_train, y=None):
        self.kmeans.fit(X_train)
        return self
    
    def transform(self, X):
        X_clustered = pd.DataFrame(X.copy())
        cluster_labels = self.kmeans.predict(X)
        X_clustered['Cluster'] = cluster_labels
        return X_clustered

# Loading the model
path_dir=os.path.dirname(os.path.abspath(__file__))
pkl_path=os.path.join(path_dir, 'wine_quality_prediction.pkl')
pipe = joblib.load(pkl_path)

input_features = [
    "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", 
    "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", 
    "pH", "sulphates", "alcohol"
]


st.title('Wine Quality Predictor Model')


def get_user_input():
    input_dict = {}

    
    with st.form(key='my_form'):
        for feat in input_features:
            input_value = st.number_input(f"Enter value for {feat}", value=0.0, step=0.01)
            input_dict[feat] = input_value

       
        submit_button = st.form_submit_button(label='Submit')

    return pd.DataFrame([input_dict]), submit_button


user_input, submit_button = get_user_input()


# When the 'Submit' button is pressed, perform the prediction
if submit_button:
    # Predict wine quality
    prediction = pipe.predict(user_input)
    prediction_value = prediction[0]

    # Display the prediction
    st.header("Predicted Quality")
    st.write(prediction_value)
    

st.markdown(
    """
    See how this model was created on Kaggle:<br>
    [🍷 Wine Quality - EDA, Prediction and Deploy](https://www.kaggle.com/code/lusfernandotorres/wine-quality-eda-prediction-and-deploy/notebook)
    """, unsafe_allow_html=True
)