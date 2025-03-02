#!/bin/bash

# ~/lx/lx14/public/py/pdf_magick_tess11.bash

# This script leads towards automating OCR + LLM text generation from Complaint docs.

. gemini2.bash

cn_s=34-2021-00291956-CU-OR-GDS

fnpdf=`find /home/dan/gsc1/cases/case_types/real_property/${cn_s}/ -iname '*complaint*pdf'`

fn=`echo $fnpdf | sed 's/.pdf$//'`

# Generate png files from pdf using imagemagick

fnpng=`echo $fn | sed 's/$/-%03d.png/'`

echo busy ...
echo wait for this:
echo $fnpng

# use ~/anaconda3/envs/gemini2 imagemagick to convert pdfn to png:
~/anaconda3/envs/gemini2/bin/magick -density 300 $fnpdf -scene 0 -quality 100 $fnpng
echo done.
echo This:
ls -l $fnpdf
echo gave me this:
ls -l ${fn}*png
echo try this to view the new png files::
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

# Ask the llm to fix the OCR output.
~/bin/llm4.bash

<<EOF

'Hi, offer ideas and syntax I can study to help me write bash syntax to do a case insensitive search for /tmp/CoMpLaInt.pDf ; Maybe `ls` offers a case insensitive glob feature? '
'Ans: find /tmp -iname "complaint.pdf"'

EOF
