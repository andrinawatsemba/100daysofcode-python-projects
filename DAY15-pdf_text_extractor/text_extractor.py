import PyPDF2

def extract_text_pypdf2(file_name):
    with open(file_name, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

if __name__ == "__main__":
    file_name = input("Enter PDF file name (place it in the same folder as this script): ")
    text = extract_text_pypdf2(file_name)
    print("\n--- Extracted Text ---\n")
    print(text)
