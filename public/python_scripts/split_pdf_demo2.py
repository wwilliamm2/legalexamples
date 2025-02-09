'''~/lx/lx14/public/py/split_pdf_demo2.py'''

'''
Splits pdfs into folders of pages. I get both pdf pages and png pages.

Demo:

conda activate gemini1
python split_pdf_demo2.py

'''

# Use bash to make a folder for each pdf:
# cd ~/ssd2/tmp/scscourt/pdfs/
# ls -1 202*.pdf | sed 's/^/mkdir /' | sed 's/.pdf$//' > /tmp/mkdirem.bash
# bash /tmp/mkdirem.bash

'gpt, Please write a Python demo to get file name from a path'

import PyPDF2, glob, os

fn_s_l = sorted(glob.glob('/media/dan/ssd2/tmp/scscourt/pdfs/202*pdf'))[:33]
magick_s = '/home/dan/anaconda3/envs/imagemagick/bin/magick'

for fn_s in fn_s_l:
    fn_ospbn_s = os.path.basename(fn_s).replace('.pdf','')
    with open(fn_s, 'rb') as file:
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(pdf_reader.pages):
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(page)
                folder_n_s = fn_s.replace('.pdf','/')
                pg_n_s = f"{folder_n_s}{fn_ospbn_s}_page{i+1:02d}.pdf"
                png_n_s = pg_n_s.replace('.pdf', '.png')
                with open(pg_n_s, 'wb') as page_f:
                    pdf_writer.write(page_f)
                    os.system(f'{magick_s} {pg_n_s} {png_n_s}')
                    print(png_n_s)
        except Exception as myex:
            print(f'I see a problematicfile: {fn_s}')
            print(f'Due to: {str(myex)}')
