#!/bin/bash
# pdf_magick_tess23fn_groq_drive.bash
# generates some bash commands to summarize some complaints
cd ~/lx/lx14/public/py/

ls -1 ~/gsc1/cases/case_types/real_property/34-2021*/34*pdf | grep -i complaint | awk '{print "basename " $1}' > /tmp/p1.bash

bash /tmp/p1.bash | awk '{print "bash pdf_magick_tess22fn_groq.bash " $1}' > pdf_magick_tess24fn_groq_drive.bash

exit
