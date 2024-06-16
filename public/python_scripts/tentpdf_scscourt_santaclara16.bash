#!/bin/bash

# tentpdf_scscourt_santaclara16.bash

/bin/ls -1 ~/lx/jffj/scscourt/pdfs/2023_0*pdf > ~/lx/lx14/public/py/tentpdf_scscourt17.txt
/bin/ls -1 ~/lx/jffj/scscourt/pdfs/2023_1*pdf >> ~/lx/lx14/public/py/tentpdf_scscourt17.txt

/bin/ls -1 ~/lx/jffj/scscourt/pdfs/2024_0*pdf >> ~/lx/lx14/public/py/tentpdf_scscourt17.txt
# /bin/ls -1 ~/lx/jffj/scscourt/pdfs/2024_1*pdf >> ~/lx/lx14/public/py/tentpdf_scscourt17.txt

# /bin/ls -1 ~/lx/jffj/scscourt/pdfs/2024_0*pdf >> ~/lx/lx14/public/py/tentpdf_scscourt17.txt
# /bin/ls -1 ~/lx/jffj/scscourt/pdfs/2024_1*pdf >> ~/lx/lx14/public/py/tentpdf_scscourt17.txt


git add .
git commit -am more-pdf
git push ghw2 main

exit
