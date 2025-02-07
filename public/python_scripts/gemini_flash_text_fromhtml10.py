'''~/lx/lx14/public/py/gemini_flash_text_fromhtml10.py'''

'''
Extracts text from html file.

Demo:
conda activate gemini1
python -i gemini_flash_text_fromhtml10.py
'''

'''
These interest me, today:
gemini-2.0-flash-lite-preview 1500 req/day free
gemini-2.0-flash-exp          1500 req/day free
'''

# Check Google AI Studio API key
import os
os.environ["GOOGLE_API_KEY"]

import google.generativeai as genai
print('Busy ...')
import datetime, glob, inspect, json, operator, re, shutil, sys, time, typing

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import langchain_core

parser = langchain_core.output_parsers.StrOutputParser()

llm_s_l = ['gemini-2.0-flash-lite-preview','gemini-2.0-flash-exp']

# create prompt list of tpls acting as messages
prompt_s = '''Study the HTML syntax below. Please extract text from the HTML sysntax and strip away all the HTML-tags.
Typically I use Python BeautifulSoup to do this task but I want you to use your knowledge of English and HTML to do this task.
The way I do this with BeautifulSoup is I rely on syntax like this: 
```
with open('my.html', 'r') as cbf:
    soup = BeautifulSoup(cbf, 'html.parser')
large_s = soup.text
# Now I have large_s which is large string full of English which has been extracted from html_cb.html
with open('my.txt', 'w') as mytf:
    mytf.write(large_s)
```
Now that you know how I extract text using BeautifulSoup (and then write it into a file named my.txt),
please extract and display the text (using your intelligence, knowledge of HTML, and knowledge of English) inside this HTML syntax: '''

user_tpl = ("user", prompt_s + "\n[[{html_syntax}]]")
messages_l = [user_tpl]
prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)

html_s = '<html>Hello Mr. Model. I like vegetarian pizza with a wide variety of veggies.</html>'

invoke_d = {'html_syntax': html_s}

llm_s = llm_s_l[0]

myllm_model = ChatGoogleGenerativeAI(model=llm_s)

chain = prompt | myllm_model | parser

text_fromhtml_s = chain.invoke(invoke_d)

print(text_fromhtml_s)

'done'
