'''~/lx/lx14/public/py/llm_groq4bash13.py'''

'''
Sends requests to groq LLM for bash scripts.

Demo:

. "/home/dan/anaconda3/etc/profile.d/conda.sh"
conda activate lx14b

python llm_groq4bash13.py ~/prompt.txt gemma2-9b-it
'''

print('Busy ...')
import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import langchain, langchain_core, langsmith, langchain_groq

myts = str(datetime.datetime.now()).replace(' ','_')

os.environ["GROQ_API_KEY"]

parser = langchain_core.output_parsers.StrOutputParser()

llm_s_l = ['gemma2-9b-it', 'llama3-8b-8192', 'llama-3.3-70b-specdec', 'mixtral-8x7b-32768']

# create prompt list of tpls acting as messages
prompt_s = '''Please describe honeybee behavior to a 10 year old student.'''

user_tpl = ("user", prompt_s + "\n[[{extra_s}]]")
messages_l = [user_tpl]
prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)

invoke_d = {'extra_s': " One page at most."}

