'''~/lx/lx14/public/py/schmid14.py'''

'''
Helps me ask Gemini LLM for a response to a prompt combined with a PDF file.
Output should be plain text rather than JSON.

Demo:
conda activate gemini1
pip install "google-genai>=1"
python -i schmid14.py
'''

import os
from google import genai

# Create a client
api_key = os.environ["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)

model_id =  "gemini-2.0-flash"

invoice_png = client.files.upload(file="invoice.png", config={'display_name': 'invoice'})

file_size = client.models.count_tokens(model=model_id,contents=invoice_png)
print(f'File: {invoice_png.display_name} equals to {file_size.total_tokens} tokens')

prompt = 'Please extract all information you see in the invoice so I can also see it. Thanks!'

response = client.models.generate_content(
    model=model_id,
    contents=[invoice_png, prompt]
)

try:
    # Extract and print only the "text" field from the response
    if response.candidates:
        response.candidates[0].content.parts[0].text
        print(response.candidates[0].content.parts[0].text)
except Exception as myexp:
    print('I see a problem due to: ', str(myexp))
