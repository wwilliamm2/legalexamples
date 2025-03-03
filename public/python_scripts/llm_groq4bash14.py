'''~/lx/lx14/public/py/llm_groq4bash14.py'''

'''
Sends requests to groq LLM for bash scripts.
Ref: https://console.groq.com/docs/quickstart

Demo:

. gemini2.bash

pip install groq

python llm_groq4bash14.py

Later I will support cmd-line tokens like this:
python llm_groq4bash14.py ~/prompt.txt gemma2-9b-it
'''

print('Busy ...')
import datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

import requests, groq

from groq import Groq

myts = str(datetime.datetime.now()).replace(' ','_')

llm_s_l = ['gemma2-9b-it', 'llama3-8b-8192', 'llama-3.3-70b-specdec', 'mixtral-8x7b-32768']

# create prompt list of tpls acting as messages
with open('/home/dan/prompt.txt', 'r') as pf:
    prompt_s = pf.read()

# Initialize the Groq client
client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

# Create a chat completion
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You act as a Law Clerk who can spot typos and bad grammar."
        },
        {
            "role": "user",
            "content": prompt_s
        }
    ],
    model='gemma2-9b-it' #"llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

'done'
