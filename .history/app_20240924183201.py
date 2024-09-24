import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load the model
model = load_model('artifacts/training/final_model.h5')  # Ensure you saved it as an .h5 file

# Define class labels
class_labels = ['Potato___Early_Blight', 'Potato___Healthy', 'Potato___Late_Blight']

# Create Streamlit app
st.title("Potato Disease Detection")
st.write("Upload an image of a potato leaf to detect disease.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    img = image.resize((224, 224))
    img_array = np.array(img, dtype=np.float32)  # Convert PIL image to numpy array as float
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize pixel values

    # Add a predict button
    if st.button("Predict"):
        # Make prediction
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)
        confidence = prediction[0][predicted_class]

        # Display the prediction
        st.write(f"**Prediction:** {class_labels[predicted_class]}")
        st.write(f"**Confidence:** {confidence:.2f}")
