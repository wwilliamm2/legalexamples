#!/bin/bash

# pdf_magick_tess10.bash

# . "/home/dan/anaconda3/etc/profile.d/conda.sh"
# conda activate gemini2
# Do this instead, this gives me imagemagick , tesseract :
. ~/lx/lx14/public/py/gemini2.bash

pdfn='/home/dan/gsc1/cases/case_types/real_property/34-2021-00313325-CU-OR-GDS/34-2021-00313325-CU-OR-GDS_03_12_30_2021_Complaint_McElhaney_Roddie_Pl.pdf'

pngn=`echo $pdfn | sed 's/.pdf$/-%03d.png/'`

echo busy ...
echo wait for this:
echo $pngn

# use ~/anaconda3/envs/gemini2 imagemagick to convert pdfn to png:
echo ~/anaconda3/envs/gemini2/bin/magick -density 300 $pdfn -scene 0 -quality 100 $pngn

# Use Tesseract to extract text from png file:
fn=`echo $pdfn | sed 's/.pdf$//'`
for pngf in ${fn}*png
do
    ~/anaconda3/envs/gemini2/bin/tesseract $pngf $pngf
done

exit
