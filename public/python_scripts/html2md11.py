'''~/lx/lx14/public/py/html2md11.py'''

'''
Converts ugly.html to better.html to better_md.txt
Demo:
. ~/lx/lx14/public/lx14b_env.bash
[ or conda activate lx14b ]
pip install html-to-markdown
python -i html2md11.py
'''

from html_to_markdown import convert_to_markdown

html_s = '<h1>Hello, world!</h1><p>This is a <strong>sample</strong>.</p>'
markdown_s = convert_to_markdown(html_s)
# print(markdown_s)

'I hope that worked'

'Now, work on Converting ugly.html to better.html'
print('Busy ...')
import bs4, datetime, glob, inspect, operator, os, re, shutil, sys, time

from bs4 import BeautifulSoup, Comment

# Define some regular expression patterns to help me remove some empty elements.
div1_re_pattern = r'<div>\s*</div>'
div2_re_pattern = r'<div>\s*</div>\n'
span_re_pattern = r'<span>\s*</span>'

fn_s = 'ugly.html'
with open(fn_s, 'r', encoding='utf-8') as cbf:
    soup = BeautifulSoup(cbf, 'html.parser')
# Find and remove all unneeded elements
tag_l = ['a', 'script', 'style', 'input', 'fieldset', 'link']
for elmnt in soup(tag_l):
    elmnt.decompose() # They should have called it delete() or rm() or destroy()
# Find and remove all comment nodes
comments = soup.find_all(string=lambda string: isinstance(string, Comment))
for comment in comments:
    comment.extract() # They should have called it delete() or rm() or destroy()
# Remove all attributes
for tag in soup.find_all(True):
    tag.attrs = {}
fn_enh_s = 'better.html'  
# Write the modified HTML to a new file
with open(fn_enh_s, 'w', encoding='utf-8') as enf:
    # Replace re pattern matches with an empty string
    nodiv1_html_s = re.sub(div1_re_pattern, '', str(soup))
    nodiv2_html_s = re.sub(div2_re_pattern, '', nodiv1_html_s, flags=re.MULTILINE)
    nospan_html_s = re.sub(span_re_pattern, '', nodiv2_html_s)
    enh_html_s = re.sub(r'^\s*$\n', '', nospan_html_s, flags=re.MULTILINE)
    enf.write(enh_html_s)
print(f'Enhanced HTML should now be inside file: {fn_enh_s}')
'Convert Enhanced HTML string to Markdown syntax string.'
better_md_s = convert_to_markdown(enh_html_s)
'Write Markdown syntax to a file.'
with open('better_md.txt', 'w', encoding='utf-8') as enf:
    enf.write(better_md_s)
'done'
