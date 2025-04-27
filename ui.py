import streamlit as st
from PIL import Image
from main import *

# Web page
st.title("Image Converter")

# File Uploader
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "webp", "tiff"]
)

# Display uploaded image
if uploaded_file is not None:

    original_file_name = uploaded_file.name.rsplit('.', 1)[0]

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_container_width=True)

    st.write(f"Original format: {image.format}")

    format_options = ["PNG", "JPEG", "WEBP", "TIFF"]
    output_format = st.selectbox (
        "Choose output format",
        format_options
    )

    # Conversion stuff after image is shown
    if st.button("Convert"):
        converted_image = convert_image(
            uploaded_file,
            output_format.lower(),
        )
        st.write(f"Image converted to {output_format}")

        new_file_name = f"{original_file_name}.{output_format.lower()}"

        st.download_button (
            label=f"Download as {output_format}",
            data=converted_image,
            file_name=new_file_name,
            mime=f"image/{output_format.lower()}",
        )