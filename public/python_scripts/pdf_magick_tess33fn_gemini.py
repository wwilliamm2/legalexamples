'''~/di/py/pdf_magick_tess33fn_gemini.py'''

'''
Helps me study gemini, magick, tesseract.

Demo:
conda activate gemini2
python -i pdf_magick_tess33fn_gemini.py
'''

import datetime, glob, os, re, sys, shlex, subprocess, time

def sshell(cmd_s): return os.system(cmd_s)

def sshell2(cmd_s):
    '''Runs shell cmd_s, captures and returns out_s.'''
    # Split the command into a list of arguments
    args = shlex.split(cmd_s)
    # Run the command and capture the output
    out1_s = subprocess.check_output(args)
    # Decode the output from bytes to a string
    out_s = out1_s.decode('utf-8').strip()
    return out_s

# basename of file I want to study
bnpdf_s = '34-2021-00292515-CU-OR-GDS_29_08_02_2022_Memorandum_of_Points_Authorit.pdf'
# Later I will get bnpdf_s from sys.argv[1]

# test ; what happens if bash-find gets many file names?
find1_s = 'find /home/dan/gsc1/cases/case_types/real_property/ -iname '
many_fnpdf_s_l = sshell2(find1_s+' *memorandum*.pdf').split()
fnpdf_s = sorted(many_fnpdf_s_l)[0]
'/home/dan/gsc1/cases/case_types/real_property/23CV001486/23CV001486_20_04_19_2024_Memorandum_of_Points_Authorities_ISO_Demurrer.pdf'
# test done ; ans: I need to split a large string into list of file names.
