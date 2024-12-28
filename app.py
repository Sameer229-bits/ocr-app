import streamlit as st
import os
from backend import extract_text  # Import the backend function

# Streamlit app
st.title("Azure OCR App using Document Intelligence")
st.write("Upload a document (PDF/Image) to extract text using Azure.")

uploaded_file = st.file_uploader("Upload your file", type=["pdf", "jpg", "png"])

if uploaded_file:
    # Save the uploaded file temporarily
    file_path = os.path.join("temp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("File uploaded successfully! Extracting text...")

    # Call Azure OCR function
    extracted_text = extract_text(file_path)
    st.subheader("Extracted Text")
    st.text_area("Result", extracted_text, height=300)

    # Cleanup
    os.remove(file_path)