'''lcg11.py'''

'''
Simple demo of passing a prompt and pdf file to Gemini LLM,
then get the response and pass that response to langchain string output parser.

Demo:
conda create -n gemini2 python=3.12
conda activate  gemini2
pip install -U "google-genai>=1"
pip install -U langchain

python -i lcg11.py
'''

from google import genai
import langchain

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

prompt_s = '''Please study information in the attached file and then summarize it.'''

fn_s = 'invoice.pdf' # attached file

doc_pdf = client.files.upload(file=fn_s, config={'display_name': fn_s})

model_id = "gemini-2.0-pro-exp-02-05"

response = client.models.generate_content(model=model_id, contents=[doc_pdf, prompt_s])
