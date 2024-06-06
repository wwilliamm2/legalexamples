'''~/lx/lx14/public/py/gen_summaries10.py'''

'''
Reads filenames from tenttext_lacourt14.txt
to generate llm-summaries of the corresponding text files.

Ref:
~dan/lc17/rt20.py
'''

print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing


'Summarize this large file:'
txt_f_s = 'lacourt/text/2024_07_19_LAM_71/tent_ruling_01.txt'

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


'done'

