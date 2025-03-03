'''~/lx/lx14/public/py/llm_groq4bash15.py'''

'''
Sends a request to groq using requests package instead of groq package.

Demo:
python ~/lx/lx14/public/py/llm_groq4bash15.py ~/prompt.txt gemma2-9b-it
'''

import os, requests

with open('/home/dan/prompt.txt','r') as pf:
    prompt_s = pf.read()
HEADERS = {
    "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
    "Content-Type": "application/json"
}
payload = {
    "model": "gemma2-9b-it",
    "messages": [{"role": "user", "content": prompt_s}],
    "max_tokens": 50
}
url = "https://api.groq.com/openai/v1/chat/completions"
response = requests.post(url, headers=HEADERS, json=payload)
print(response)
