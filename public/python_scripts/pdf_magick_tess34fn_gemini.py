'''~/di/py/pdf_magick_tess34fn_gemini.py'''

'''
Helps me study gemini, magick, tesseract.

Demo:
conda activate gemini2
python -i pdf_magick_tess34fn_gemini.py
'''

import datetime, glob, os, re, sys, shlex, subprocess, time

def unq(): return datetime.datetime.now().strftime('%f')

def wwrite(fn_s, my_s):
    with open(fn_s, 'w') as wwf:
        wwf.write(my_s)
    return True

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

def sshell3(cmd_s):
    bash_fn_s = f'/tmp/sshell3_script_{unq()}.bash'
    wwrite(bash_fn_s, cmd_s+'\n')
    return subprocess.run(['bash', bash_fn_s])

# basename of pdf I want to study
bnpdf_s = '34-2023-00337041-CU-OR-GDS_21_07_05_2023_Memorandum_of_Points_Authorit.pdf'
# Later I will get bnpdf_s from sys.argv[1]
find1_s = 'find /home/dan/gsc1/cases/case_types/real_property/ -iname '
many_fnpdf_s_l = sshell2(f'{find1_s} {bnpdf_s}').split()
# Full name of the pdf:
fnpdf_s = [f_s for f_s in many_fnpdf_s_l if bnpdf_s in f_s][0]
# Create a folder which I will use later to store llm summary files:
fn_s = fnpdf_s.replace('.pdf','')
sshell2(f'mkdir -p {fn_s}')

# Get the first 25 pages of the pdf
qpdf = os.path.expanduser('~/anaconda3/envs/gemini2/bin/qpdf')
'llama:   qpdf --pages /tmp/big.pdf 1-25 -- /tmp/little.pdf.' # wrong
'perplxy: qpdf /tmp/big.pdf --pages . 1-25 -- /tmp/little.pdf' # right

cmd_s = f'''
rm -rf /tmp/urpdf
mkdir -p /tmp/urpdf/
cp {fnpdf_s} /tmp/urpdf/big.pdf
'''
sshell3(cmd_s)

# How many pages in the pdf?
npg_i = int(sshell2(f'{qpdf} --show-npages /tmp/urpdf/big.pdf'))

# I want 25 pages or less
if 25 >= npg_i:
    cmd_s = 'cp /tmp/urpdf/big.pdf /tmp/urpdf/pg1_25.pdf' # just use big.pdf
else:
    cmd_s = '{qpdf} /tmp/urpdf/big.pdf --pages . 1-25 -- /tmp/urpdf/pg1_25.pdf'

sshell2(cmd_s)

