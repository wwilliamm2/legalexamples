'''~/lx/lx14/public/py/gen_summaries12_hp88.py'''

'''
Reads filenames from tenttext_lacourt14.txt
to generate llm-summaries of the corresponding text files.

Ref:
gen_summaries10.py
gen_summaries11.py
~dan/lc17/rt20.py

Demo:
ll ~/anaconda3/envs/
. ~/lx/lx14/public/lx14b_env.bash
python gen_summaries12_hp88.py

'''

print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import langchain, langchain_core, langsmith, langchain_groq

myts = str(datetime.datetime.now()).replace(' ','_')

os.environ["GROQ_API_KEY"]

LLAMA3 = 'llama3-8b-8192'

llama3_model = langchain_groq.ChatGroq(model=LLAMA3)

parser = langchain_core.output_parsers.StrOutputParser()

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

'I use this to connect prompt to groq llama3_model:'
chain = prompt | llama3_model | parser

'''Use tenttext_lacourt14.txt, 
a full of tr-file-names to drive a loop 
which calls LLM to summarize each tr file.'''

with open('tenttext_lacourt14.txt') as txtf:
    tr_files_s = txtf.read()
tr_fn_s_l = sorted(tr_files_s.split('\n')[:-1]) # skip last 1

for tr_fn_s in tr_fn_s_l[-1299:]:
    summ_fn_s = tr_fn_s.replace('/tent_ruling_','/summary_')
    'I shd check if summ_fn_s exists so I dont overwrite it'
    'gpt, write demo python syntax which checks if /tmp/hello.txt exists before I create it.'
    'Use: os.path.isfile("/tmp/hello.txt")'
    if os.path.isfile(summ_fn_s):
        f'{summ_fn_s} is a file, avoid it.'
    else:
        with open(tr_fn_s) as txtf:
            tr_pln_txt_s = txtf.read() # Txt I want to summarize
        'If tr_pln_txt_s is large enough,'
        if len(tr_pln_txt_s) > 700: # It interests me
            'Note the file name:'
            print(f'Summarizing this file: {tr_fn_s}')
            print(f'Its length in chars: {len(tr_pln_txt_s)}')
            print('Busy with API ...')
            'I shd call LLM here.'
            'Send context sized <= 30011 (about 8000 tokens) to LLM.'
            context_i = 29011
            'Prep a dict to help me call invoke():'
            invoke_d = {'tent_ruling': tr_pln_txt_s[:context_i]}
            'Rubber meets road:'
            try:
                summary_s = chain.invoke(invoke_d)
                with open(f'{summ_fn_s}', 'w') as sumf:
                    sumf.write(summary_s)
                    print(f'New summary: {summ_fn_s}')
                    # Make note of invoke_d
                with open(f'/tmp/invoke_d.txt', 'w') as invdf:
                    invdf.write(str(prompt.invoke(invoke_d)))
                'remem to throttle API calls:'
                print('Busy with API ...')
                time.sleep(66) # seconds
            except:
                time.sleep(600) # 10min
