'''~/lx/lx14/public/py/groq_token_status1.py'''

'''
Helps me understand the status of my token usage of the groq API.

Ref:
|
Hi, I am curious about the groq LLM API.
Please offer ideas and python syntax I can study which will help me access any groq API endpoints.
I want to find an endpoint which serves info about my recent rate of token usage.
I want to find an endpoint which serves info about any token rate limits which might apply to my groq account.
Thanks!
|

Demo:
python -i groq_token_status1.py
'''

import os, requests

HEADERS = {
    "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
    "Content-Type": "application/json"
}

# Example endpoint for a chat completion request
url = "https://api.groq.com/openai/v1/chat/completions"

# Dummy payload for the request
payload = {
    "model": "gemma2-9b-it",
    "messages": [{"role": "user", "content": "Hi, please respond with 'Hello'."}],
    "max_tokens": 50
}

# Make a POST request to the endpoint
response = requests.post(url, headers=HEADERS, json=payload)

# Extract token usage from response headers
if response.status_code == 200:
    print("Some Token Info:")
    print(f"x-ratelimit-remaining-tokens:   {response.headers.get('x-ratelimit-remaining-tokens')}")
    print(f"x-ratelimit-remaining-requests: {response.headers.get('x-ratelimit-remaining-requests')}")
    print(f"x-ratelimit-reset-tokens:       {response.headers.get('x-ratelimit-reset-tokens')}")
    print(response.headers)
    if 'retry-after' in response.headers:
        print(f"retry-after: {response.headers.get('retry-after')}")
else:
    print(f"Error: {response.status_code}, {response.text}")
'''
hallucination:
rate_limit_url = "https://api.groq.com/v1/rate_limits"

rate_limit_response = requests.get(rate_limit_url, headers=HEADERS)

if rate_limit_response.status_code == 200:
    print("Rate Limit Details:")
    print(rate_limit_response.json())  # Assuming the API returns JSON with limit details
else:
    print(f"Error: {rate_limit_response.status_code}, {rate_limit_response.text}")

Error: 404, {"error":{"message":"Unknown request URL: GET /v1/rate_limits. Please check the URL for typos, or see the docs at https://console.groq.com/docs/","type":"invalid_request_error","code":"unknown_url"}}
'''

'done'
