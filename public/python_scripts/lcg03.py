'''~/di/py/lcg03.py'''

'''
Helps me study this Python package: langchain-google

Ref:
https://github.com/langchain-ai/langchain
https://github.com/langchain-ai/langchain-google

Demo:
conda create -n gemini2 python=3.12
conda activate gemini2
pip install langchain langchain-google
python -i lcg03.py
'''

import os
import langchain_google

#  You MUST set this environment variable.
#  See https://python.langchain.com/docs/integrations/llms/google_genai
google_api_key = os.environ.get('GOOGLE_API_KEY')

# Get a list of LLM models available from Google AI Studio

if not google_api_key:
    raise ValueError("The GOOGLE_API_KEY environment variable is not set.")

from langchain_google import genai

'''
>>> from langchain_google import genai
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'genai' from 'langchain_google' (/home/dan/anaconda3/envs/gemini2/lib/python3.12/site-packages/langchain_google/__init__.py)
>>>
'''
