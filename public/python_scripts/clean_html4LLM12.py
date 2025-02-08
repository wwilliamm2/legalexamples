'''~/lx/lx14/public/py/clean_html4LLM12.py'''

'''
Cleans my.html so my LLM can more easily parse my.html.
Removes html-elements: anchor , script , style , link , comments , form , input
Removes attributes: id , class

Demo:
. ~/lx/lx14/public/lx14b_env.bash
[ or conda activate lx14b ]
python -i clean_html4LLM12.py
'''

print('Busy ...')
import bs4, datetime, glob, inspect, operator, os, re, shutil, sys, time

from bs4 import BeautifulSoup

with open('my.html', 'r', encoding='utf-8') as cbf:
    soup = BeautifulSoup(cbf, 'html.parser')
'I want to see the text in my.html'    
large_s = soup.text
with open('soup.txt', 'w') as tf:
    tf.write(large_s)

# Find and remove all unneeded elements
tag_l = ['a', 'script', 'style', 'link', 'form', 'input']
for elmnt in soup(tag_l):
    elmnt.decompose() # They should have called it delete() or rm() or ...

# Write the modified HTML to a new file
with open('my_enhanced.html', 'w', encoding='utf-8') as enf:
    enf.write(str(soup))

'''
gpt, Please write a simple Python demo which uses BeautifulSoup to remove comments from my.html

Answer:

Certainly! Here's a simple Python demo that uses BeautifulSoup to remove comments from your HTML file:

```python
from bs4 import BeautifulSoup, Comment

# Read the original HTML file
with open('my.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find and remove all comment nodes
comments = soup.find_all(text=lambda text: isinstance(text, Comment))
for comment in comments:
    comment.extract()

# Write the modified HTML to a new file
with open('my_without_comments.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("Comments removed and HTML saved to my_without_comments.html")
```

This script does the following:

1. Imports BeautifulSoup and Comment from bs4.
2. Opens and reads 'my.html'.
3. Creates a BeautifulSoup object using the 'html.parser'.
4. Finds all comment nodes using a lambda function that checks if the text is an instance of Comment.
5. Removes each comment using the `extract()` method.
6. Writes the modified HTML (without comments) to 'my_without_comments.html'.

This script will preserve the structure of your HTML while removing all comments. It's a straightforward way to clean up your HTML file.

Remember to have BeautifulSoup installed (`pip install beautifulsoup4`) before running this script.

Let me know if you need any clarification or have any questions about this demo!

---
Answer from Perplexity: https://www.perplexity.ai/search/gpt-i-have-a-python-script-nam-Rso_Y6gkTgKfvJ4xYBhdMw?utm_source=copy_output


'''
