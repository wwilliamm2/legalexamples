'''gen_summaries19groq.py'''

'''
Reads filenames from tenttext_lacourt14.txt
to generate llm-summaries of the corresponding text files.

Demo:
ll ~/anaconda3/envs/
. ~/lx/lx14/public/lx14b_env.bash
python gen_summaries19groq.py

'''

print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import langchain, langchain_core, langsmith, langchain_groq

myts = str(datetime.datetime.now()).replace(' ','_')

os.environ["GROQ_API_KEY"]

parser = langchain_core.output_parsers.StrOutputParser()

llm_s_l = ['gemma2-9b-it', 'llama3-8b-8192', 'llama-3.3-70b-specdec', 'mixtral-8x7b-32768']

# create prompt list of tpls acting as messages
prompt_s = '''Please write a simple summary in Markdown format of a legal document, a
"tentative ruling", written by a Judge about a future Court Hearing. 
The legal document describes the Judge's thinking based on infomation presented 
to the Judge before today.
In Markdown format, please write: Case Number, Plaintiff's Name, Defendant's Name,
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

context_i = 199011 # large-ish, smaller is friendlier to LLM
        
# I want the outer loop to loop through file names.
# Inside each file-effort I will loop through names of LLM-models.

for tr_fn_s in tr_fn_s_l[:1000]:
    summ_fn_s = tr_fn_s.replace('/tent_ruling_','/summary_')
    with open(tr_fn_s) as txtf:
        tr_pln_txt_s = txtf.read()
    if len(tr_pln_txt_s) > 700: # It interests me
        print('Busy with API ...')
        'Prep a dict to help me call invoke():'
        invoke_d = {'tent_ruling': tr_pln_txt_s[:context_i]}
        for llm_s in llm_s_l:
            'Note the file name:'
            print(f'{llm_s} might summarize this file: {tr_fn_s}')
            print(f'File length in chars: {len(tr_pln_txt_s)}')
            try:
                myllm_model = langchain_groq.ChatGroq(model=llm_s)            
                chain = prompt | myllm_model | parser
                'Rubber meets road:'
                summary_s = chain.invoke(invoke_d)
                with open(f'{summ_fn_s}', 'a') as sumf:
                    tsnow_s = str(datetime.datetime.now()).replace(' ','_')
                    top_s = f'{dot_s}\nOn {tsnow_s}\n{top0_s} "{llm_s}":\n'
                    sumf.write(f'{top_s}{summary_s}\n')
                print(f'We might have new summary: {llm_s} + {summ_fn_s}')
                # Make note of invoke_d
                with open(f'/tmp/invoke_d.txt', 'w') as invdf:
                    invdf.write(str(prompt.invoke(invoke_d)))
                'remem to throttle API calls:'
                print('Busy with API ...')
                time.sleep(25) # seconds
            except Exception as myex:
                print(f'Exception on 1st-try. I am sleeping it off:\n{str(myex)}')
                # I want to make note of this Exception.
                # Rather deal with logging, just put it in the summary file.
                # I can filter it out later if I change my mind about the best destinationn.
                with open(f'{summ_fn_s}', 'a') as sumf:
                    tsnow_s = str(datetime.datetime.now()).replace(' ','_')
                    top_s = f'{dot_s}\nOn {tsnow_s}\n{top0_s} "{llm_s}":\n'
                    sumf.write(f'{top_s}Exception:\n{str(myex)}\n')
                time.sleep(600)
