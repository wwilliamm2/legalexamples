'''~/lx/lx14/public/py/gen_summaries10.py'''

'''
NOT USED ANYMORE.

Practices operation of llama3 LLM model to generate summary of tent ruling.

Reads filenames from tenttext_lacourt14.txt
to generate llm-summaries of the corresponding text files.

Ref:
~dan/lc17/rt20.py
'''

print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import langchain, langchain_core, langsmith, langchain_groq

myts = str(datetime.datetime.now()).replace(' ','_')

'Summarize this large file:'
txt_f_s = 'lacourt/text/2024_07_19_LAM_71/tent_ruling_01.txt'

os.environ["LANGCHAIN_ENDPOINT"]
os.environ["LANGCHAIN_HUB_API_URL"]
os.environ["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_HUB_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"]
os.environ["LANGCHAIN_PROJECT"]=f'gen_summaries10.py_{myts}'
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

'Read the plain text file, txt_f_s, into a string, tent_ruling_s:'
with open(txt_f_s) as txtf:
    tent_ruling_s = txtf.read()

'Prep a dict to help me call invoke():'
invoke_d = {'tent_ruling': tent_ruling_s}
'Rubber meets road:'
tent_ruling_summary_s = chain.invoke(invoke_d)
print(tent_ruling_summary_s)

'done'

