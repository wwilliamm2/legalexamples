'''~/lx/lx14/public/py/gemini_flash_text_fromhtml12.py'''

'''
Extracts text from html file.

Demo:
conda activate gemini1
python -i gemini_flash_text_fromhtml12.py
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
prompt_s = '''Please study the HTML syntax (from a file named hal.html) below.
Try to understand the intentions of the HTML-author ("Hal") about how Hal wants to present the English to us.
Please look for headings, bolded words, horizontal lines, paragraphs, sentences, and any formatting clues.
Try to ignore syntax which contains JavaScript. Also ignore any non-English content.
Try to ignore any syntax which is a long-string of characters because that might be encoded data which I dont care about.
From a semantic viewpoint,
the English in hal.html contains legal information about some specific Court cases (or maybe just 1 case).
That legal information is important to me, please ensure you focus on it.
Please try to ignore information displayed by boiler-plate template nav-bar menu links like 'Home', 'Online Services' and so on.
Next, try to extract the important semantic English relevant to the Court case(s).
During your extraction efforts, do your best to format the English using Markdown syntax so that Hal's formatting efforts are still honored.
If you semantically sense more than one Court case from hal.html, please separate each case by a horizontal line.
When you are done, please display the English (formatted by your Markdown) full of legal information to me.
So, now that you understand what I want, please study this HTML syntax and display the English in it: '''

user_tpl = ("user", prompt_s + "\n[[{html_syntax}]]")
messages_l = [user_tpl]
prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)

html_fn_s = 'my.html'
with open(html_fn_s, 'r') as myhf:
    html_s = myhf.read()

invoke_d = {'html_syntax': html_s}

llm_s = llm_s_l[0]

myllm_model = ChatGoogleGenerativeAI(model=llm_s)

chain = prompt | myllm_model | parser

text_fromhtml_s = chain.invoke(invoke_d)

with open('my.txt', 'w') as mytf:
    mytf.write(text_fromhtml_s)

'done'

'''

'''
