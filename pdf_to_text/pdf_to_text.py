from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string
import os
import sys

args = sys.argv
file_name = args[1]
pdf_data_path = "./pdf_data/" + file_name + ".pdf"
text_data_path = "./text_data/" + file_name + ".txt"

def clean_text(text):
    text = text.replace("\n", " ")
    text = text.replace("\x0c", " ")
    return text

def extract_text_from_pdf(pdf_path):
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path, dpi=300)  # Adjust DPI if needed
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        return None

    text = ""
    for image in images:
        try:
            # Convert image to RGB
            pil_image = image.convert('RGB')
            # Process the image and generate pixel values
            addText = image_to_string(pil_image)
            addText = clean_text(addText)
            text += addText
        except Exception as e:
            print(f"Error processing image: {e}")
    return text


pdf_text = ''
os.makedirs("text_data", exist_ok=True)
if not os.path.exists(f"text_data/{file_name}.txt"):
    with open(f"text_data/{file_name}.txt", "w") as f:
        pdf_text = extract_text_from_pdf(pdf_data_path)
        f.write(pdf_text)