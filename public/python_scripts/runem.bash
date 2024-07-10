#!/bin/bash

# ~/lx/legalexamples/public/python_scripts/runem.bash
# Runs some scripts I like to run.

cd ~/lx/legalexamples/public/python_scripts/

/bin/bash tenttext_lacourt10.bash
. ~/lx/lx12_env.bash
~/anaconda3/envs/lx12/bin/python tenttext_lacourt11.py
/bin/bash tenttext_lacourt12.bash

/bin/bash tenttext_lacourt13.bash

exit
/bin/bash tenttext_lacourt15.bash
