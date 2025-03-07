#!/bin/bash

# groq4.bash

# Sends ~/prompt.txt to groq LLM for a response back.
# demo:
# bash groq4.bash
# or
# bash groq4.bash [~/prompt.txt [gemma2-9b-it]]
# demos:
# groq4.bash myprompt.txt      llama-guard-3-8b
# groq4.bash /tmp/urprompt.txt llama-3.1-8b-instant
# groq4.bash ~/xprompt.txt     llama3-70b-8192
#
# see: ~/lx/lx14/public/py/groq_models.txt

. ~/lx/lx14/public/py/gemini2.bash

prompt_s=$1
model_s=$2

python ~/lx/lx14/public/py/llm_groq4bash17.py $1 $2

exit
