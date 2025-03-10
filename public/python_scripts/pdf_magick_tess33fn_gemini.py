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

# Copy prompt-prefix + pages1_14.txt into /tmp/urpdf/full_summary_1_prompt.txt
sshell(f'cat summary_prompt10.txt /tmp/urpdf/pages1_14.txt > /tmp/urpdf/full_summary_1_prompt.txt')
sshell("echo '```' >>  /tmp/urpdf/full_summary_1_prompt.txt")

# Send /tmp/urpdf/full_summary_1_prompt.txt to gemini

with open('/tmp/urpdf/full_summary_1_prompt.txt','r') as fsp:
    fsp_s = fsp.read()

fsp_s[:33]

from google import genai
model_id = 'gemini-2.0-flash'
model_id = 'gemini-2.0-pro-exp-02-05'
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
response = client.models.generate_content(model=model_id, contents=[fsp_s])
response.text
# response.candidates[0].content.parts[0].text
with open('/tmp/urpdf/big_llm_1_summary.txt','w') as rspf:
    rspf.write(response.text)

'done'

'''
Okay, here's a summary of the legal information in `legal_info_and_ocr_info.txt`, prepared for the judge, focusing on the requested elements and avoiding the OCR/LLM generation details:

**Case Summary for Judge**

**Case Name:**  `Adam Harmoning v. Cheyenne Funding et al.`

**Case Number:** 34-2021-00292515

**Court:** Superior Court of the State of California, County of Sacramento

**Current Date of Document:** August 1, 2022, date of signature, Memorandum.
**Filing Date:** August 2, 2022.

**Document Type:** Memorandum of Points and Authorities in Support of Motion for Dismissal of Action Against Lawyers Title Company and Bea Ayotte; and For Judgment in Their Favor Following Plaintiff's Failure to Amend Complaint

**Parties and Roles:**

*   **Plaintiff:** Adam Harmoning (appearing *pro per*, meaning representing himself)
*   **Defendants:**
    *   Cheyenne Funding (aka Cheyenne Funding, a Wyoming Corporation aka Cheyenne Funding, Inc.)
    *   Milestone Financial LLC
    *   William R. Stuart
    *   Lawyers Title Company ("LTC") - *Moving Party for Dismissal*
    *   Bea Ayotte (aka Beatrice Rose Ayotte aka Beatrice Rose Ayotte-Tyson) - *Moving Party for Dismissal*
    *   Aquino Trust #2919
    *   Raul Chavez
    *   Florence Real Estate
    *   Christopher J. Firenze
    *   Emily A. Santana
    *   Does 8-17 (unnamed defendants)

* **Attorneys:**
    *   Gina Arico-Smith (SBN: 139645) of Fidelity National Law Group, representing Lawyers Title Company and Bea Ayotte.

**Timeline of Relevant Events:**

1.  **Prior to June 28, 2022:** Plaintiff Adam Harmoning filed a Third Amended Complaint ("TAC") against multiple defendants, including Lawyers Title Company and Bea Ayotte (collectively, "LTC Defendants").
2.  **June 28, 2022:** The Court issued a tentative ruling sustaining the LTC Defendants' demurrer to the TAC and granted Harmoning leave to amend.  The deadline for filing the amended complaint was set for July 11, 2022.
3.  **June 29, 2022:** The tentative ruling became a minute order, effective immediately. No formal order or further notice was required.
4.  **July 11, 2022:** Deadline for Plaintiff Harmoning to file a Fourth Amended Complaint.  He failed to do so.
5.  **August 1, 2022:** Date of LTC Defendants' current motion.
6.  **August 2, 2022**: LTC Defendants file the present motion for dismissal.
7. **Oct 12, 2022**: Date of hearing for Motion. Dept 53, 1:30 p.m.

**Nature of the Motion:**

The LTC Defendants (Lawyers Title Company and Bea Ayotte) are moving for dismissal of the action against them and for entry of judgment in their favor.  The basis for the motion is Plaintiff's failure to file a Fourth Amended Complaint by the court-ordered deadline of July 11, 2022.

**Legal Arguments and Authorities:**

*   **Dismissal for Failure to Amend:**
    *   **California Rule of Court 3.1320(h):**  Relates to procedures for amending pleadings after a demurrer is sustained.
    *   **Code of Civil Procedure § 581(f)(2):** Allows the court to dismiss a complaint when a plaintiff fails to amend it within the time allowed by the court after a demurrer is sustained with leave to amend.
    *    LTC Defendants assert that the court's file should show, pursuant to Evid. Code Section 452(d), that the Fourth Amended Complaint was not filed.

*   **Entry of Separate Judgment:**
    *   **Code of Civil Procedure § 579:**  Allows the court, in its discretion, to render judgment against one or more defendants, leaving the action to proceed against others, whenever a several judgment is proper.
    *   **Case Law:**  `Cuevas v. Truline Corp.` (2004) 118 Cal.App.4th 56, 60-61.  This case supports the proposition that the "one final judgment rule" does not prohibit separate judgments against some, but not all, defendants.  It clarifies that CCP § 579 allows for such separate judgments. Other relevant, cited Cases include: `Vandenberg v. Superior Court` (1999) 21 Cal.4th 815, 824, and `T & R Painting Construction, Inc. v. St. Paul Fire & Marine Ins. Co.` (1994) 23 Cal.App.4th 738, 742-743.
    * LTC Defendants do not know who the remaining defendants are.

**Underlying Dispute (Limited Information):**

The document provides very little information about the underlying dispute. We know:

*   Plaintiff Harmoning filed a Third Amended Complaint, suggesting prior iterations of the complaint and ongoing disputes about its sufficiency.
*   The LTC Defendants demurred to the Third Amended Complaint, meaning they argued it was legally insufficient.
*   The court agreed with the LTC Defendants (at least in part) and gave Harmoning a chance to amend.
*   The specific causes of action and facts are not detailed in this memorandum.  The nature of Harmoning's claims against the LTC Defendants is unknown. We do not know what facts are or were in dispute.
* There is no explicit mention of money, causes of action, or property, but the involvement of a title company (Lawyers Title Company) suggests a potential dispute related to real estate. The presence of "Cheyenne Funding" and "Milestone Financial LLC" suggests a financial component.

**Relevant Information for the Judge:**

1.  **Procedural Posture:** This is a motion for dismissal based on a procedural failure (failure to amend). The judge needs to verify that the plaintiff did, in fact, fail to file the Fourth Amended Complaint by the deadline.
2.  **Discretion:**  Code of Civil Procedure § 581(f)(2) states the court *may* dismiss the complaint. This is a discretionary decision. The judge should consider whether there are any extenuating circumstances or reasons to give the plaintiff another opportunity to amend, despite the missed deadline. However, the Plaintiff was *pro per*.
3.  **Separate Judgment:** The judge needs to determine if a separate judgment for the LTC Defendants is appropriate under CCP § 579. This will likely depend on whether the claims against the LTC Defendants are sufficiently distinct from the claims against the remaining defendants (if any). The *Cuevas* case provides guidance.
4.  **Underlying Merits:** While the motion is procedural, the judge may want to briefly review the Third Amended Complaint (if available) and the ruling on the demurrer to understand the context of the case and the nature of the deficiencies the plaintiff was supposed to cure. This is important to ensure that dismissal is just and that the plaintiff is not being unfairly penalized for a minor technicality. Because Plaintiff is pro per, a review for fairness is warranted.
5.  **Verification:** The judge should independently verify that the Fourth Amended Complaint was not filed, as claimed by the LTC Defendants.
6. **Missing Defendants:** It may be prudent for the Court to ascertain the status of the other Defendants in the case.

This summary provides a clear picture of the procedural situation and the legal arguments, highlighting the key decisions the judge needs to make. It also flags the limited information about the underlying dispute and suggests further review of prior filings to fully understand the context.
'''
