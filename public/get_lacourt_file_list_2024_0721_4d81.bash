#!/bin/bash

# ~/lx/lx14/public/get_lacourt_file_list.bash

# Gets a list of available html files.

# /bin/ls -1 ~tent1/tent1/lacourt/htmls/2*html > lacourt_file_list.txt

# copy recent html files to the right place:
rsync -a ~tent1/tent1/lacourt/htmls/2*html ~/lx/jffj/lacourt/htmls/

/bin/ls -1 ~/lx/jffj/lacourt/htmls/2*html > tmp.txt
cat tmp.txt | sed '1,$s:/home/lc11/lx/jffj/lacourt/htmls/::' > lacourt_file_list.txt

# These files shd also be available from jffjorg github repo.

exit
