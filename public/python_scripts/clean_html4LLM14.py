'''~/lx/lx14/public/py/clean_html4LLM14.py'''

'''
Cleans my.html so my LLM can more easily parse my.html.
Removes html-elements: anchor , script , style , link , comments , form , input
Removes attributes: id , class

Demo:
. ~/lx/lx14/public/lx14b_env.bash
[ or conda activate lx14b ]
python -i clean_html4LLM14.py
'''

print('Busy ...')
import bs4, datetime, glob, inspect, operator, os, re, shutil, sys, time

from bs4 import BeautifulSoup, Comment

with open('my.html', 'r', encoding='utf-8') as cbf:
    soup = BeautifulSoup(cbf, 'html.parser')
'I want to see the text in my.html'    
large_s = soup.text
with open('soup.txt', 'w') as tf:
    tf.write(large_s)

# Find and remove all unneeded elements
tag_l = ['a', 'script', 'style']
for elmnt in soup(tag_l):
    elmnt.decompose() # They should have called it delete() or rm() or ...

# Find and remove all comment nodes
comments = soup.find_all(string=lambda string: isinstance(string, Comment))
for comment in comments:
    comment.extract()

# Remove all attributes
for tag in soup.find_all(True):
    tag.attrs = {}
    
# Write the modified HTML to a new file
with open('my_enhanced.html', 'w', encoding='utf-8') as enf:
    enf.write(str(soup))

