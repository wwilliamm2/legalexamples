'''~/lx/lx14/public/py/gemini_flash_text_from_markdown14.py'''

'''
Extracts text from html file.

Demo:
conda activate gemini1
python -i gemini_flash_text_from_markdown14.py
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
prompt_s = '''Please study the Markdown syntax I will show you soon.
Try to understand the intentions of the Markdown-author.
The Markdown-author wants to present English to us which describes "Tentative Rulings" from Judges in Los Angeles Courts.
Usually a Tentative Ruling is a written response from a Judge to a request (sometimes a request is called a "Motion") from a Plaintiff or a Defendant.
The Markdown-English contains actual writings from the Judges; I want you to focus on their writings.

Please ignore any non-English content directed at non-English speakers.
Please try to ignore general information displayed in the Markdown-English which is relevant people who have general questions about how the Court operates.

Please look for headings, bolded words, horizontal lines, paragraphs, sentences, and any formatting clues.

From a semantic viewpoint,
the English contains legal information about some specific Court cases (or maybe just 1 case).

That legal information is important to me, please ensure you focus on it.

NEXT, PLEASE TRY TO EXTRACT, VERBATIM, the important semantic English relevant to each Court case.
During your extraction efforts, do your best to format the English so it is easy for a human to read.
For example, start each paragraph with a tab.
If you semantically sense more than one Court case in the Markdown-English, please separate each case by a horizontal line.
When you are done, please display the English full of legal information to me.
So, now that you understand what I want, please study this Markdown syntax and display the English in it: '''

user_tpl = ("user", prompt_s + "\n[[{markdown_syntax}]]")
messages_l = [user_tpl]
prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)

fn_s_l = sorted(glob.glob('/media/dan/ssd2/tmp/markdown_files/202*.md'))[:5]

for markdown_fn_s in fn_s_l:
    txt_fn_s = markdown_fn_s.replace('.md','.txt')
    print(f'At {str(datetime.datetime.now())}, Busy with: {txt_fn_s}')    
    if os.path.exists(txt_fn_s):
        print('The text is already extracted. Work on the next file.')
    else:
        'I will extract case info into text file: ' + txt_fn_s
        with open(markdown_fn_s, 'r') as mymdf:
            markdown_s = mymdf.read()
        invoke_d = {'markdown_syntax': markdown_s}
        llm_s = llm_s_l[0] # I have choices, today I want the 0th model.
        myllm_model = ChatGoogleGenerativeAI(model=llm_s)
        chain = prompt | myllm_model | parser
        text_frommarkdown_s = chain.invoke(invoke_d)
        top_s = f'This file contains information generated from:\n{markdown_fn_s}\nby an LLM named {llm_s}.\n'
        with open(txt_fn_s, 'w') as mytf:
            mytf.write(top_s + text_frommarkdown_s)
        time.sleep(15) # Throttle my calls to avoid trouble with API.

'done'

'''

'''
