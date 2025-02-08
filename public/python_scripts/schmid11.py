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
 
