#!/bin/bash

# ~/lx/lx14/public/py/pdf_magick_tess14.bash

# This script leads towards automating OCR + LLM text generation from Complaint docs.

# Demo:
# bash pdf_magick_tess14.bash 34-2021-00292843-CU-OR-GDS

. gemini2.bash

if [ -n "$1" ]; then
    cn_s=$1
    echo cn_s is $cn_s
else
    echo You forgot to give me a value for cn_s. Bye.
    exit 1
fi

dir_cn_s=/home/dan/gsc1/cases/case_types/real_property/${cn_s}/
echo $dir_cn_s

# fnpdf=`find /home/dan/gsc1/cases/case_types/real_property/${cn_s}/ -iname '*complaint*pdf' | head -1`
fnpdf=`find $dir_cn_s -iname '*complaint*pdf' | head -1`
echo fnpdf is $fnpdf

if [ ! -f $fnpdf ]; then
  echo "Error: $fnpdf missing , bye."
  exit 1
fi

fn=`echo $fnpdf | sed 's/.pdf$//'`

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

# Save my work to a folder near the Complaint doc.
rsync -av /tmp/mypdf $dir_cn_s

# Prep for llm.
cat ocr_prompt10.txt /tmp/mypdf/my*.txt > ~/prompt.txt
echo '```' >> ~/prompt.txt

cp ~/prompt.txt ${fn}_llm_prompt.txt

exit

# Ask the llm to fix the OCR output.
date 
echo LLM is busy please wait .......
~/bin/llm4.bash gemini-2.0-flash-exp > ${fn}_llm_enhanced.txt

sleep 61 # throttle it

# Prep for llm summary.
cat summary_prompt10.txt ${fn}_llm_enhanced.txt > ~/prompt.txt
echo '```' >> ~/prompt.txt
date 
echo LLM is busy please wait .......
~/bin/llm4.bash gemini-2.0-flash-exp > ${fn}_llm_summary.txt
echo LLM is done.
date

exit
