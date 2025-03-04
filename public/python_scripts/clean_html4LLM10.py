'''~/lx/lx14/public/py/clean_html4LLM10.py'''

'''
Cleans my.html so my LLM can more easily parse my.html.
Removes html-elements: anchor , script , style , link , comments , form , input
Removes attributes: id , class

Demo:
. ~/lx/lx14/public/lx14b_env.bash
[ or conda activate lx14b ]
python -i clean_html4LLM10.py
'''

print('Busy ...')
import bs4, datetime, glob, inspect, operator, os, re, shutil, sys, time

from bs4 import BeautifulSoup

with open('my.html', 'r') as cbf:
    soup = BeautifulSoup(cbf, 'html.parser')
'I want to see the text in my.html'    
large_s = soup.text
with open('soup.txt', 'w') as tf:
    tf.write(large_s)

'done'
