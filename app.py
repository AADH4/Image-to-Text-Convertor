import streamlit as st
from PIL import Image
import pytesseract
import requests
from io import BytesIO

# Make sure tesseract is in your PATH, or specify its location
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # For Windows (adjust accordingly)

def ocr_from_image(image):
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image)
    return text

def main():
    st.title("Image to Text Converter")
    st.write("Upload an image or paste an image URL to convert it to text.")

    # Choose to upload an image or paste an image URL
    image_option = st.radio("Select Input Method", ["Upload Image", "Paste Image URL"])

    if image_option == "Upload Image":
        # User uploads an image
        uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

        if uploaded_image is not None:
            # Open the uploaded image with PIL
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Extract text using OCR
            text = ocr_from_image(image)
            st.subheader("Extracted Text")
            st.text_area("OCR Output", text, height=300)

    elif image_option == "Paste Image URL":
        # User pastes an image URL
        image_url = st.text_input("Enter Image URL")

        if image_url:
            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                st.image(img, caption="Image from URL", use_column_width=True)

                # Extract text using OCR
                text = ocr_from_image(img)
                st.subheader("Extracted Text")
                st.text_area("OCR Output", text, height=300)
            except Exception as e:
                st.error(f"Error fetching image: {e}")

if __name__ == "__main__":
    main()
