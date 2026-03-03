#pip install pymupdf

#import fitz #PyMuPDF
from pprint import pprint
import pymupdf

SOURCE_FILE = r"G:/C++.pdf"
PAGES_PER_FILE = 10

def main():
    split_pdf(SOURCE_FILE, PAGES_PER_FILE)

def split_pdf(input_file, pages_per_file):

    source_file = pymupdf.open(input_file) # or pymupdf.Document(filename)

    for i in range(0, len(source_file), pages_per_file):
        output_file = pymupdf.open()

        for j in range(i, min (i + pages_per_file, len(source_file))):
            output_file.insert_pdf(source_file, from_page= j, to_page= j)

        part = (i // pages_per_file) + 1
        output_file.save(f"G:/C++/part_{part}.pdf")
        output_file.close()

        pprint(f"Chapter {part} created")

    source_file.close()

if __name__ == "__main__":
    main()