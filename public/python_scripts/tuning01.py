'''~/lx/lx14/public/py/tuning01.py'''

'''
Helps me follow a Gemini tuning tutorial:
https://aistudio.google.com/tune
https://ai.google.dev/gemini-api/docs/model-tuning/tutorial?lang=python

Demo:
conda activate gemini1
python -i tuning01.py
'''

import datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing

# import google.generativeai as genai # old way
from google import genai # new way

'''
With Gemini 2 we are offering a new SDK (google-genai, v1.0).
The updated SDK is fully compatible with all Gemini API models and features,
including recent additions like the live API (audio + video streaming),
improved tool usage ( code execution, function calling and integrated Google search grounding),
and media generation (Imagen).
This SDK allows you to connect to the Gemini API through either
Google AI Studio or Vertex AI.

The google-generativeai package will continue to support the original Gemini models.

https://github.com/google-gemini/generative-ai-python/blob/8849d4f46010ce4ae68243c4f8a44a138b56598f/README.md#L30-L31
'''


'''
Before:
pip install -U -q "google-generativeai"
After:
pip install -U -q "google-genai"

ref:
gen_summaries20gemini.py , Old Way + LangChain
schmid14.py              , Newer
'''


#  Get the key from the GOOGLE_API_KEY env variable
client = genai.Client()

for model_info in client.models.list():
    print(model_info.name)
'''
(gemini1) dan@hpsda6:~/lx/lx14/public/py$ python -i tuning01.py
models/chat-bison-001
models/text-bison-001
models/embedding-gecko-001
models/gemini-1.0-pro-latest
models/gemini-1.0-pro
models/gemini-pro
models/gemini-1.0-pro-001
models/gemini-1.0-pro-vision-latest
models/gemini-pro-vision
models/gemini-1.5-pro-latest
models/gemini-1.5-pro-001
models/gemini-1.5-pro-002
models/gemini-1.5-pro
models/gemini-1.5-flash-latest
models/gemini-1.5-flash-001
models/gemini-1.5-flash-001-tuning <-- interests me
models/gemini-1.5-flash
models/gemini-1.5-flash-002
models/gemini-1.5-flash-8b
models/gemini-1.5-flash-8b-001
models/gemini-1.5-flash-8b-latest
models/gemini-1.5-flash-8b-exp-0827
models/gemini-1.5-flash-8b-exp-0924
models/gemini-2.0-flash-exp
models/gemini-2.0-flash
models/gemini-2.0-flash-001
models/gemini-2.0-flash-lite-preview
models/gemini-2.0-flash-lite-preview-02-05
models/gemini-2.0-pro-exp
models/gemini-2.0-pro-exp-02-05
models/gemini-exp-1206
models/gemini-2.0-flash-thinking-exp-01-21
models/gemini-2.0-flash-thinking-exp
models/gemini-2.0-flash-thinking-exp-1219
models/learnlm-1.5-pro-experimental
models/embedding-001
models/text-embedding-004
models/aqa
models/imagen-3.0-generate-002
>>>
'''

'''
To create a tuned model, you need to pass your dataset to the model in the tunedModels.create method.
https://ai.google.dev/api/tuning#Dataset
https://ai.google.dev/api/tuning#method:-tunedmodels.create
'''

# https://ai.google.dev/gemini-api/docs/model-tuning/tutorial?lang=python#create-tuned-model

# create tuning model
training_dataset =  [
    ["1", "2"],
    ["3", "4"],
    ["-3", "-2"],
    ["twenty two", "twenty three"],
    ["two hundred", "two hundred one"],
    ["ninety nine", "one hundred"],
    ["8", "9"],
    ["-98", "-97"],
    ["1,000", "1,001"],
    ["10,100,000", "10,100,001"],
    ["thirteen", "fourteen"],
    ["eighty", "eighty one"],
    ["one", "two"],
    ["three", "four"],
    ["seven", "eight"],
]

'''
FAILS here:
NameError: name 'types' is not defined. Did you mean: 'type'?

This is probably a documentation-bug.

oh well...
I will study the collab notebook I see here:
https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/python.ipynb

training_dataset=types.TuningDataset(
        examples=[
            types.TuningExample(
                text_input=i,
                output=o,
            )
            for i,o in training_dataset
        ],
    )
tuning_job = client.tunings.tune(
    base_model='models/gemini-1.0-pro-001',
    training_dataset=training_dataset,
    config=types.CreateTuningJobConfig(
        epoch_count= 5,
        batch_size=4,
        learning_rate=0.001,
        tuned_model_display_name="test tuned model"
    )
)

# generate content with the tuned model
response = client.models.generate_content(
    model=tuning_job.tuned_model.model,
    contents='III',
)

print(response.text)
'''
