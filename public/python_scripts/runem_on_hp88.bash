#!/bin/bash

# runem_on_hp88.bash

# Derived from:
# ~/lx/legalexamples/public/python_scripts/runem.bash
# Runs some scripts I like to run.

cd ~/lx/legalexamples/public/python_scripts/
date

/bin/bash tenttext_lacourt10.bash
date

. ~/lx/lx14/public/lx14b_env.bash
date

~/anaconda3/envs/lx12/bin/python tenttext_lacourt11.py
date

/bin/bash tenttext_lacourt12.bash
date

exit

/bin/bash tenttext_lacourt13.bash
date

/bin/bash tenttext_lacourt15.bash
date

# ~/anaconda3/envs/lx12/bin/python gen_summaries12.py

exit
