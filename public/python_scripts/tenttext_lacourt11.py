'''tenttext_lacourt11.py'''

'''
Extracts plain text from tentative rulings in lacourt-html files.
The text is copied to this folder:
/tmp/lacourt_text/
the text files should have a structure like this:
text/2023_09_18_ALH_3/text01.txt
text/2023_09_18_ALH_3/text02.txt
text/2023_09_18_ALH_3/text03.txt

ref:
~dan/lc17/rt20.py

Demo:
bash tenttext_lacourt10.bash
python tenttext_lacourt11.py
bash tenttext_lacourt12.bash

'''

print('Busy ...')
import bs4, datetime, glob, inspect, operator, os, re, shutil, sys, time

from bs4 import BeautifulSoup

os.makedirs('/tmp/lacourt_text/', exist_ok=True) # to store some files
'Loop through a list of html files.'
html_file_s_l = glob.glob('/tmp/lacourt_htmls/*.html')
# depends on rsync -av ~tent1/tent1/lacourt/htmls/ /tmp/lacourt_htmls/
for html_file_s in sorted(html_file_s_l):
    print(f'Processing html_file_s: {html_file_s}')
    # shutil.copy2(html_file_s, "/tmp/lacourt_text/")
    'Create a folder to store summaries for each html file.'
    folder_name_s = f"/tmp/lacourt_text/{os.path.basename(html_file_s).replace('.html','')}"
    os.makedirs(folder_name_s, exist_ok=True)
    'Extract html syntax into giant string'
    with open(html_file_s, 'r') as hf:
        html_s = hf.read()
    'Create a text boundary near all hr-elements'
    html_cb_s = html_s.replace('<hr', 'CASE_BOUNDARY<hr')
    with open(f'{folder_name_s}/html_cb.html', 'w') as cbf:
        cbf.write(html_cb_s)
    'Extract text from the boundary-enhanced html file.'
    with open(f'{folder_name_s}/html_cb.html', 'r') as cbf:
        soup = BeautifulSoup(cbf, 'html.parser')
    large_s = soup.text
    'Write the text to file so I can study it.'
    '''with open(f'{folder_name_s}/soup.txt', 'w') as tf:
        tf.write(large_s)
        if I want to see it during debugging'''
    'Try to create a separate txt file for each tent_ruling.'
    tent_ruling_s_l = large_s.split('CASE_BOUNDARY')
    for r_i, tent_ruling_s in enumerate(tent_ruling_s_l):
        with open(f'{folder_name_s}/tent_ruling_{r_i:02}.txt', 'w') as cf:
            cf.write(tent_ruling_s)
