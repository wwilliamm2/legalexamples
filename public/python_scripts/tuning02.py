'''~/lx/lx14/public/py/tuning02.py'''

'''
Helps me study tuning of a gemini model.

Ref:
https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/python.ipynb

Old-way vs new-way:
https://github.com/google-gemini/generative-ai-python/blob/8849d4f46010ce4ae68243c4f8a44a138b56598f/README.md#L30-L31

Demo:
pip install google-generativeai # the old way
python -i tuning02.py
'''

import google.generativeai as genai # old way

'''
You can check you existing tuned models with the genai.list_tuned_model method.

for i, m in zip(range(5), genai.list_tuned_models()):
  print(m.name)
'''

list(genai.list_tuned_models())

'''
To create a tuned model,
you need to pass your dataset to the model in the genai.create_tuned_model method.
You can do this be directly defining the input and output values in the
call or importing from a file into a dataframe to pass to the method.

For this example, you will tune a model to generate the next number in the sequence.
'''

[mmodel.name for mmodel in genai.list_models() if 'tun' in mmodel.name]

'''
['models/gemini-1.5-flash-001-tuning']
>>>
'''

base_model_l = [mmodel for mmodel in genai.list_models() if 'tun' in mmodel.name]
base_model = base_model_l[0]
'''
[Model(name='models/gemini-1.5-flash-001-tuning',
      base_model_id='',
      version='001',
      display_name='Gemini 1.5 Flash 001 Tuning',
      description=('Version of Gemini 1.5 Flash that supports tuning, our fast and versatile '
                   'multimodal model for scaling across diverse tasks, released in May of 2024.'),
      input_token_limit=16384,
      output_token_limit=8192,
      supported_generation_methods=['generateContent', 'countTokens', 'createTunedModel'],
      temperature=1.0,
      max_temperature=2.0,
      top_p=0.95,
      top_k=64)]
>>>
'''

import random

name = f'generate-num-{random.randint(0,10000)}'

'generate-num-1213'

base_model.name

operation = genai.create_tuned_model(
    # You can use a tuned model here too. Set `source_model="tunedModels/..."`
    source_model=base_model.name,
    training_data=[
        {
             'text_input': '1',
             'output': '2',
        },{
             'text_input': '3',
             'output': '4',
        },{
             'text_input': '-3',
             'output': '-2',
        },{
             'text_input': 'twenty two',
             'output': 'twenty three',
        },{
             'text_input': 'two hundred',
             'output': 'two hundred one',
        },{
             'text_input': 'ninety nine',
             'output': 'one hundred',
        },{
             'text_input': '8',
             'output': '9',
        },{
             'text_input': '-98',
             'output': '-97',
        },{
             'text_input': '1,000',
             'output': '1,001',
        },{
             'text_input': '10,100,000',
             'output': '10,100,001',
        },{
             'text_input': 'thirteen',
             'output': 'fourteen',
        },{
             'text_input': 'eighty',
             'output': 'eighty one',
        },{
             'text_input': 'one',
             'output': 'two',
        },{
             'text_input': 'three',
             'output': 'four',
        },{
             'text_input': 'seven',
             'output': 'eight',
        }
    ],
    id = name,
    epoch_count = 100,
    batch_size=4,
    learning_rate=0.001,
)

'''
Your tuned model is immediately added to the list of tuned models,
but its status is set to "creating" while the model is tuned.

model = genai.get_tuned_model(f'tunedModels/{name}')

model

model.state
'''


'''
I saw this:

(gemini1) dan@hpsda6:~/lx/lx14/public/py$ 
(gemini1) dan@hpsda6:~/lx/lx14/public/py$ python -i tuning02.py
Traceback (most recent call last):
  File "/media/dan/ssd1/lx/legalexamples/public/python_scripts/tuning02.py", line 71, in <module>
    operation = genai.create_tuned_model(
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/generativeai/models.py", line 364, in create_tuned_model
    operation = client.create_tuned_model(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/ai/generativelanguage_v1beta/services/model_service/client.py", line 1294, in create_tuned_model
    response = rpc(
               ^^^^
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__
    return wrapped_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/api_core/retry/retry_unary.py", line 293, in retry_wrapped_func
    return retry_target(
           ^^^^^^^^^^^^^
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/api_core/retry/retry_unary.py", line 153, in retry_target
    _retry_error_helper(
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/api_core/retry/retry_base.py", line 212, in _retry_error_helper
    raise final_exc from source_exc
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/api_core/retry/retry_unary.py", line 144, in retry_target
    result = target()
             ^^^^^^^^
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/api_core/timeout.py", line 130, in func_with_timeout
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/api_core/grpc_helpers.py", line 78, in error_remapped_callable
    raise exceptions.from_grpc_error(exc) from exc
google.api_core.exceptions.PermissionDenied: 403 You do not have permission to access tuned model generate-num-4879.
>>>
'''


'''
This looks like the shit I saw when I tried to walk through Vertex tutorials in 2023.
'''

'''
gpt, please offer ideas I can study to help me debug this Python Exception:
```
  File "/home/dan/anaconda3/envs/gemini1/lib/python3.11/site-packages/google/api_core/grpc_helpers.py", line 78, in error_remapped_callable
    raise exceptions.from_grpc_error(exc) from exc
google.api_core.exceptions.PermissionDenied: 403 You do not have permission to access tuned model generate-num-4879.
```
This exception is unexpected because it was caused by syntax straight from a Google tutorial I found on their site:
https://ai.google.dev/gemini-api/docs/model-tuning/tutorial?lang=python
and
https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/python.ipynb
Please search the web for information and discussions about developers who tried to do this Google tutorial.
Try to focus on the tutorial more than general debuggig tips.
Thanks!

Answer:
The error you're encountering suggests a permission issue when trying to access a tuned Gemini model. This is a common problem faced by developers following Google's tutorials for the Gemini API. Here are some ideas to help you debug and resolve this issue:

1. Check API key permissions: Ensure that your API key has the necessary permissions to access tuned models. You may need to enable additional scopes or permissions in your Google Cloud Console[3].

2. Verify project settings: Make sure you're using the correct project ID and that the Gemini API is enabled for your project[3].

3. Review authentication method: If you're using an API key, consider switching to OAuth 2.0 credentials, which may provide more comprehensive access to Gemini features[3].

4. Double-check model name: Ensure that the model name you're trying to access is correct and that you have permission to use it. The error message mentions "generate-num-4879", which might not be the correct model identifier[5].

5. Examine API version: Verify that you're using the correct API version (v1 or v1beta) that supports the features you're trying to use[5].

6. Update SDK version: Make sure you're using the latest version of the Google AI Python client library, as older versions may not support all features of the Gemini API[1].

7. Check for rate limits: Although less likely, ensure you haven't exceeded any rate limits or quotas for your project[5].

8. Review fine-tuning job status: If you've recently created a tuned model, check its status to ensure it has completed successfully and is ready for use[3][7].

9. Consult Google Cloud support: If the issue persists, consider reaching out to Google Cloud support or posting on their community forums for more specific assistance[9].

Remember to carefully review the documentation and examples provided in the Google tutorials, as they may have been updated since your initial attempt. If you continue to face issues, consider sharing more details about your specific implementation and environment on developer forums or Google's issue tracker for the Gemini API.

Citations:
[1] https://stackoverflow.com/questions/78154047/encountering-503-error-when-calling-gemini-api-from-google-colab
[2] https://www.w3schools.com/gen_ai/chatgpt-4/chatgpt-4_code_debug.php
[3] https://ai.google.dev/gemini-api/docs/model-tuning
[4] https://stackoverflow.com/questions/4929251/how-to-step-through-python-code-to-help-debug-issues
[5] https://ai.google.dev/gemini-api/docs/troubleshooting
[6] https://dev.to/hassanshahzadaheer/5-gpt-prompts-to-level-up-your-code-learning-1ac3
[7] https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune_gemini/tune-gemini-learn
[8] https://chatgpt.com
[9] https://www.googlecloudcommunity.com/gc/AI-ML/Fine-tuning-Gemini-models-through-mat-files-for-the-inputs/td-p/821008
[10] https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning

---
Answer from Perplexity: https://www.perplexity.ai/search/gpt-please-offer-ideas-i-can-s-k_Yzq3CcTCqwRlLDqWHJmw?utm_source=copy_output
'''

