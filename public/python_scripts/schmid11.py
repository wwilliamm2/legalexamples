'''~/lx/lx14/public/py/schmid11.py'''

'''
Helps me understand a blog post about using Gemini to read PDF files.

Ref:
https://www.philschmid.de/gemini-pdf-to-data

Demo:

wget -https://storage.googleapis.com/generativeai-downloads/data/pdf_structured_outputs/handwriting_form.pdf

conda activate gemini1
pip install "google-genai>=1"
python -i schmid11.py
'''

import os
from google import genai
'''
>>> genai
<module 'google.genai' from '/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/genai/__init__.py'>
>>>
'''

# Create a client
api_key = os.environ["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)

model_id =  "gemini-2.0-flash" # or "gemini-2.0-flash-lite-preview-02-05"  , "gemini-2.0-pro-exp-02-05"

from pydantic import BaseModel, Field

class Form(BaseModel):
    """Extract the form number, fiscal start date, fiscal end date, and the plan liabilities beginning of the year and end of the year."""
    form_number: str = Field(description="The Form Number")
    start_date: str = Field(description="Effective Date")
    beginning_of_year: float = Field(description="The plan liabilities beginning of the year")
    end_of_year: float = Field(description="The plan liabilities end of the year")

def extract_structured_data(file_path: str, model: BaseModel):
    # Upload the file to the File API
    file = client.files.upload(file=file_path, config={'display_name': file_path.split('/')[-1].split('.')[0]})
    # Generate a structured response using the Gemini API
    prompt = f"Extract the structured data from the following PDF file"
    response = client.models.generate_content(model=model_id, contents=[prompt, file], config={'response_mime_type': 'application/json', 'response_schema': model})
    # Convert the response to the pydantic model and return it
    return response.parsed

result = extract_structured_data("handwriting_form.pdf", Form)
'''
>>> result
Form(form_number='5500-EZ', start_date='02/05/.2022', beginning_of_year=40000.0, end_of_year=55000.0)
>>>
'''

print(f'Extracted Form Number: {result.form_number} with start date {result.start_date}. \nPlan liabilities beginning of the year {result.beginning_of_year} and end of the year {result.end_of_year}')
'''
>>> print(f'Extracted Form Number: {result.form_number} with start date {result.start_date}. \nPlan liabilities beginning of the year {result.beginning_of_year} and end of the year {result.end_of_year}')

Extracted Form Number: 5500-EZ with start date 02/05/.2022. 
Plan liabilities beginning of the year 40000.0 and end of the year 55000.0
>>> >>>
'''
