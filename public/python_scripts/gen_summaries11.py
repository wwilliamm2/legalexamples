'''gen_summaries11.py'''

'''
Reads filenames from tenttext_lacourt14.txt
to generate llm-summaries of the corresponding text files.

Ref:
gen_summaries10.py
~dan/lc17/rt20.py

'''

print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import langchain, langchain_core, langsmith, langchain_groq

myts = str(datetime.datetime.now()).replace(' ','_')

os.environ["LANGCHAIN_ENDPOINT"]
os.environ["LANGCHAIN_HUB_API_URL"]
os.environ["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_HUB_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"]
os.environ["LANGCHAIN_PROJECT"]=f'gen_summaries11.py_{myts}'
os.environ["LANGCHAIN_PROJECT"]
os.environ["OPENAI_API_KEY"]
os.environ["GROQ_API_KEY"]

LLAMA3 = 'llama3-8b-8192'

llama3_model = langchain_groq.ChatGroq(model=LLAMA3)

parser = langchain_core.output_parsers.StrOutputParser()

# create prompt list of tpls acting as messages
prompt_s = '''Write a simple summary in YAML format of a legal document, a
"tentative ruling", written by a Judge about a future Court Hearing. 
The document describes the Judge's thinking based on infomation presented 
to the Judge before today.
In YAML format, write: Case Number, Plaintiff's Name, Defendant's Name,
People-Names, Company-Names, Places, Dates, Events, Money, 
Intentions, Facts, Disputes, Acts, Agreements, Laws, Case Citations, 
Statutes, Roles and Signifcant Statements.
Also write English-text to summarize this judge's tentative ruling: '''

user_tpl = ("user", prompt_s + "\n[[{tent_ruling}]]")

messages_l = [user_tpl]

prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)

'I use this to connect prompt to groq llama3_model:'
chain = prompt | llama3_model | parser

'''Use tenttext_lacourt14.txt, 
a full of tr-file-names to drive a loop 
which calls LLM to summarize each tr file.'''

with open('tenttext_lacourt14.txt') as txtf:
    tr_files_s = txtf.read()
tr_fn_s_l = tr_files_s.split('\n')

'not done yet'
