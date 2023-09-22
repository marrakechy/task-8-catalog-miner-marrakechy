import re
import PyPDF2

import os
import PyPDF2


def extract_pdf_texts(folder_path):
    texts = {}

    # Get all PDF files in the specified folder
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


def analyze_texts(texts):

    pattern = re.compile(r'\b[A-Za-z]{2,3}-\d{3}\b')
    # and answer the specific questions based on the structure and content of the catalogs

    #count the disction of courses through the programs
    dict =  {'MUS:', 'BUS: ', 'AAS: ', 'POL: ', ''}
    pass




# Specify the path to the folder containing the PDFs
folder_path = "path/to/your/pdf/folder"

# Extract texts from all PDFs in the specified folder
texts = extract_pdf_texts(folder_path)

# Analyze the extracted texts to answer the questions
analyze_texts(texts)



