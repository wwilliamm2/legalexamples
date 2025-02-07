'''~/lx/lx14/public/py/gen_summaries20gemini.py'''

'''
Reads filenames from tenttext_lacourt14.txt
to generate llm-summaries of the corresponding text files.

Demo:
conda create -n gemini1 python=3.11
conda activate gemini1

pip install google-generativeai
pip install langchain langchain-google-genai

ll ~/anaconda3/envs/gemini1/lib/python3.11/site-packages/

python -i gen_summaries20gemini.py
'''

'''Get a list of model-names.'''

# Check Google AI Studio API key
import os
os.environ["GOOGLE_API_KEY"]

import google.generativeai as genai

m_l = [mdl.name for mdl in genai.list_models()]

'''
>>> m_l
['models/chat-bison-001', 'models/text-bison-001', 'models/embedding-gecko-001', 'models/gemini-1.0-pro-latest', 'models/gemini-1.0-pro', 'models/gemini-pro', 'models/gemini-1.0-pro-001', 'models/gemini-1.0-pro-vision-latest', 'models/gemini-pro-vision', 'models/gemini-1.5-pro-latest', 'models/gemini-1.5-pro-001', 'models/gemini-1.5-pro-002', 'models/gemini-1.5-pro', 'models/gemini-1.5-flash-latest', 'models/gemini-1.5-flash-001', 'models/gemini-1.5-flash-001-tuning', 'models/gemini-1.5-flash', 'models/gemini-1.5-flash-002', 'models/gemini-1.5-flash-8b', 'models/gemini-1.5-flash-8b-001', 'models/gemini-1.5-flash-8b-latest', 'models/gemini-1.5-flash-8b-exp-0827', 'models/gemini-1.5-flash-8b-exp-0924', 'models/gemini-2.0-flash-exp', 'models/gemini-2.0-flash', 'models/gemini-2.0-flash-001', 'models/gemini-2.0-flash-lite-preview', 'models/gemini-2.0-flash-lite-preview-02-05', 'models/gemini-2.0-pro-exp', 'models/gemini-2.0-pro-exp-02-05', 'models/gemini-exp-1206', 'models/gemini-2.0-flash-thinking-exp-01-21', 'models/gemini-2.0-flash-thinking-exp', 'models/gemini-2.0-flash-thinking-exp-1219', 'models/learnlm-1.5-pro-experimental', 'models/embedding-001', 'models/text-embedding-004', 'models/aqa', 'models/imagen-3.0-generate-002']
>>>
'''

my_mdl = [mdl for mdl in genai.list_models() if mdl.name == 'models/gemini-2.0-pro-exp'  ][0]
ur_mdl = [mdl for mdl in genai.list_models() if mdl.name == 'models/gemini-2.0-flash-exp'][0]
'''
>>> my_mdl
Model(name='models/gemini-2.0-pro-exp',
      base_model_id='',
      version='2.0',
      display_name='Gemini 2.0 Pro Experimental',
      description='Experimental release (February 5th, 2025) of Gemini 2.0 Pro',
      input_token_limit=2097152,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)
>>>
>>> ur_mdl
Model(name='models/gemini-2.0-flash-exp',
      base_model_id='',
      version='2.0',
      display_name='Gemini 2.0 Flash Experimental',
      description='Gemini 2.0 Flash Experimental',
      input_token_limit=1048576,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens', 'bidiGenerateContent'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=40)
>>> 
'''

print('Busy ...')
import datetime, glob, inspect, json, operator, re, shutil, sys, time, typing

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import langchain_core

llm_s_l = ['gemini-2.0-flash-exp','gemini-2.0-pro-exp']

# create prompt list of tpls acting as messages
prompt_s = '''Please write a simple summary in YAML format of a legal document, a
"tentative ruling", written by a Judge about a future Court Hearing. 
The legal document describes the Judge's thinking based on infomation presented 
to the Judge before today.
In YAML format, please write: Case Number, Plaintiff's Name, Defendant's Name,
People-Names, Company-Names, Places, Dates, Events, Money, 
Intentions, Facts, Disputes, Acts, Agreements, Laws, Case Citations, 
Statutes, Roles and Signifcant Statements.
I really appreciate your help!
Oh, also please write English-text to summarize this judge's tentative ruling: '''

user_tpl = ("user", prompt_s + "\n[[{tent_ruling}]]")
messages_l = [user_tpl]
prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)
            
dot_s = '..................... .....................'
top0_s = 'The summary displayed below was created by an LLM named: '

with open('tenttext_lacourt14.txt') as txtf:
    tr_files_s = txtf.read()
tr_fn_s_l = sorted(tr_files_s.split('\n')[:-1]) # skip last 1

context_i = 1234567890 # large-ish, smaller is friendlier to LLM

# I want the outer loop to loop through file names.
# Inside each file-effort I will loop through names of LLM-models.

for tr_fn_s in tr_fn_s_l[0:11]:
    summ_fn_s = tr_fn_s.replace('/tent_ruling_','/summary_')
