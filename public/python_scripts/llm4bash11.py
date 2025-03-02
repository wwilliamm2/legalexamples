'''~/di/py/llm4bash11.py'''

'''
Sends a prompt to an LLM in Google AI Studio.
The prompt should be inside ~/prompt.txt

Demo:
conda create -n gemini2 python=3.12
conda activate  gemini2
pip install -U "google-genai>=1"

echo 'Please describe how to access a command line token inside argv in Python. Thanks!' > ~/prompt.txt
python ~/di/py/llm4bash11.py ~/prompt.txt
'''

from google import genai
import re, os, sys

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

model_id = "gemini-2.0-pro-exp-02-05"

with open(os.path.expanduser(sys.argv[1]),'r') as pf:
    prompt_s = pf.read()
    
response = client.models.generate_content(model=model_id, contents=[prompt_s])

txt_s = response.candidates[0].content.parts[0].text
print(txt_s)



