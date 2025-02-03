#!/bin/bash

# prepend_modelname2summary.bash

# Prepends a model name to many summary files.

# Demo:
# find /home/dan/lx/jffj/lacourt/text/2025_02_*/ -name 'summary_*.txt' -type f | sed 's:^:./prepend_modelname2summary.bash :'
# bash ./prepend_modelname2summary.bash /home/dan/lx/jffj/lacourt/text/2025_02_24_LAM_17/summary_01.txt

echo >> $1

# Inefficent but easy to understand:
cat <<EOF > /tmp/newsummary.txt
..................... ..................... ..................... ......
The summary displayed below was created by an LLM named 'llama3-8b-8192':
EOF

cat $1 >> /tmp/newsummary.txt
cat       /tmp/newsummary.txt > $1

exit
