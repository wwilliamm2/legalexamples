'''~/di/py/lcg01.py'''

'''
Helps me study this Python package: langchain-google

Ref:
https://github.com/langchain-ai/langchain
https://github.com/langchain-ai/langchain-google

Demo:
conda create -n gemini2 python=3.12
conda activate gemini2
pip install langchain langchain-google
python -i lcg01.py
'''

import os
import langchain, langchain-google

google_api_key = os.environ(['GOOGLE_API_KEY'])

# Get a list of LLM models available from Google AI Studio

'''
gpt, please study the Python script listed below named lcg01.py
I want to enhance lcg01.py so it gives me a list of models which
I see listed in the web-UI of my google AI Studio account served from this URL:
https://aistudio.google.com/prompts/new_chat
The web-UI of the above URL has a section on the RHS named Run settings.
At the top of Run settings I see a select-option pull down menu which lists names of Google LLMs.
For example I see this name:
'Gemini 2.0 Pro Experimental 02-05'
which has this label attached to the name: 'gemini-2.0-pro-exp-02-05'.
If possible I want to rely on langchain-google as much as possible
(rather than direct use of packages from Google) to connect to the Google API
because that is a development pattern I want to embrace because I see
langchain scripts as more portable when I need to connect to LLMs from
different LLM-providers.
'''

