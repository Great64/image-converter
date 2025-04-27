from PIL import Image
import io

def convert_image(image_file, format):
    with Image.open(image_file) as img:

        # Create in-memory storage
        output_image = io.BytesIO()

        # Save the image to in-memory storage
        img.save(output_image, format=format.upper())

        # Reset pointer
        output_image.seek(0)

        return output_image