'''~/di/py/pdf_magick_tess35fn_gemini.py'''

'''
Helps me study gemini, magick, tesseract.

Demo:
conda activate gemini2
python -i pdf_magick_tess35fn_gemini.py
'''

import datetime, glob, os, re, sys, shlex, subprocess, time

def unq(): return datetime.datetime.now().strftime('%f')

def rread(fn_s):
    with open(fn_s,'r') as rf:
        return rf.read()

def wwrite(fn_s, my_s):
    with open(fn_s, 'w') as wwf:
        wwf.write(my_s)
    return True

def wwrites(my_s, fn_s):
    return wwrite(fn_s, my_s) # switch them
    
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

# Get individual pdf pages:
for pg_i in range(1,npg_i+1):
    sshell(f'{qpdf} /tmp/urpdf/big.pdf --pages /tmp/urpdf/big.pdf {pg_i} -- /tmp/urpdf/my{pg_i:03}.pdf')

# Get png pages from pdf pages
magick = os.path.expanduser('~/anaconda3/envs/gemini2/bin/magick')
for ffnpdf in glob.glob('/tmp/urpdf/my0*.pdf'):
    sshell2(f'{magick} -density 300 {ffnpdf} -quality 100 {ffnpdf}.png')
# magick done, I now have png files.
    
# Use tesseract to generate txt files from png files:
print('tesseract is busy...')
tess = os.path.expanduser('~/anaconda3/envs/gemini2/bin/tesseract')
for fnpng in glob.glob('/tmp/urpdf/my0*.pdf.png'):
    sshell2(f'{tess} {fnpng} {fnpng}')

# Prep gemini

from google import genai
model_id  = 'gemini-2.0-flash'
modelf_id = 'gemini-2.0-flash'
modelp_id = 'gemini-2.0-pro-exp-02-05'

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# prep txt for the llm to fix the OCR output of pages.

# I need to loop through /tmp/urpdf/my0*png.txt and enhance each page
# rather than try to enhance 1 large txt file.

# replace this with a loop
# myf_s_l = [myf_s for myf_s in sorted(glob.glob('/tmp/urpdf/my0*png.txt'))]
# sshell(f"cat {' '.join(myf_s_l)} > /tmp/urpdf/ocr_txt4_llm.txt")

for txtf_s in glob.glob('/tmp/urpdf/my0*.pdf.png.txt'):
    ocrp2_s = rread('ocr_prompt14pdf.txt') + rread(txtf_s)
    response1 = client.models.generate_content(model=modelf_id, contents=[ocrp2_s])
    wwrites(response1.text, + 'llm_enhanced_' + txtf_s)
sshell(f"cat /tmp/urpdf/llm_enhanced_*.txt > /tmp/urpdf/ocr_txt4_llm.txt")

# Summarize the enhanced text
sshell(f'cat summary_prompt14.txt /tmp/urpdf/ocr_txt4_llm.txt > /tmp/urpdf/full_summary_prompt.txt')

fsp_s = rread("/tmp/urpdf/full_summary_prompt.txt")

response2 = client.models.generate_content(model=modelp_id, contents=[fsp_s])

wwrite('/tmp/urpdf/full_llm_summary.txt', response2.text)
'done'
