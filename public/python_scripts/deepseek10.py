'''~/lx/lx14/public/py/deepseek10.py'''

'''
Helps me study groq + deepseek.

Demo:
ll ~/anaconda3/envs/
. ~/lx/lx14/public/lx14b_env.bash
python deepseek10.py
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
prompt_s = '''Please write a simple comparison of Python 3.12 to Python 3.11: '''

user_tpl = ("user", prompt_s + "\n[[{tent_ruling}]]")

messages_l = [user_tpl]

prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(messages_l)

'I use this to connect prompt to groq llama3_model:'
chain = prompt | llama3_model | parser
