'''~/lx/lx14/public/py/gemini_flash_text_from_png16.py'''

'''
Uses LLM to generate text from png files.

Demo:
conda activate gemini1
python -i gemini_flash_text_from_png16.py
'''

from google import genai

# Check Google AI Studio API key
import os

print('Busy ...')
import datetime, glob, inspect, json, operator, re, shutil, sys, time, typing

llm_s_l = ['gemini-2.0-flash-lite-preview','gemini-2.0-flash-exp']

model_id = llm_s_l[0]

fn_s_l = sorted(glob.glob('/media/dan/ssd2/tmp/scscourt/pdfs/2023_0916_2245_33_dept10_tues/2*png'))

fn_s = fn_s_l[0]

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

doc_png = client.files.upload(file=fn_s, config={'display_name': fn_s})

file_size = client.models.count_tokens(model=model_id,contents=doc_png)

print(f'File: {doc_png.display_name} equals to {file_size.total_tokens} tokens')

prompt_s = '''Please study information from my file and then extract (verbatim) all text you see in it.
My file is an image of a single page in California legal document filed in a county court.
Please preserve the format and placement of all the words, sentenances, and paragraphs.
Please give me plain text; I dislike Markdown and HTML.
I want you to preserve the format because I want your extracted and verbatim text to be comprehensive for an attorney.
'''

response = client.models.generate_content(model=model_id, contents=[doc_png, prompt_s])

try:
    # Extract and print only the "text" field from the response
    if response.candidates:
        response.candidates[0].content.parts[0].text
        print(response.candidates[0].content.parts[0].text)
except Exception as myexp:
    print('I see a problem with {fn_s}\ndue to: ', str(myexp))
