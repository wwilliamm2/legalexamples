'''~/di/py/lcg04.py'''

'''
Helps me study this Python package: langchain-google

Ref:
https://github.com/langchain-ai/langchain
https://github.com/langchain-ai/langchain-google

Demo:
conda create -n gemini2 python=3.12
conda activate gemini2
pip install langchain langchain-google
python -i lcg04.py
'''

import os
# import langchain, langchain_google
# perplexity:
from langchain_google_genai import ChatGoogleGenerativeAI

#  You MUST set this environment variable.
#  See https://python.langchain.com/docs/integrations/llms/google_genai
google_api_key = os.environ.get('GOOGLE_API_KEY')

# Get a list of LLM models available from Google AI Studio

'''
gpt, Please help me debug this Python exception:
ModuleNotFoundError: No module named 'langchain_google_genai'
Thanks!

Ans:
pip install -U langchain-google-genai

'''

# ~/anaconda3/envs/gemini2/lib/python3.12/site-packages/langchain_google_genai/__init__.py

'''
"""**LangChain Google Generative AI Integration**

This module integrates Google's Generative AI models, specifically the Gemini series, with the LangChain framework. It provides classes for interacting with chat models and generating embeddings, leveraging Google's advanced AI capabilities.

**Chat Models**

The `ChatGoogleGenerativeAI` class is the primary interface for interacting with Google's Gemini chat models. It allows users to send and receive messages using a specified Gemini model, suitable for various conversational AI applications.

**LLMs**

The `GoogleGenerativeAI` class is the primary interface for interacting with Google's Gemini LLMs. It allows users to generate text using a specified Gemini model.

**Embeddings**

The `GoogleGenerativeAIEmbeddings` class provides functionalities to generate embeddings using Google's models.
These embeddings can be used for a range of NLP tasks, including semantic analysis, similarity comparisons, and more.
**Installation**

To install the package, use pip:

```python
pip install -U langchain-google-genai
```
## Using Chat Models

After setting up your environment with the required API key, you can interact with the Google Gemini models.

```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
llm.invoke("Sing a ballad of LangChain.")
```

## Using LLMs

The package also supports generating text with Google's models.

```python
from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(model="gemini-pro")
llm.invoke("Once upon a time, a library called LangChain")
```

'''
