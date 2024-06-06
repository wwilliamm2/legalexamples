'''~/lc17/rt20.py'''

'''
Extracts text from LA County tent rulings in html files.

Sends that text to groq - llama3-8b-8192 LLM for summarization.

Uses string processing to separate cases from each other.
'''


'''
Use this idea to split a large string obtained from html file into pieces:

s1 = 'abcd hr uuuy7 hr  iiiiiiiiiii9 hr      iiiiiiiiii hr'
s1.split('hr')

When I study the LA tent rulings I see an hr element acting as a boundary between cases.

I will use python-replace('<hr', 'CASE_BOUNDARY<hr')
to write a boundary phrase, "CASE_BOUNDARY", attached to the element.

Then I will use bs4 to extract text from the html file into a large string.

Then I will do this:

cases_s_l = large_string_s.split('CASE_BOUNDARY')

Then I will have most cases separated from each other.

A bug I see is that footnotes also rely on <hr>.
That bug causes this script to treat a footnote as a case.

I try to compensate by ignoring text-chunks which are <= 400 characters.
Also any case-text <= 400 is not an interesting case.

'''
print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, psycopg, pypdf, re, shutil, sys, time, typing

import langchain, langchain_core, langsmith, langchain_groq
import langchain_core.documents
import langchain_core.output_parsers
import langchain_core.prompts
import langchain_core.runnables
import langchain_community
import langchain_community.embeddings
import langchain_community.document_loaders
import langchain_community.llms
import langchain_community.tools
import langchain_community.utilities
import langchain_community.vectorstores
import langchain.agents
import langchain_postgres.vectorstores
import langchain_text_splitters

myts = str(datetime.datetime.now()).replace(' ','_')

os.environ["LANGCHAIN_ENDPOINT"]
os.environ["LANGCHAIN_HUB_API_URL"]
os.environ["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_HUB_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"]
os.environ["LANGCHAIN_PROJECT"]=f'rt20.py_{myts}'
os.environ["LANGCHAIN_PROJECT"]
os.environ["OPENAI_API_KEY"]
os.environ["GROQ_API_KEY"]
MIXTRAL = 'mixtral-8x7b-32768'
LLAMA3 = 'llama3-8b-8192'
mixtral_model = langchain_groq.ChatGroq(model=MIXTRAL)
llama3_model = langchain_groq.ChatGroq(model=LLAMA3)
phi3_model = langchain_community.llms.Ollama(model="phi3")
HF='all-MiniLM-L6-v2' # Sentence Transformer Model
embedding_model = langchain_community.embeddings.HuggingFaceEmbeddings(model_name=HF)
parser = langchain_core.output_parsers.StrOutputParser()
rpt = langchain_core.runnables.RunnablePassthrough()

def diro(obj): print('\n'.join(dir(obj))) ; return None

'........................ ......................................'

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import chain

from bs4 import BeautifulSoup


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

os.makedirs('rt20_summaries', exist_ok=True) # to store some files
'Loop through a list of html files.'
html_file_s_l = glob.glob('/home/tent1/tent1/lacourt/htmls/2023_09_21_[B-C]*.html')
for html_file_s in sorted(html_file_s_l):
    print(f'Processing html_file_s: {html_file_s}')
    shutil.copy2(html_file_s, "rt20_summaries/")
    'Create a folder to store summaries for each html file.'
    folder_name_s = f"rt20_summaries/{os.path.basename(html_file_s).replace('.html','')}"
    os.makedirs(folder_name_s, exist_ok=True)
    with open(html_file_s, 'r') as hf:
        html_s = hf.read()
    0
    'Create a text boundary near all hr-elements'
    html_cb_s = html_s.replace('<hr', 'CASE_BOUNDARY<hr')
    with open(f'{folder_name_s}/html_cb.html', 'w') as cbf:
        cbf.write(html_cb_s)
    0
    'Extract text from the boundary-enhanced html file.'
    with open(f'{folder_name_s}/html_cb.html', 'r') as cbf:
        soup = BeautifulSoup(cbf, 'html.parser')
    0
    large_s = soup.text
    'Write the text to file so I can study it.'
    soup_ts = str(datetime.datetime.now()).replace(' ','_')
    with open(f'{folder_name_s}/soup_{soup_ts}.txt', 'w') as tf:
        tf.write(large_s)
    0
    'Try to create a separate txt file for each tent_ruling.'
    tent_ruling_s_l = large_s.split('CASE_BOUNDARY')
    for tent_ruling_s in tent_ruling_s_l:
        time.sleep(2) # to help with file naming
        trts = str(datetime.datetime.now()).replace(' ','_')
        with open(f'{folder_name_s}/tent_ruling_{trts}.txt', 'w') as cf:
            cf.write(tent_ruling_s)
        0
    0
    th_i = 31 # seconds bc model is on my laptop.
    'Summarize each tent_ruling.'
    for tent_ruling_s in tent_ruling_s_l[1:-1]: # 0th and last are usually not cases
        print(f'Wait {th_i} sec ... I need to throttle API calls.')
        time.sleep(th_i)
        'Summarize.'
        print(f'html_file_s: {html_file_s}\n')
        print(f'Summarizing:\n{tent_ruling_s[:99]} ...\n')
        try:
            if len(tent_ruling_s) > 400: # It interests me
                urts = str(datetime.datetime.now()).replace(' ','_')
                'Send context sized <= 32001 (about 8000 tokens) to LLM.'
                context_i = 32001
                invoke_d = {'tent_ruling': tent_ruling_s[:context_i]}
                with open(f'{folder_name_s}/invoke_this_{urts}.txt', 'w') as invkf:
                    invkf.write(str(prompt.invoke(invoke_d)))
                tent_ruling_summary_s = chain.invoke(invoke_d)
                with open(f'{folder_name_s}/tent_ruling_summary_{urts}.txt', 'w') as cf:
                    cf.write(tent_ruling_summary_s)
        except Exception as err:
            print(err)
            time.sleep(th_i)
        0
    0
0

'''
mixtral_model gives better summaries.

llama3_model gives better behavior

The YAML format idea works well.
'''
