#!/bin/bash

# ~/lx/lx14/public/py/pdf_magick_tess12.bash

# This script leads towards automating OCR + LLM text generation from Complaint docs.

. gemini2.bash


# G, Please give me ideas and syntax I can study to help my place if-then logic in a bash script which looks for $1 and does `echo found dolla1` if $1 has a value.

if [ -n "$1" ]; then
    cn_s=$1
    echo cn_s is $cn_s
else
    echo You forgot to give me a value for cn_s. Bye.
    exit 1
fi

fnpdf=`find /home/dan/gsc1/cases/case_types/real_property/${cn_s}/ -iname '*complaint*pdf' | head -1`
echo fnpdf is $fnpdf

if [ ! -f $fnpdf ]; then
  echo "Error: $fnpdf missing , bye."
  exit 1
fi

fn=`echo $fnpdf | sed 's/.pdf$//'`

# Generate png files from pdf using imagemagick

fnpng=`echo $fn | sed 's/$/-%03d.png/'`

echo busy ...
echo wait for this pattern to be used by magick:
echo $fnpng

# use ~/anaconda3/envs/gemini2 imagemagick to convert pdfn to png:
~/anaconda3/envs/gemini2/bin/magick -density 300 $fnpdf -scene 0 -quality 100 $fnpng

exit

echo done.
echo This:
ls -l $fnpdf
echo gave me this:
ls -l ${fn}*png
echo try this to view the new png files:
echo eog ${fn}*png

# Use tesseract to generate txt files from png files:
echo tesseract is busy...
for pngf in ${fn}*png
do
    ~/anaconda3/envs/gemini2/bin/tesseract $pngf $pngf
done
echo tesseract is done

echo Maybe study these:
echo emacs ${fn}*png.txt

# Prep for llm.
cat ocr_prompt10.txt ${fn}*png.txt > ~/prompt.txt
echo '```' >> ~/prompt.txt

cp ~/prompt.txt   ${fn}_llm_prompt.txt

# Ask the llm to fix the OCR output.
date 
echo LLM is busy please wait .......
~/bin/llm4.bash > ${fn}_llm_enhanced.txt
sleep 61 # throttle it

# Prep for llm summary.
cat summary_prompt10.txt ${fn}_llm_enhanced.txt > ~/prompt.txt
echo '```' >> ~/prompt.txt
date 
echo LLM is busy please wait .......
~/bin/llm4.bash > ${fn}_llm_summary.txt
echo LLM is done.
date

exit


