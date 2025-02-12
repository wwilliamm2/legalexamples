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
