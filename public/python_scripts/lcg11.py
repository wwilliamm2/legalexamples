'''lcg11.py'''

'''
Simple demo of passing a prompt and pdf file to Gemini LLM,
then get the response and pass that response to a langchain parser.

Demo:
conda create -n gemini2 python=3.12
conda activate  gemini2
pip install -U "google-genai>=1"
pip install -U langchain-core

python -i lcg11.py
'''

from google import genai
import langchain, langchain_core, os

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

prompt_s = '''Please study information in the attached file and then summarize it.'''

fn_s = 'invoice.pdf' # attached file

doc_pdf = client.files.upload(file=fn_s, config={'display_name': fn_s})

model_id = "gemini-2.0-pro-exp-02-05"

response = client.models.generate_content(model=model_id, contents=[doc_pdf, prompt_s])

'''
I see that the response looks like this:

>>> response
GenerateContentResponse(candidates=[Candidate(content=Content(parts=[Part(video_metadata=None, thought=None, code_execution_result=None, executable_code=None, file_data=None, function_call=None, function_response=None, inline_data=None, text="Here's a summary of the invoice (number 27301261, dated 10/09/2012) provided:\n\n*   **Seller:** Williams LLC, located in West Alexandria, AR.\n*   **Client:** Hernandez-Anderson, located in South Ronaldbury, AZ.\n*   **Items:** The invoice details seven different clothing items, mostly dresses, from brands like Lilly Pulitzer, Erin Fertherston, Sequence, Fire Los Angeles, Eileen Fisher, Lularoe, and J.Crew. The quantities range from 1 to 5, the price for each item is also detailed.\n*   **Summary:**\n    *   **Net Worth:** $494.96\n    *   **VAT (10%):** $49.50\n    *   **Gross Worth (Total):** $544.46\n\nIn essence, Hernandez-Anderson owes Williams LLC a total of $544.46 for the purchase of various clothing items, inclusive of a 10% Value Added Tax.\n")], role='model'), citation_metadata=None, finish_message=None, token_count=None, avg_logprobs=None, finish_reason=<FinishReason.STOP: 'STOP'>, grounding_metadata=None, index=0, logprobs_result=None, safety_ratings=None)], model_version='gemini-2.0-pro-exp-02-05', prompt_feedback=None, usage_metadata=GenerateContentResponseUsageMetadata(cached_content_token_count=None, candidates_token_count=232, prompt_token_count=834, total_token_count=1066), automatic_function_calling_history=[], parsed=None)
>>>
'''

# Pass the response to a langchain parser so that the text portion of the response is extracted from the response object.

