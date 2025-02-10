'''~/lx/lx14/public/py/gemini_flash_text_from_png15.py'''

'''
Uses LLM to generate text from png files.

Demo:
conda activate gemini1
python -i gemini_flash_text_from_png15.py
'''

# Check Google AI Studio API key
import os
os.environ["GOOGLE_API_KEY"]

import google.generativeai as genai
print('Busy ...')
import datetime, glob, inspect, json, operator, re, shutil, sys, time, typing

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import langchain_core

parser = langchain_core.output_parsers.StrOutputParser()

# model_id =  "gemini-2.0-flash"

llm_s_l = ['gemini-2.0-flash-lite-preview','gemini-2.0-flash-exp']

model_id = llm_s_l[0]

fn_s_l = sorted(glob.glob('/media/dan/ssd2/tmp/scscourt/pdfs/2023_0916_2245_33_dept10_tues/2*png'))

api_key = os.environ["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)


fn_s = fn_s_l[0]
tr_png = client.files.upload(file=fn_s, config={'display_name': 'TR page'})

file_size = client.models.count_tokens(model=model_id,contents=tr_png)
print(f'File: {tr_png.display_name} equals to {file_size.total_tokens} tokens')

# create prompt list of tpls acting as messages
prompt_s = '''Please study the png file and then extract all text you see in it.
Please preserve the format and placement of all the words, sentenances, and paragraphs.
'''

response = client.models.generate_content(
    model=model_id,
    contents=[tr_png, prompt]
)

try:
    # Extract and print only the "text" field from the response
    if response.candidates:
        response.candidates[0].content.parts[0].text
        print(response.candidates[0].content.parts[0].text)
except Exception as myexp:
    print('I see a problem due to: ', str(myexp))
