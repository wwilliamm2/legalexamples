#!/bin/bash

# Helps me spot new html files not in my current set of html files.

# The new files are here:
# ~tent1/tent1/lacourt/htmls/2024_06_*.html

# my current set of html files is here:
# ~/lx/jffj/lacourt/htmls/2024_06_*.html

cd ~tent1/tent1/lacourt/htmls/
find . -name '2024_06_*.html' | sort > /tmp/new_html.txt

cd ~/lx/jffj/lacourt/htmls/
find . -name '2024_06_*.html' | sort > /tmp/current_html.txt

diff /tmp/new_html.txt /tmp/current_html.txt | grep "^<"

exit

# gpt, write demo bash syntax which lists files in /dir1/ which are not in /dir2/.
# The main idea that gpt gives me is to use the diff bash command.

# Define the directories
dir1="/path/to/dir1"
dir2="/path/to/dir2"

# List the files in dir1
files_in_dir1=$(/bin/ls -1 /tmp/d1)

# List the files in dir2
files_in_dir2=$(/bin/ls -1 /tmp/d2)

# Find the files that are in dir1 but not in dir2
files_only_in_dir1=$(diff <(echo "$files_in_dir1") <(echo "$files_in_dir2") | grep "^<")

# Output the result
echo "Files in /tmp/d1 but not in /tmp/d2 :"
echo "$files_only_in_dir1"


