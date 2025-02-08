'''~/lx/lx14/public/py/clean_html4LLM15.py'''

'''
Cleans my.html so my LLM can more easily parse my.html.
Removes html-elements: anchor , script , style , link , comments , form , input
Removes attributes: id , class

Demo:
. ~/lx/lx14/public/lx14b_env.bash
[ or conda activate lx14b ]
python -i clean_html4LLM15.py
'''

print('Busy ...')
import bs4, datetime, glob, inspect, operator, os, re, shutil, sys, time

from bs4 import BeautifulSoup, Comment

fn_s_l = sorted(glob.glob('/media/dan/ssd2/tmp/htmls/202*.html'))[:33]
# Define the regular expression pattern
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
    fn_enh_s = fn_s.replace('/htmls/','/enhanced_htmls/')    
    # Write the modified HTML to a new file
    with open(fn_enh_s, 'w', encoding='utf-8') as enf:
        # Replace re pattern matches with an empty string
        nodiv1_html_s = re.sub(div1_re_pattern, '', str(soup))
        nodiv2_html_s = re.sub(div2_re_pattern, '', nodiv1_html_s, flags=re.MULTILINE)
        nospan_html_s = re.sub(span_re_pattern, '', nodiv2_html_s)
        enh_html_s = re.sub(r'^\s*$\n', '', nospan_html_s, flags=re.MULTILINE)
        enf.write(enh_html_s)
'done'

'''
gpt, Please write a simple Python demo which uses the re package to replace
'<div>   </div>' with ''
using a regular expression to match 0 or more space characters between the two div-tags.

Answer:
div_re_pattern = r'<div>\s*</div>'
clean_s = re.sub(div_re_pattern, '', dirty_s)
'''

'''
gpt, Please write a simple Python demo which removes empty lines from a text file.
Perhaps a regular expression exists which matches an empty line?

Answer:

pattern = r'^\s*$\n'

# Remove empty lines
cleaned_content = re.sub(pattern, '', mystring, flags=re.MULTILINE)

'''
