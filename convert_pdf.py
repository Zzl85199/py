import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path
from opencc import OpenCC
from fpdf import FPDF

def convert_pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, "PNG")
        image_paths.append(image_path)
    return image_paths

def extract_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path), lang='chi_sim')

def simplify_to_traditional(text):
    cc = OpenCC('s2t')  # Simplified to Traditional
    return cc.convert(text)

def create_pdf_from_text(text_list, output_pdf):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for text in text_list:
        pdf.multi_cell(0, 10, text, align='L')
        pdf.ln()
    pdf.output(output_pdf)

def process_pdf(input_pdf, output_folder, output_pdf):
    os.makedirs(output_folder, exist_ok=True)
    image_paths = convert_pdf_to_images(input_pdf, output_folder)
    
    traditional_texts = []
    for image_path in image_paths:
        extracted_text = extract_text_from_image(image_path)
        traditional_text = simplify_to_traditional(extracted_text)
        traditional_texts.append(traditional_text)
    
    create_pdf_from_text(traditional_texts, output_pdf)
    print(f"Converted PDF saved to {output_pdf}")

# Example usage
input_pdf = "04_DeepSeek.pdf"  # Input PDF file
output_folder = "./pdf_images"  # Folder to store images
output_pdf = "./converted_traditional.pdf"  # Output PDF file

process_pdf(input_pdf, output_folder, output_pdf)