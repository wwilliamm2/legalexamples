#!/bin/bash

# groq4.bash

# Sends ~/prompt.txt to groq LLM for a response back.
# demo:
# bash groq4.bash
# or
# bash groq4.bash gemma2-9b-it

'''
. ~/lx/lx14/public/py/gemini2.bash
python llm_groq4bash14.py # ~/prompt.txt $1
'''

# rely solely on python requests package:
python ~/lx/lx14/public/py/llm_groq4bash15.py # ~/prompt.txt $1

exit
