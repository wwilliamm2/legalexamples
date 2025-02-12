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

from google import genai

#  Get the key from the GOOGLE_API_KEY env variable
client = genai.Client()

