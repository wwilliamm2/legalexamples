#!/bin/bash

# groq4.bash

# Sends ~/prompt.txt to groq LLM for a response back.
# demo:
# bash groq4.bash gemma2-9b-it

. ~/lx/lx14/public/lx14b_env.bash

python llm_groq4bash13.py ~/prompt.txt $1

exit
