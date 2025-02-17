'''~/di/py/lcg02.py'''

'''
Helps me study this Python package: langchain-google

Ref:
https://github.com/langchain-ai/langchain
https://github.com/langchain-ai/langchain-google

Demo:
conda create -n gemini2 python=3.12
conda activate gemini2
pip install langchain langchain-google
python -i lcg02.py
'''

import os
import langchain, langchain-google

google_api_key = os.environ(['GOOGLE_API_KEY'])

# Get a list of LLM models available from Google AI Studio

# chat.langchain.com + gemini pro ans 1:

llm_models = langchain-google.list_llm_models(google_api_key)
for model in llm_models:
    print(model)
'''
(gemini2) dan@hpsda6:~/di/py$ 
(gemini2) dan@hpsda6:~/di/py$ python -i lcg02.py
  File "/media/dan/ssd1/lx/legalexamples/public/python_scripts/lcg02.py", line 18
    import langchain, langchain-google
                               ^
SyntaxError: invalid syntax
>>>
'''
