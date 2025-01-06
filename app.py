import streamlit as st
import tensorflow as tf
import numpy as np
from sklearn.linear_model import LogisticRegression
import os

# Load your pre-trained TensorFlow model for accessibility analysis
# Replace 'model.h5' with the actual path to your model
MODEL_PATH = 'model.h5'

try:
    if os.path.exists(MODEL_PATH):
        model = tf.keras.models.load_model(MODEL_PATH)
        st.success("Model loaded successfully!")
    else:
        model = None
        st.error("Model file not found. Please upload the correct 'model.h5' file.")
except Exception as e:
    model = None
    st.error(f"Error loading model: {e}")

# Dummy data for statistical analysis (replace with real data)
# Here, we assume 'accessibility_data' contains relevant features for analysis
accessibility_data = np.random.rand(100, 5)
# Replace 'accessibility_labels' with corresponding labels (binary classification: accessible or not)
accessibility_labels = np.random.randint(2, size=(100,))

# Train a simple logistic regression model for statistical analysis
statistical_model = LogisticRegression()
statistical_model.fit(accessibility_data, accessibility_labels)

# Streamlit app
st.title("Accessibility Analysis Tool")

# Input form for user data
st.header("Enter the Features for Analysis")
feature1 = st.number_input("Feature 1", value=0.0, format="%.2f")
feature2 = st.number_input("Feature 2", value=0.0, format="%.2f")
feature3 = st.number_input("Feature 3", value=0.0, format="%.2f")
feature4 = st.number_input("Feature 4", value=0.0, format="%.2f")
feature5 = st.number_input("Feature 5", value=0.0, format="%.2f")

# Analyze button
if st.button("Analyze"):
    user_input = [feature1, feature2, feature3, feature4, feature5]

    if model is not None:
        # Use TensorFlow model for accessibility prediction
        try:
            accessibility_prediction = model.predict(np.array([user_input]))
            st.write(f"Accessibility Prediction (TensorFlow Model): {accessibility_prediction[0][0]:.4f}")
        except Exception as e:
            st.error(f"Error making prediction with TensorFlow model: {e}")
    else:
        st.warning("TensorFlow model is not loaded. Skipping prediction.")

    # Use statistical model for additional insights
    try:
        statistical_prediction = statistical_model.predict(np.array([user_input]))
        st.write(f"Statistical Prediction (Logistic Regression): {statistical_prediction[0]}")
    except Exception as e:
        st.error(f"Error making prediction with statistical model: {e}")
