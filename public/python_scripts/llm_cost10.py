'''~/di/py/llm_cost10.py'''

'''
Helps me learn how to extract information from the request object which I can use to calculate the cost of a request.
I assume that the cost is a function of 4 variables:
request_count
tokens_in
tokens_out
llm_name

Demo:
conda create -n gemini2 python=3.12
conda activate  gemini2
pip install -U "google-genai>=1"

python llm_cost10.py
'''

from google import genai
import re, os

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

model_id = "gemini-2.0-pro-exp-02-05"

prompt_s = 'Gemini, please compare oxygen to nitrogen for a 14 year old student.'

response = client.models.generate_content(model=model_id, contents=[prompt_s])

print(response)
