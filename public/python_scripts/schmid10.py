'''~/lx/lx14/public/py/schmid10.py'''

'''
Helps me understand a blog post about using Gemini to read PDF files.

Ref:
https://www.philschmid.de/gemini-pdf-to-data

Demo:

wget -https://storage.googleapis.com/generativeai-downloads/data/pdf_structured_outputs/handwriting_form.pdf
wget https://storage.googleapis.com/generativeai-downloads/data/pdf_structured_outputs/invoice.pdf

conda activate gemini1
pip install "google-genai>=1"
python -i schmid10.py
'''

import os
from google import genai

# Create a client
api_key = os.environ["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)

model_id =  "gemini-2.0-flash" # or "gemini-2.0-flash-lite-preview-02-05"  , "gemini-2.0-pro-exp-02-05"

invoice_pdf = client.files.upload(file="invoice.pdf", config={'display_name': 'invoice'})

file_size = client.models.count_tokens(model=model_id,contents=invoice_pdf)
print(f'File: {invoice_pdf.display_name} equals to {file_size.total_tokens} tokens')


from pydantic import BaseModel, Field
 
# Define a Pydantic model
# Use the Field class to add a description and default value to provide more context to the model
class Topic(BaseModel):
    name: str = Field(description="The name of the topic")
 
class Person(BaseModel):
    first_name: str = Field(description="The first name of the person")
    last_name: str = Field(description="The last name of the person")
    age: int = Field(description="The age of the person, if not provided please return 0")
    work_topics: list[Topic] = Field(description="The fields of interest of the person, if not provided please return an empty list")


# Define the prompt
prompt = "Philipp Schmid is a Senior AI Developer Relations Engineer at Google DeepMind working on Gemini, Gemma with the mission to help every developer to build and benefit from AI in a responsible way.  "
 
# Generate a response using the Person model
response = client.models.generate_content(model=model_id, contents=prompt, config={'response_mime_type': 'application/json', 'response_schema': Person})

# print the response as a json string
print(response.text)
 
# sdk automatically converts the response to the pydantic model
philipp: Person = response.parsed
 
# access an attribute of the json response
print(f"First name is {philipp.first_name}")

'''
4. Extract Structured data from PDFs using Gemini 2.0

Now, let's combine the File API and structured output to extract information from our PDFs. You can create a simple method that accepts a local file path and a pydantic model and return the structured data for us. The method will:

    Upload the file to the File API
    Generate a structured response using the Gemini API
    Convert the response to the pydantic model and return it
'''


def extract_structured_data(file_path: str, model: BaseModel):
    # Upload the file to the File API
    file = client.files.upload(file=file_path, config={'display_name': file_path.split('/')[-1].split('.')[0]})
    # Generate a structured response using the Gemini API
    prompt = f"Extract the structured data from the following PDF file"
    response = client.models.generate_content(model=model_id, contents=[prompt, file], config={'response_mime_type': 'application/json', 'response_schema': model})
    # Convert the response to the pydantic model and return it
    return response.parsed

'''

In our Example every PDF is a different to each other. So you want to define unique Pydantic models for each PDF to show the performance of the Gemini 2.0. If you have very similar PDFs and want to extract the same information you can use the same model for all of them.

    Invoice.pdf : Extract the invoice number, date and all list items with description, quantity and gross worth and the total gross worth
    
    handwriting_form.pdf : Extract the form number, plan start date and the plan liabilities beginning of the year and end of the year

Note: Using Pydantic features you can add more context to the model to make it more accurate as well as some validation to the data. Adding a comprehensive description can significantly improve the performance of the model. Libraries like instructor added automatic retries based on validation errors, which can be a great help, but come at the cost of additional requests.

https://python.useinstructor.com/

Instructor makes it easy to get structured data like JSON from
LLMs like GPT-3.5, GPT-4, GPT-4-Vision,
and open-source models including Mistral/Mixtral, Ollama, and llama-cpp-python.

'''

from pydantic import BaseModel, Field
 
class Item(BaseModel):
    description: str = Field(description="The description of the item")
    quantity: float = Field(description="The Qty of the item")
    gross_worth: float = Field(description="The gross worth of the item")
 
class Invoice(BaseModel):
    """Extract the invoice number, date and all list items with description, quantity and gross worth and the total gross worth."""
    invoice_number: str = Field(description="The invoice number e.g. 1234567890")
    date: str = Field(description="The date of the invoice e.g. 2024-01-01")
    items: list[Item] = Field(description="The list of items with description, quantity and gross worth")
    total_gross_worth: float = Field(description="The total gross worth of the invoice")
 
 
result = extract_structured_data("invoice.pdf", Invoice)
print(type(result))
print(f"Extracted Invoice: {result.invoice_number} on {result.date} with total gross worth {result.total_gross_worth}")
for item in result.items:
    print(f"Item: {item.description} with quantity {item.quantity} and gross worth {item.gross_worth}")

'''
ini1) dan@hpsda6:~/lx/lx14/public/py$ 
(gemini1) dan@hpsda6:~/lx/lx14/public/py$ python -i schmid10.py
File: invoice equals to 821 tokens
{
  "age": 0,
  "first_name": "Philipp",
  "last_name": "Schmid",
  "work_topics": [
    {
      "name": "AI"
    },
    {
      "name": "Gemini"
    },
    {
      "name": "Gemma"
    }
  ]
}
First name is Philipp
<class '__main__.Invoice'>
Extracted Invoice: 27301261 on 10/09/2012 with total gross worth 544.46
Item: Lilly Pulitzer dress Size 2 with quantity 5.0 and gross worth 247.5
Item: New ERIN Erin Fertherston Straight Dress White Sequence Lining Sleeveless SZ 10 with quantity 1.0 and gross worth 65.99
Item: Sequence dress Size Small with quantity 3.0 and gross worth 115.5
Item: fire los angeles dress Medium with quantity 3.0 and gross worth 21.45
Item: Eileen Fisher Women's Long Sleeve Fleece Lined Front Pockets Dress XS Gray with quantity 3.0 and gross worth 52.77
Item: Lularoe Nicole Dress Size Small Light Solid Grey/ White Ringer Tee Trim with quantity 2.0 and gross worth 8.25
Item: J.Crew Collection Black & White sweater Dress sz S with quantity 1.0 and gross worth 33.0
>>>
'''

