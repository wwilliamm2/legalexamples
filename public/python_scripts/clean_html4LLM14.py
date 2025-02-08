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

'''
gpt, Please write a simple Python demo script which uses BeautifulSoup to remove empty div elements from HTML syntax.

Certainly! Here's a simple Python demo script that uses BeautifulSoup to remove empty div elements from HTML syntax:

```python
from bs4 import BeautifulSoup

def remove_empty_divs(soup):
    # Find all div elements
    divs = soup.find_all('div')
    
    # Iterate through divs in reverse order to avoid skipping elements
    for div in reversed(divs):
        # Check if the div is empty (no text and no non-empty child elements)
        if not div.text.strip() and not div.find(lambda tag: tag.name != 'br' and not isinstance(tag, str)):
            div.extract()
    
    return soup

# Read the original HTML file
with open('my.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Remove empty div elements
cleaned_soup = remove_empty_divs(soup)

# Write the modified HTML to a new file
with open('my_without_empty_divs.html', 'w', encoding='utf-8') as file:
    file.write(str(cleaned_soup))

print("Empty div elements removed. Modified HTML saved to my_without_empty_divs.html")
```

This script does the following:

1. Defines a function `remove_empty_divs` that:
   - Finds all div elements in the soup object.
   - Iterates through the divs in reverse order (to avoid issues with changing the structure while iterating).
   - Checks if each div is empty by ensuring it has no text content (after stripping whitespace) and no non-empty child elements (ignoring <br> tags).
   - Removes empty divs using the `extract()` method.

2. Reads the original HTML file 'my.html'.

3. Creates a BeautifulSoup object using the 'html.parser'.

4. Applies the `remove_empty_divs` function to remove empty div elements.

5. Writes the modified HTML without empty divs to 'my_without_empty_divs.html'.

This script effectively removes div elements that have no content or only contain whitespace or break tags. It preserves divs that have any meaningful content, including text or other non-empty elements.

Remember to have BeautifulSoup installed (`pip install beautifulsoup4`) before running this script.

---
Answer from Perplexity: https://www.perplexity.ai/search/gpt-i-have-a-python-script-nam-Rso_Y6gkTgKfvJ4xYBhdMw?utm_source=copy_output

'''
