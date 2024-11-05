import streamlit as st
import numpy as np
import joblib

st.title('iris dataset predictions')

pipeline_entrenado = joblib.load('C:\AA1\MLOps\iris_pipeline.joblib')


# st.sidebar.header('valores de las features para predecir:')
# sepal_length = st.sidebar.number_input('Sepal length', min_value=0.0, max_value=10.0)
# sepal_width = st.sidebar.number_input('Sepal width', min_value=0.0, max_value=10.0)
# petal_length = st.sidebar.number_input('Petal length', min_value=0.0, max_value=10.0)
# petal_width = st.sidebar.number_input('Petal width', min_value=0.0, max_value=10.0)

sepal_length = st.slider('Sepal length', 4.0, 8.0, 5.0)
sepal_width = st.slider('Sepal width', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal length', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal width', 0.1, 2.5, 1.0)

data_para_predecir = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

prediccion = pipeline_entrenado.predict(data_para_predecir)

st.write('Predicciónn:', prediccion)
