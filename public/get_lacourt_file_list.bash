#!/bin/bash

# ~dan/lx/lx14/public/get_lacourt_file_list.bash

# Gets a list of available html files.

cd ~dan/lx/lx14/public/

# copy recent html files to the right place:
# rsync -a ~dan/lx/tent1/lacourt/htmls/2*html ~dan/lx/jffj/lacourt/htmls/
rsync -a tent1@d81:tent1/lacourt/htmls/2*html ~dan/lx/jffj/lacourt/htmls/

/bin/ls -1 /home/dan/lx/jffj/lacourt/htmls/2*html > tmp.txt
cat tmp.txt | sed '1,$s:/home/dan/lx/jffj/lacourt/htmls/::' > lacourt_file_list.txt

# These files shd also be available from jffjorg github repo.

exit
