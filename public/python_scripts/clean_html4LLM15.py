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
        enh_html_s = str(soup).replace('<div></div>','').replace('<span></span>','')
        enf.write(enh_html_s)
'done'

