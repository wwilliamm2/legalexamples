'''~/di/py/llm_cost11.py'''


'''
Helps me learn how to extract information from the request object which I can use to calculate the cost of a request.
I assume that the cost is a function of 4 variables:
request_count
tokens_in
tokens_out
llm_name

Demo:
conda create -n gemini2 python=3.12
conda activate  gemini2
pip install -U "google-genai>=1"

python llm_cost11.py
'''

import os
from google import genai

# Set up the client
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# Define model and pricing
model_id = "gemini-2.0-pro-exp-02-05"
INPUT_PRICE_PER_1K_TOKENS = 0.0012
OUTPUT_PRICE_PER_1K_TOKENS = 0.005


def calculate_cost(response):
    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count
    output_tokens = usage.candidates_token_count
    total_tokens = usage.total_token_count

    input_cost = (prompt_tokens / 1000) * INPUT_PRICE_PER_1K_TOKENS
    output_cost = (output_tokens / 1000) * OUTPUT_PRICE_PER_1K_TOKENS
    total_cost = input_cost + output_cost

    return total_cost, total_tokens

prompt_s = 'Gemini, please compare oxygen to nitrogen for a 14 year old student.'

response = client.models.generate_content(model=model_id, contents=[prompt_s])

cost, tokens = calculate_cost(response)

print(f"This demo cost ${cost:.6f} to run because it made 1 request to the LLM '{model_id}' and used {tokens} tokens.")
print(response.text)


'''
This script does the following:

1. Defines the pricing constants for input and output tokens.
2. Creates a `calculate_cost` function that uses the `usage_metadata` from the response to calculate the cost.
3. Generates the content using the Gemini model.
4. Calculates the cost and token usage.
5. Prints a cost summary and the generated response.

Note that the pricing used in this example is based on the Gemini 1.5 Pro model, as the exact pricing for Gemini 2.0 Pro was not available in the search results. You should replace these values with the correct pricing for the Gemini 2.0 Pro model when it becomes available[1].

Also, keep in mind that pricing may change over time, so it's a good practice to fetch the latest pricing information programmatically if possible, or update the constants regularly to ensure accuracy.

This enhanced script provides a clear demonstration of how to calculate the cost of each request to the Gemini LLM, fulfilling your requirement for a cost calculation demo.

Citations:
[1] https://cloud.google.com/vertex-ai/generative-ai/pricing
[2] https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal
[3] https://yourgpt.ai/tools/openai-and-other-llm-api-pricing-calculator
[4] https://www.youtube.com/watch?v=L-oVni1HJAA
[5] https://docsbot.ai/tools/gpt-openai-api-pricing-calculator
[6] https://discuss.ai.google.dev/t/how-can-i-code-with-python-in-ai-of-google-ai-studio/45342
[7] https://www.googlecloudcommunity.com/gc/Gemini-Code-Assist/Python-function-to-calculate-the-cost-of-each-conversation-with/m-p/826397
[8] https://simonw.substack.com/p/video-scraping-using-google-gemini

---
Answer from Perplexity: https://www.perplexity.ai/search/hi-i-have-a-python-script-llm-inICiX9oQxm5luBTtDesgw?utm_source=copy_output

'''
