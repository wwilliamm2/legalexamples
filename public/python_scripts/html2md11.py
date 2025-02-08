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
print(markdown_s)

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

'done'
    
