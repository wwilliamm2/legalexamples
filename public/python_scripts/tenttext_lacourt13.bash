#!/bin/bash

# ~/lx/lx14/public/py/tenttext_lacourt13.bash

# Helps me prep text files for github.io repo for serving
# --ignore-existing       skip updating files that already exist on receiver
# --dry-run               perform a trial run with no changes made
# --list-only             list the files instead of copying them

# gpt, write demo bash syntax which lists files in /dir1/ which are not in /dir2/.
# see notin.bash


rsync -av /tmp/lacourt_text/202* ~/lx/jffj/lacourt/text/

du -sh ~/lx/jffj/lacourt/text/

# cd ~/lx/jffj/lacourt/
# git add text
# git commit -am more-text
# git push origin main

# /bin/ls -1 ~/lx/jffj/lacourt/text/202*/tent*.txt > ~/lx/lx14/public/py/tenttext_lacourt14.txt
# bash: /bin/ls: Argument list too long
# darn
# Try listing fewer files:
/bin/ls -1 ~/lx/jffj/lacourt/text/2023_0*/tent*.txt > ~/lx/lx14/public/py/tenttext_lacourt14.txt
/bin/ls -1 ~/lx/jffj/lacourt/text/2023_1*/tent*.txt >> ~/lx/lx14/public/py/tenttext_lacourt14.txt
/bin/ls -1 ~/lx/jffj/lacourt/text/2024_0*/tent*.txt >> ~/lx/lx14/public/py/tenttext_lacourt14.txt
# Eventually these should not fail:
/bin/ls -1 ~/lx/jffj/lacourt/text/2024_1*/tent*.txt >> ~/lx/lx14/public/py/tenttext_lacourt14.txt
/bin/ls -1 ~/lx/jffj/lacourt/text/2025_0*/tent*.txt >> ~/lx/lx14/public/py/tenttext_lacourt14.txt
/bin/ls -1 ~/lx/jffj/lacourt/text/2025_1*/tent*.txt >> ~/lx/lx14/public/py/tenttext_lacourt14.txt

cd ~/lx/lx14/public/py/
git add .
git commit -am more-text
git push ghw2 main
bash ../deploylx14.bash

exit
