'''~/lx/lx14/public/py/gemini_flash_text_from_png15.py'''

'''
Uses LLM to generate text from png files.

Demo:
conda activate gemini1
python -i gemini_flash_text_from_png15.py
'''

from google import genai

# Check Google AI Studio API key
import os
os.environ["GOOGLE_API_KEY"]


print('Busy ...')
import datetime, glob, inspect, json, operator, re, shutil, sys, time, typing


# model_id =  "gemini-2.0-flash"

llm_s_l = ['gemini-2.0-flash-lite-preview','gemini-2.0-flash-exp']

model_id = llm_s_l[0]

fn_s_l = sorted(glob.glob('/media/dan/ssd2/tmp/scscourt/pdfs/2023_0916_2245_33_dept10_tues/2*png'))

api_key = os.environ["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)


fn_s = fn_s_l[0]
tr_png = client.files.upload(file=fn_s, config={'display_name': 'TR page'})

file_size = client.models.count_tokens(model=model_id,contents=tr_png)
print(f'File: {tr_png.display_name} equals to {file_size.total_tokens} tokens')

# create prompt list of tpls acting as messages
prompt_s = '''Please study the png file and then extract all text you see in it.
Please preserve the format and placement of all the words, sentenances, and paragraphs.
'''

response = client.models.generate_content(
    model=model_id,
    contents=[tr_png, prompt_s]
)

try:
    # Extract and print only the "text" field from the response
    if response.candidates:
        response.candidates[0].content.parts[0].text
        print(response.candidates[0].content.parts[0].text)
except Exception as myexp:
    print('I see a problem due to: ', str(myexp))
'''
(gemini1) dan@hpsda6:~/lx/lx14/public/py$ python -i gemini_flash_text_from_png15.py
Busy ...
File: TR page equals to 259 tokens
Here's the text from the image, preserving format and placement:

SUPERIOR COURT, STATE OF CALIFORNIA
COUNTY OF SANTA CLARA
Department 10
Honorable Frederick S. Chung
Farris Bryant, Courtroom Clerk (covering for Rachel Tien)
191 North First Street, San Jose, CA 95113
Telephone: 408-882-2210

DATE: September 12, 2023    TIME: 9:00 A.M.

To contest the ruling, call (408) 883-6856 before 4:00 P.M.
Make sure to let the other side know before 4:00 P.M. that you plan to contest the ruling,
in accordance with California Rule of Court 3.1308(a)(1) and Local Rule 8.E.

The courthouse is open: Department 10 is now fully open for in-person hearings, as of April 18, 2023.
The court strongly prefers in-person appearances for all contested law-and-motion matters. For all other
hearings (e.g., case management conferences), the court strongly prefers either in-person or video
appearances. Audio-only appearances are permitted but disfavored, as they cause significant disruptions
and delays to the proceedings. Please use telephone-only appearances as a last resort.
CourtCall is no longer available: Department 10 uses Microsoft Teams for remote hearings. Please
click on this link if you need to appear remotely, and then scroll down to click the link for Department
10: https://www.sccourt.org/general_info/ra_teams/video_hearings_teams.shtml.
Recording is prohibited: As a reminder, most hearings are open to the public, but state and local court
rules prohibit recording of court proceedings without a court order. This prohibition applies to both
in-person and remote appearances.
Court reporters: Unfortunately, the court is no longer able to provide official court reporters for civil
proceedings (as of July 24, 2017). If any party wishes to have a court reporter, the appropriate form must
be submitted. See https://www.sccourt.org/general_info/court_reporters.shtml.

1

>>>
'''
