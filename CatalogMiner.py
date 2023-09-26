import os
import PyPDF2
import re


def extract_pdf_texts(folder_path):
    texts = {}

    #get all PDF files in the specified folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    for file in files:
        texts[file] = []
        file_path = os.path.join(folder_path, file)

        try:
            with open(file_path, "rb") as infile:
                pdf_reader = PyPDF2.PdfReader(infile)
                for page in pdf_reader.pages:
                    texts[file].append(page.extract_text())
        except Exception as e:
            print(f"Could not read {file} due to: {str(e)}")
    return texts


#pattern regex pattern to read through course codes (2 to 3 numbers, dash, then three letters)
pattern = re.compile(r'\b[A-Za-z]{2,3}-\d{3}\b')


def extract_courses_from_text(text):
    return pattern.findall(text)






