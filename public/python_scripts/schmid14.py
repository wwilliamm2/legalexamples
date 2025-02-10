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
'''
(gemini1) dan@hpsda6:~/lx/lx14/public/py$ python -i schmid14.py
File: invoice equals to 259 tokens
Here is the extracted information from the invoice:

**Invoice Information:**

*   Invoice no: 27301261
*   Date of issue: 10/09/2012

**Seller:**

*   Williams LLC
*   72074 Taylor Plains Suite 342
*   West Alexandria, AR 97978
*   Tax Id: 922-88-2832
*   IBAN: GB70FTNR64199348221780

**Client:**

*   Hernandez-Anderson
*   084 Carter Lane Apt. 846
*   South Ronaldbury, AZ 91030
*   Tax Id: 959-74-5868

**Items:**

| No. | Description                                                                             | Qty   | UM    | Net price | Net worth | VAT [%] | Gross worth |
|-----|-----------------------------------------------------------------------------------------|-------|-------|-----------|-----------|---------|-------------|
| 1.  | Lilly Pulitzer dress Size 2                                                             | 5,00  | each  | 45,00     | 225,00    | 10%     | 247,50      |
| 2.  | New ERIN Erin Fertherston Straight Dress White Sequence Lining Sleeveless SZ 10          | 1,00  | each  | 59,99     | 59,99     | 10%     | 65,99       |
| 3.  | Sequence dress Size Small                                                               | 3,00  | each  | 35,00     | 105,00    | 10%     | 115.50      |
| 4.  | fire los angeles dress Medium                                                            | 3,00  | each  | 6,50      | 19.50     | 10%     | 21,45       |
| 5.  | Fileen Fisher Women's I ong Sleeve Fleece Lined Front Pockets Dress XS Gray           | 3,00  | each  | 15,99     | 47,97     | 10%     | 57,77       |
| 6.  | Lularoe Nicole Dress Size Small Light Solid Grey/White Ringer Tee Trim                     | 2,00  | each  | 3,75      | 7,50      | 10%     | 8,25        |
| 7.  | J.Crew Collection Black & White sweater Dress sz S                                      | 1,00  | each  | 30,00     | 30,00     | 10%     | 33,00       |

**Summary:**

| VAT [%] | Net worth | VAT    | Gross worth |
|---------|-----------|--------|-------------|
| 10%     | 494.96    | 49.50  | 544,46      |
| Total   | $ 494,96   | $ 49,50 | $ 544,46     |
>>> 
(gemini1) dan@hpsda6:~/lx/lx14/public/py$
'''

