#!/bin/bash

# ~/lx/lx14/public/py/pdf_magick_tess17fn_groq.bash

# This script leads towards automating OCR + groq-LLM text generation from Complaint docs.
# This script wants a file name , not a case number
# Demo:
# bash pdf_magick_tess17fn_groq.bash 34-2021-00293419-CU-OR-GDS_32_01_29_2021_Complaint_Davis_John_Plaintif.pdf

# I need access to qpdf, magick, and tesseract:
. gemini2.bash

if [ -n "$1" ]; then
    bnpdf=$1 # basename of file I want to study
    fnpdf=`find /home/dan/gsc1/cases/case_types/real_property/ -iname $1 | head -1`
    echo fnpdf is $fnpdf
    dir_cn_s=`dirname $fnpdf`
else
    echo You forgot to give me a value for file_name. Bye.
    exit 1
fi

if [ ! -f $fnpdf ]; then
  echo "Error: $fnpdf missing , bye."
  exit 1
fi

fn=`echo $fnpdf | sed 's/.pdf$//'`
echo fn is $fn

# Generate png files from pdf using imagemagick

# use ~/anaconda3/envs/gemini2 imagemagick to convert pdf to png:
# I need to cut the pdf into pieces or else magick will choke.

rm -rf   /tmp/mypdf/
mkdir -p /tmp/mypdf/

cp $fnpdf /tmp/big.pdf

# Get ready for some warnings from dirty pdf files
qpdf --show-npages /tmp/big.pdf
num_pages=$(qpdf --show-npages /tmp/big.pdf)
echo /tmp/big.pdf num_pages $num_pages

echo qpdf is busy...
for ((i=1; i<=num_pages; i++)); do
    output_file=$(printf "/tmp/mypdf/my%s%03d.pdf" "$output_prefix" "$i")
    echo qpdf /tmp/big.pdf --pages /tmp/big.pdf "$i" -- "$output_file"
    ~/anaconda3/envs/gemini2/bin/qpdf /tmp/big.pdf --pages /tmp/big.pdf "$i" -- "$output_file"
done

# Save my work to a folder near the Complaint doc.
rsync -av /tmp/mypdf $dir_cn_s

echo magick is busy...
for ffnpdf in /tmp/mypdf/my*.pdf
do
    echo magick -density 300 $ffnpdf -quality 100 ${ffnpdf}.png
    ~/anaconda3/envs/gemini2/bin/magick -density 300 $ffnpdf -quality 100 ${ffnpdf}.png
done

# Save my work to a folder near the Complaint doc.
rsync -av /tmp/mypdf $dir_cn_s

# Use tesseract to generate txt files from png files:
echo tesseract is busy...
for fnpng in /tmp/mypdf/my*.png
do
    echo tesseract $fnpng $fnpng
    ~/anaconda3/envs/gemini2/bin/tesseract $fnpng $fnpng
done

cat /tmp/mypdf/my???.pdf.png.txt > /tmp/mypdf/big.pdf.png.txt
# Save my work to a folder near the Complaint doc.
rsync -av /tmp/mypdf $dir_cn_s

# Prep for the LLM.

# Ask the llm to fix the OCR output.
date 
echo LLM is busy please wait .......

for mytxtfn in /tmp/mypdf/my*.txt
do
    echo working on: $mytxtfn ...
    cat ocr_prompt14pdf.txt $mytxtfn > ~/prompt.txt
    # Feed groq 1 page of text:
    ./groq4.bash ~/prompt.txt llama3-8b-8192 > ${mytxtfn}_llm_enhanced.txt
    # throttle it via 4 sec delay, leading to 15 Req/min (about) ,
    # which is less than API limit of 30 Req/Min:
    sleep 4
done

cat /tmp/mypdf/m*_llm_enhanced.txt > /tmp/mypdf/big_llm_enhanced.txt
# Save my work to a folder near the Complaint doc.
rsync -av /tmp/mypdf $dir_cn_s

echo Now I will throttle back for 61 sec to ease load on API server...

sleep 63 # throttle it

# Prep for llm summary.
cat summary_prompt10.txt /tmp/mypdf/big_llm_enhanced.txt > /tmp/mypdf/full_summary_prompt.txt
echo '```' >>  /tmp/mypdf/full_summary_prompt.txt
date

exit

echo LLM is busy please wait .......
./groq4.bash /tmp/mypdf/full_summary_prompt.txt llama3-8b-8192 > /tmp/mypdf/big_llm_summary.txt
echo LLM is done.

# Save my work to a folder near the Complaint doc.
rsync -av /tmp/mypdf $dir_cn_s

date

exit
