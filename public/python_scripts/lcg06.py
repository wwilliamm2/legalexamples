'''~/di/py/lcg06.py'''

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
python -i lcg06.py
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

# fails: llm = ChatGoogleGenerativeAI(google_api_key=google_api_key, temperature=0.0)

# try this:  
llm1 = ChatGoogleGenerativeAI(model="gemini-pro") # works
llm2 = ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05") # works
llm3 = ChatGoogleGenerativeAI(model="nada-model-and-shd-fail") # works but shd fail

'''
llm2.invoke('Describe: "gemini-2.0-pro-exp-02-05"')
(gemini2) dan@hpsda6:~/di/py$ python -i lcg06.py
>>> llm2.invoke('Describe: "gemini-2.0-pro-exp-02-05"')
AIMessage(content='"gemini-2.0-pro-exp-02-05" describes a specific, internal, experimental version of Google\'s Gemini model.  Let\'s break down each part of the name to understand what it likely signifies:\n\n*   **Gemini:** This is the overarching name for Google\'s family of large language models (LLMs), designed to be multimodal (capable of handling text, images, audio, and video). Think of it like the "brand name."\n\n*   **2.0:** This strongly suggests a major version number.  It indicates a significant upgrade or iteration from a previous version (presumably "Gemini 1.0" or "Gemini 1.5").  Version 2.0 likely represents substantial improvements in capabilities, architecture, training data, or a combination of these factors.  It\'s a new *generation* of the model.\n\n*   **Pro:** This is a common tier designation, indicating a more powerful and capable version of the model compared to a potential "base" or "standard" version.  "Pro" models typically have:\n    *   **Larger context windows:** They can process and remember more information in a single conversation or prompt.\n    *   **Higher accuracy and reasoning abilities:** They are better at complex tasks, understanding nuances, and generating more coherent and relevant responses.\n    *   **More advanced features:** They might have access to specialized tools or capabilities not available in lower tiers.\n    *   **Faster response times:** Though this can depend on infrastructure, "Pro" models are often optimized for speed.\n\n*   **exp:** This is short for "experimental."  This is the most crucial part of the name.  It signifies that this is *not* a publicly released, stable version of the model.  It\'s an internal build used for testing, research, and development.  Experimental models are often:\n    *   **Unstable:** They might exhibit unexpected behavior, generate nonsensical outputs, or even crash.\n    *   **Unpolished:** Their responses might be less refined or lack the safety guardrails of a released model.\n    *   **Used for A/B testing:** Different experimental versions might be compared to each other to evaluate changes.\n    *   **Subject to frequent changes:** They are constantly being updated and modified as developers iterate.\n    *   **Not representative of the final product:** The features and performance of an experimental model may differ significantly from what eventually gets released.\n\n*   **02-05:** This is likely a date code, indicating the build date of this specific experimental version (February 5th, likely of the current or a recent year). This helps track different iterations of the experimental model. It\'s a way for Google\'s internal teams to distinguish between various builds during the development process.\n\n**In Summary:**\n\n"gemini-2.0-pro-exp-02-05" refers to a specific, internal, experimental build of a more powerful ("Pro") version of Google\'s second-generation Gemini large language model, built on February 5th. It\'s a testing version, not intended for public use, and likely exhibits characteristics typical of experimental software – potential instability, unrefined outputs, and frequent changes.  It\'s a snapshot of the ongoing development process towards a future, more stable Gemini release. It\'s *not* something a regular user would interact with directly.', additional_kwargs={}, response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'safety_ratings': []}, id='run-55958f2f-3623-4dbc-a1fc-013e22c301e9-0', usage_metadata={'input_tokens': 20, 'output_tokens': 722, 'total_tokens': 742, 'input_token_details': {'cache_read': 0}})
>>>
'''
