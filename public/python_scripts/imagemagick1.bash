#!/bin/bash

# ~/lx/lx14/public/py/imagemagick1.bash

# Uses a loop to call magick on some pdf files

# Demo:
# conda activate imagemagick
# bash ~/lx/lx14/public/py/imagemagick1.bash

echo started:
date

fldr=/media/dan/ssd2/tmp/scscourt/pdfs/
for pdf in ${fldr}2024*/2*page*.pdf
do
    if [ -f ${pdf}.png ]; then
	echo magick did this already: ${pdf}.png
    else
	echo magick $pdf ${pdf}.png
	magick $pdf ${pdf}.png
    fi
done

echo finished:
date

exit

# gpt, please write demo Bash syntax which returns true if /tmp/abc.tx exists

if [ -f "/tmp/abc.tx" ]; then
    echo "File exists"
    exit 0
else
    echo "File does not exist"
    exit 1
fi
