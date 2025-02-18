'''lcg10.py'''

'''
Demo of attaching a pdf file to a prompt as part of a request to Google Generative AI Gemini LLM.
'''

'''
Ref:
https://python.langchain.com/api_reference/google_genai/index.html

Demo:
conda create -n gemini2 python=3.12
conda activate  gemini2
pip install langchain
pip install -U langchain-google-genai

python -i lcg10.py
'''

import os
from langchain_google_genai import GoogleGenerativeAI
llm = GoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05")

prompt_s = 'I, the LLM, have studied the attached pdf file and I summarize it as this set of statements in Markdown format: '

# Here I attach invoice.pdf to the request and then call llm.invoke() to get a response from the API serving responses from a GoogleGenerativeAI LLM model.


