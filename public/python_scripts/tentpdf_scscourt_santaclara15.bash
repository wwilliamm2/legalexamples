#!/bin/bash
# tentpdf_scscourt_santaclara15.bash

# Copies pdf files to the right place.
rsync -av ~tent1/tent1/scscourt/pdfs/2023_0*pdf ~/lx/jffj/scscourt/pdfs/
rsync -av ~tent1/tent1/scscourt/pdfs/2023_1*pdf ~/lx/jffj/scscourt/pdfs/
rsync -av ~tent1/tent1/scscourt/pdfs/2024*pdf ~/lx/jffj/scscourt/pdfs/

cd ~/lx/jffj/
git add .
git commit -am more-pdf
git push origin main

exit

