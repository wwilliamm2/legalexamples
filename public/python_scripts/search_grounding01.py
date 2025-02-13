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

'''
