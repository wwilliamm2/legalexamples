'''
~/lx/lx14/public/py/search_grounding01.py
'''

'''
Helps me study Search Grounding as describe at this URL:

https://github.com/google-gemini/generative-ai-python/blob/8849d4f46010ce4ae68243c4f8a44a138b56598f/README.md#search-grounding

Demo:
pip install pip install "google-genai>=1"

python -i search_grounding01.py
'''

from google import genai
from google.genai import types
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='What is the Google stock price?',
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch()
            )
        ]
    )
)

'''
>>> response
GenerateContentResponse(candidates=[Candidate(content=Content(parts=[Part(video_metadata=None, thought=None, code_execution_result=None, executable_code=None, file_data=None, function_call=None, function_response=None, inline_data=None, text='As of February 12, 2025, the price of Google (Alphabet Inc.) stocks are as follows:\n\n*   **GOOG (Class C):** \\$185.43\n*   **GOOGL (Class A):** \\$186.47\n\n')], role='model'), citation_metadata=None, finish_message=None, token_count=None, avg_logprobs=None, finish_reason=<FinishReason.STOP: 'STOP'>, g .......

gpt, Please write a simple re regexp demo in Python to match the string:
r"text='As of February 12, goodbye.'"
'''

import re

pattern_r = r'text='

re_m = re.match(pattern_r, str(response))

'fails'


"gpt, please write a reg-exp to match this ugly string: `text=\'As of February n\'`"

pattern_r = r"text=\\'As of February n\\'"

'fails too'

# works:
response.candidates[0].content.parts[0].text

'done'
