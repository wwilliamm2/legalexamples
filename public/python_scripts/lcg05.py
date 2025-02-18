'''~/di/py/lcg05.py'''

'''
Helps me study this Python package: langchain-google

Ref:
https://python.langchain.com/api_reference/google_genai/index.html

Demo:
conda create -n gemini2 python=3.12
conda activate gemini2
pip install langchain
pip install langchain-google # maybe not needed
pip install -U langchain-google-genai # needed
python -i lcg05.py
'''

import os
# import langchain, langchain_google
# perplexity:
from langchain_google_genai import ChatGoogleGenerativeAI

#  You MUST set this environment variable.
#  See https://python.langchain.com/docs/integrations/llms/google_genai
google_api_key = os.environ.get('GOOGLE_API_KEY')

# Get a list of LLM models available from Google AI Studio

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.  Please set it with your Google AI Studio API key.")

llm = ChatGoogleGenerativeAI(google_api_key=google_api_key, temperature=0.0)
'done'

'''

(gemini2) dan@hpsda6:~/di/py$ python -i lcg05.py
Traceback (most recent call last):
  File "/media/dan/ssd1/lx/legalexamples/public/python_scripts/lcg05.py", line 32, in <module>
    llm = ChatGoogleGenerativeAI(google_api_key=google_api_key, temperature=0.0)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dan/anaconda3/envs/gemini2/lib/python3.12/site-packages/langchain_core/load/serializable.py", line 125, in __init__
    super().__init__(*args, **kwargs)
  File "/home/dan/anaconda3/envs/gemini2/lib/python3.12/site-packages/pydantic/main.py", line 214, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for ChatGoogleGenerativeAI
model
  Field required [type=missing, input_value={'google_api_key': 'AIzaS...70', 'temperature': 0.0}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
>>> 
(gemini2) dan@hpsda6:~/di/py$
'''
