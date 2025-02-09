'''~/lx/lx14/public/py/schmid13.py'''

'''
Helps me understand a blog post about using Gemini to read PDF files.

Ref:
https://www.philschmid.de/gemini-pdf-to-data

Demo:

wget https://storage.googleapis.com/generativeai-downloads/data/pdf_structured_outputs/invoice.pdf

conda activate gemini1
pip install "google-genai>=1"
python -i schmid13.py
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

# Define a Pydantic model
# Use the Field class to add a description and default value
from pydantic import BaseModel, Field

class InvoiceInfo(BaseModel):
    the_info: str = Field(description="All information extracted from the invoice")

prompt = 'Please extract all information you see in the invoice so I can also see it. Thanks!'

response = client.models.generate_content(
    model=model_id,
    contents=[invoice_png, prompt],
    config={
        'response_mime_type': 'application/json',
        'response_schema': InvoiceInfo
    }
)

invoice_data: InvoiceInfo = response.parsed

print(f"Extracted information: {invoice_data.the_info}")

'done'

