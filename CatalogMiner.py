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


def analyze_courses(texts):
    distinct_course_counts = {}
    for file, text_list in texts.items():
        all_courses = []
        for text in text_list:
            all_courses.extend(extract_courses_from_text(text))

        #converting to set to get distinct courses and then back to list

        distinct_courses = list(set(all_courses))
        distinct_course_counts[file] = len(distinct_courses)
    return distinct_course_counts


def main():
    folder_path = "catalogs"
    texts = extract_pdf_texts(folder_path)
    counts = analyze_courses(texts)

    #sort pdfs by the number of distinct courses they offer
    sorted_programs = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    for program, count in sorted_programs:
        print(f"{program} offers {count} distinct courses.")

    print(
        f"\nThe program {sorted_programs[0][0]} offers the most distinct courses with {sorted_programs[0][1]} courses.")


if __name__ == "__main__":
    main()




