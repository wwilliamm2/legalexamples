'''~/lx/lx14/public/py/gettags_frompg1_a.py'''

'''
Gets tags from page 1 of a document.
A tag is a token like:
2021, complaint, demurrer, sacramento, plaintiff, casenumber, personal injury, auto, ...
Demo:
conda activate gemini2
python -i gettags_frompg1_a.py
'''

import datetime, glob, os, pathlib, re, sys, shlex, subprocess, time

def unq(): return datetime.datetime.now().strftime('%f')

def sshell(cmd_s): return os.system(cmd_s)

cn_s = '34-2021-00292112-CU-PA-GDS'

dir_s = os.path.expanduser(f'~/lx/gsc1/cases/unlimited_civil_2021_02/{cn_s}/')

fn_s = f'{cn_s}_05_01_08_2021_Complaint_Tiu_Maria_Plaintiff.pdf'

ffn_s = dir_s + fn_s

# Create a working folder

wrk_s = f'/tmp/gettags_{unq()}/'

mkdir_s = f'mkdir -p {wrk_s}'

sshell(f'{mkdir_s}')

# Get 1st pg of pdf

qpdf = os.path.expanduser('~/anaconda3/envs/gemini2/bin/qpdf')

sshell(f'cp {ffn_s} {wrk_s}')

page1pdf = f'{wrk_s}page1_{fn_s}'

cmd_qpdf_s = f'{qpdf} {wrk_s}{fn_s} --pages . 1 -- {page1pdf}'

sshell(cmd_qpdf_s)

# Get png page from pdf page 1

magick = os.path.expanduser('~/anaconda3/envs/gemini2/bin/magick')

sshell(f'{magick} -density 300 {page1pdf} -quality 100 {page1pdf}.png')

# Use tesseract to get text from png

tess = os.path.expanduser('~/anaconda3/envs/gemini2/bin/tesseract')

sshell(f'{tess} {page1pdf}.png {page1pdf}.png}')

# Prep gemini

'done'
