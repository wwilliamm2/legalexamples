#!/bin/bash

# runem_on_hp88.bash

# Derived from:
# ~/lx/legalexamples/public/python_scripts/runem.bash
# Runs some scripts I like to run.

cd ~/lx/lx14/public/py/
date

/bin/bash tenttext_lacourt10.bash
date

. ~/lx/lx14/public/lx14b_env.bash
date

python tenttext_lacourt11.py
date

/bin/bash tenttext_lacourt12.bash
date

/bin/bash tenttext_lacourt13.bash
date

# commit the new text files
/bin/bash tenttext_lacourt15.bash
date

# python gen_summaries12_hp88.py

# commit the new summaries
/bin/bash tenttext_lacourt15.bash
date

exit
