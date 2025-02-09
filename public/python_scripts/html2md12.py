'''~/lx/lx14/public/py/html2md12.py'''

'''
Converts ugly html files to better html files to markdown files.
Demo:
. ~/lx/lx14/public/lx14b_env.bash
[ or conda activate lx14b ]
pip install html-to-markdown
python -i html2md12.py
'''

from html_to_markdown import convert_to_markdown

html_s = '<h1>Hello, world!</h1><p>This is a <strong>sample</strong>.</p>'
markdown_s = convert_to_markdown(html_s)
# print(markdown_s)

'I hope that worked'

'Now, work on Converting ugly html files to better html files'
print('Busy ...')
import bs4, datetime, glob, inspect, operator, os, re, shutil, sys, time
from bs4 import BeautifulSoup, Comment

fn_s_l = sorted(glob.glob('/media/dan/ssd2/tmp/htmls/202*.html'))[:444]

# Define some regular expression patterns to help me remove some empty elements.
div1_re_pattern = r'<div>\s*</div>'
div2_re_pattern = r'<div>\s*</div>\n'
span_re_pattern = r'<span>\s*</span>'

for fn_s in fn_s_l:
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
    fn_better_s = fn_s.replace('htmls', 'better_htmls')
    # Write the better HTML to a new file
    with open(fn_better_s, 'w', encoding='utf-8') as enf:
        # Replace re pattern matches with an empty string
        nodiv1_html_s = re.sub(div1_re_pattern, '', str(soup))
        nodiv2_html_s = re.sub(div2_re_pattern, '', nodiv1_html_s, flags=re.MULTILINE)
        nospan_html_s = re.sub(span_re_pattern, '', nodiv2_html_s)
        better_html_s = re.sub(r'^\s*$\n', '', nospan_html_s, flags=re.MULTILINE)
        enf.write(better_html_s)
    print(f'Better HTML should now be inside file: {fn_better_s}')
    'Convert Better HTML string to Markdown syntax string.'
    better_md_s = convert_to_markdown(better_html_s)
    'Write Markdown syntax to a file.'
    fn_markdown_s = fn_s.replace('htmls', 'markdown_files').replace('.html', '.md')
    with open(fn_markdown_s, 'w', encoding='utf-8') as betterf:
        betterf.write(better_md_s)
    print(f'Better be ready: {fn_markdown_s}')
'done'
