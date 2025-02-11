'''~/lx/lx14/public/py/gemini_flash_text_from_png16.py'''

'''
Uses LLM to generate text from png files.

Demo:
conda activate gemini1
python -i gemini_flash_text_from_png16.py
'''

print('Busy ...')

import datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

from google import genai

llm_s_l = ['gemini-2.0-flash-lite-preview','gemini-2.0-flash-exp']

model_id = llm_s_l[0]

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

prompt_s = '''Please study information from my file and then extract (verbatim) all text you see in it.
My file is an image of a single page in California legal document filed in a county court.
Please preserve the format and placement of all the words, sentenances, and paragraphs.
If you see text which looks like a paragraph, please ensure that the text you extract places a tab before the paragraph.
If the image contains text in a single rectangle, please use Markdown to show the text inside a single-cell table.
If the image contains a table with text in the cells, please use HTML (or Markdown or Haml or YAML) sytax to markup that table and the text in the table's cells.
The td elements will separate cell-text well.
The td elements will prevent text from one cell mixing with text in another cell.
Outside of tables,
I want you to preserve the text format and avoid using HTML because I want your extracted and verbatim text
to be comprehensive for an attorney who might be confused by text marked-up by HTML (or Markdown or Haml or YAML).
Thanks!
'''

fn_s_l = sorted(glob.glob('/media/dan/ssd2/tmp/scscourt/pdfs/2023_0916_2245_33_dept10_tues/2*png'))[:8]

# fn_s = fn_s_l[0]

for fn_s in fn_s_l:
    try:
        fn_txt_s = f'{fn_s}.txt'
        if os.path.exists(fn_txt_s):
            print('File ready already:', fn_txt_s)
        else:
            print('Working on: ', fn_txt_s)
            doc_png = client.files.upload(file=fn_s, config={'display_name': fn_s})
            file_size = client.models.count_tokens(model=model_id,contents=doc_png)
            print(f'File: {doc_png.display_name} equals to {file_size.total_tokens} tokens')
            response = client.models.generate_content(model=model_id, contents=[doc_png, prompt_s])
            time.sleep(2) # Throttle my calls to avoid trouble with API.            
            # Extract and print only the "text" field from the response
            if response.candidates:
                with open(fn_txt_s, 'w') as txtf:
                    txtf.write(response.candidates[0].content.parts[0].text)
    except Exception as myexp:
        print(f'I see a problem with {fn_s}\ndue to: ', str(myexp))
        with open(fn_txt_s, 'w') as txtf:
            # Salvage what I can...
            txtf.write(f'{str(myexp)}\n{str(response)}')

'done'
