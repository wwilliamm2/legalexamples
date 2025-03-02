#!/bin/bash

# qpdf10.bash

# Simple qpdf demo.

# LLM, Please offer ideas and syntax to help me write a bash script which cuts big.pdf into pieces.
# I want each piece to hold 1 page. I want to write each piece to a numbered file corresponding
# to a page number like: /tmp/mypdf/my001.pdf

. gemini2.bash # to access anaconda3/envs/gemini2/bin/

bigpdf=~/gsc1/cases/case_types/real_property/34*GDS/34*GDS*2021_Complaint_Agheli*pdf

cp $bigpdf /tmp/big.pdf
mkdir -p /tmp/mypdf/
# Get the total number of pages
qpdf --show-npages /tmp/big.pdf
num_pages=$(qpdf --show-npages /tmp/big.pdf)
echo num_pages $num_pages

for ((i=1; i<=num_pages; i++)); do
    output_file=$(printf "/tmp/mypdf/my%s%03d.pdf" "$output_prefix" "$i")
    # date > $output_file
    # DONE ALREADY qpdf /tmp/big.pdf --pages /tmp/big.pdf "$i" -- "$output_file"
done

# Lets see if I can turn those pages into png files using imagemagick.

mkdir -p /tmp/mypng/

for fnpdf in /tmp/mypdf/my*.pdf
do
  ~/anaconda3/envs/gemini2/bin/magick -density 300 $fnpdf -scene 0 -quality 100 ${fnpdf}.png
done
