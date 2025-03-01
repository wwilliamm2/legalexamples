#!/bin/bash

# pdf_magick_tess10.bash

# . "/home/dan/anaconda3/etc/profile.d/conda.sh"
# conda activate gemini2

# This gives me imagemagick , tesseract 
. ~/lx/lx14/public/py/gemini2.bash

pdfn='/home/dan/gsc1/cases/case_types/real_property/34-2021-00313325-CU-OR-GDS/34-2021-00313325-CU-OR-GDS_03_12_30_2021_Complaint_McElhaney_Roddie_Pl.pdf'

pngn=`echo $pdfn | sed 's/.pdf$/.png/'`

echo busy ...
echo wait for this:
echo $pngn

# use ~/anaconda3/envs/gemini2 imagemagick to convert pdfn to png:
~/anaconda3/envs/gemini2/bin/magick convert -density 300 $pdfn -quality 100 $pngn

exit
