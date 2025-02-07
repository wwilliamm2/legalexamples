#!/bin/bash

# ~/lx/lx14/public/py/grepv_viewstate.bash

# Filters out some bad input elements.

# rsync -a ~/lx/jffj/lacourt/htmls /tmp/lacourt/
cd /tmp/lacourt/htmls/
for htmlf in 2025_*html
do
    grep -v __VIEWSTATE $htmlf > good.html
    mv good.html $htmlf
done


