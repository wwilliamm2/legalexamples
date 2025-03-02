'''~/di/py/llm4bash12.py'''

'''
Sends a prompt to an LLM in Google AI Studio.
The prompt should be inside ~/prompt.txt

Demo:
conda create -n gemini2 python=3.12
conda activate  gemini2
pip install -U "google-genai>=1"

echo 'Please describe how to access a command line token inside argv in Python. Thanks!' > ~/prompt.txt
python ~/di/py/llm4bash12.py ~/prompt.txt
'''

from google import genai
import re, os, sys

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

model_id = "gemini-2.0-pro-exp-02-05"

with open(os.path.expanduser(sys.argv[1]),'r') as pf:
    prompt_s = pf.read()
    
response = client.models.generate_content(model=model_id, contents=[prompt_s])

# txt_s = response.candidates[0].content.parts[0].text
txt_s = response.text
print(txt_s)

# Define model and pricing
model_id = "gemini-2.0-pro-exp-02-05"
INPUT_PRICE_PER_1K_TOKENS = 0.0012
OUTPUT_PRICE_PER_1K_TOKENS = 0.005

def calculate_cost(response):
    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count
    output_tokens = usage.candidates_token_count
    total_tokens = usage.total_token_count

    input_cost = (prompt_tokens / 1000) * INPUT_PRICE_PER_1K_TOKENS
    output_cost = (output_tokens / 1000) * OUTPUT_PRICE_PER_1K_TOKENS
    total_cost = input_cost + output_cost

    return total_cost, total_tokens

cost, tokens = calculate_cost(response)

print(f"This demo cost ${cost:.6f} to run because it made 1 request to the LLM '{model_id}' and used {tokens} tokens.")

