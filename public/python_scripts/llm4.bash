#!/bin/bash

# ~/lx/lx14/public/py/llm4.bash

# Sends a prompt to an LLM in Google AI Studio.
# The prompt should be inside ~/prompt.txt
# Demo:
# echo 'Please describe how to access a command line token inside argv in Python. Thanks!' > ~/prompt.txt
# ./llm4.bash

. "/home/dan/anaconda3/etc/profile.d/conda.sh"
conda activate gemini2

python ~/di/py/llm4bash12.py ~/prompt.txt
exit

