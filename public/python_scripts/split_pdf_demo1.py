'''~/lx/lx14/public/py/split_pdf_demo1.py'''

'''
gpt, please write a simple demo of using pypdf2 to cut big.pdf into pdf01.pdf, pdf02.pdf, pdf03.pdf
..............
Answer:

import PyPDF2

def split_pdf(input_path, output_prefix):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for i in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[i])
            
            output_filename = f"{output_prefix}{i+1:02d}.pdf"
            with open(output_filename, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f"Created: {output_filename}")

# Usage
split_pdf('big.pdf', 'pdf')

'''

# ls -1 202*.pdf | sed 's/^/mkdir /' | sed 's/.pdf$//' > /tmp/mkdirem.bash
# bash /tmp/mkdirem.bash

import PyPDF2
with open('big.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    # for i in range(len(pdf_reader.pages))[:3]:
    for i, page in enumerate(pdf_reader.pages):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page)
        with open(f"/tmp/page{i+1:02d}.pdf", 'wb') as page_f:
            pdf_writer.write(page_f)
