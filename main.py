#pip install pymupdf

import fitz #PyMuPDF

SOURCE_FILE = r"G:/C++.pdf"
PAGES_PER_FILE = 50

def main():
    split_pdf()

def split_pdf():

    source_file = fitz.open(SOURCE_FILE)

    for index in range(0, len(source_file), PAGES_PER_FILE):
        output_file = fitz.open()

        for j_index in range(index, min (index + PAGES_PER_FILE, len(source_file))):
            output_file.insert_pdf(source_file, from_page= j_index, to_page= j_index)


        output_file.save(f"G:/C++/part_{index//PAGES_PER_FILE + 1}.pdf")
        output_file.close()

    source_file.close()

if __name__ == "__main__":
    main()