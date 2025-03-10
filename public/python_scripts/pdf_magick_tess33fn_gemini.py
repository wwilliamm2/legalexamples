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

# test ; what happens if bash-find gets many file names?
find1_s = 'find /home/dan/gsc1/cases/case_types/real_property/ -iname '
many_fnpdf_s_l = sshell2(find1_s+' *memorandum*.pdf').split()
fnpdf_s = sorted(many_fnpdf_s_l)[0]
'/home/dan/gsc1/cases/case_types/real_property/23CV001486/23CV001486_20_04_19_2024_Memorandum_of_Points_Authorities_ISO_Demurrer.pdf'
# test done ; ans: I need to split a large string into list of file names.

# basename of file I want to study
bnpdf_s = '34-2021-00292515-CU-OR-GDS_29_08_02_2022_Memorandum_of_Points_Authorit.pdf'
# Later I will get bnpdf_s from sys.argv[1]
many_fnpdf_s_l = sshell2(f'{find1_s} {bnpdf_s}').split()
fnpdf_s = sorted(many_fnpdf_s_l)[0]

# Do I need this:
dir_cn_s = os.path.dirname(fnpdf_s)
# ?

# Create a folder which I will use later to store llm summary files:
fn_s = fnpdf_s.replace('.pdf','')
sshell2(f'mkdir -p {fn_s}')

# Generate png files from pdf using imagemagick

# use ~/anaconda3/envs/gemini2 imagemagick to convert pdf to png:
# I need to cut the pdf into pieces or else magick will choke.

'''
rm -rf   /tmp/mypdf/
mkdir -p /tmp/mypdf/
cp $fnpdf /tmp/mypdf/big.pdf
'''

sshell2('rm -rf   /tmp/urpdf/')
sshell2('mkdir -p /tmp/urpdf/')
sshell2(f'cp {fnpdf_s} /tmp/urpdf/big.pdf')

print('qpdf is busy...')

sshell2('which qpdf')

# test qpdf
qpdf = os.path.expanduser('~/anaconda3/envs/gemini2/bin/qpdf')
try:
    sshell2(f'{qpdf} /tmp/urpdf/big.pdf --pages /tmp/urpdf/big.pdf 1 -- /tmp/urpdf/my001.pdf')
except:
    'ignore qpdf errors'
sshell(f'{qpdf} /tmp/urpdf/big.pdf --pages /tmp/urpdf/big.pdf 1 -- /tmp/urpdf/my001.pdf')
# sshell() works better here.
for pg_i in range(1,16):
    sshell(f'{qpdf} /tmp/urpdf/big.pdf --pages /tmp/urpdf/big.pdf {pg_i} -- /tmp/urpdf/my{pg_i:03}.pdf')
# sshell() works better here.

# Save my work to a folder near the Complaint doc.
sshell2(f'rsync -av /tmp/urpdf {fn_s}/')

# Use imagemagick to convert pdf files to png.
'''
echo magick is busy...
for ffnpdf in /tmp/mypdf/my0*.pdf
do
    echo magick -density 300 $ffnpdf -quality 100 ${ffnpdf}.png
    ~/anaconda3/envs/gemini2/bin/magick -density 300 $ffnpdf -quality 100 ${ffnpdf}.png
done
'''

magick = os.path.expanduser('~/anaconda3/envs/gemini2/bin/magick')
for ffnpdf in glob.glob('/tmp/urpdf/my0*.pdf'):
    sshell2(f'{magick} -density 300 {ffnpdf} -quality 100 {ffnpdf}.png')
# magick done, I now have png files.

# Save my work to a folder near the Complaint doc.
sshell2(f'rsync -av /tmp/urpdf {fn_s}/')

# Use tesseract to generate txt files from png files:
print('tesseract is busy...')
tess = os.path.expanduser('~/anaconda3/envs/gemini2/bin/tesseract')
for fnpng in glob.glob('/tmp/urpdf/my0*.pdf.png'):
    sshell2(f'{tess} {fnpng} {fnpng}')

# Save my work to a folder near the Complaint doc.
sshell2(f'rsync -av /tmp/urpdf {fn_s}/')

# Can I pass a right-carrot to sshell()?
sshell('cat /tmp/urpdf/my???.pdf.png.txt > /tmp/urpdf/big.pdf.png.txt')
# yep
# I will not actually use big.pdf.png.txt but I want to see it.

# Ask the llm to fix the OCR output of pages 0-14

myf_s_l = [myf_s for myf_s in sorted(glob.glob('/tmp/urpdf/my0*png.txt'))[:15]]
sshell(f"cat {' '.join(myf_s_l)} > /tmp/urpdf/pages1_14.txt")
    
    



