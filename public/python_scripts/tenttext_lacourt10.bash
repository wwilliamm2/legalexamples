#!/bin/bash

# public/py/tenttext_lacourt10.bash
# Prepares copies of html files. I will extract text from the copies.

rm -rf /tmp/lacourt_htmls/
rm -rf /tmp/lacourt_text/
# done
# rsync -av ~tent1/tent1/lacourt/htmls/2023*  /tmp/lacourt_htmls/
# rsync -av ~tent1/tent1/lacourt/htmls/2024*  /tmp/lacourt_htmls/
rsync -av tent1@d81:tent1/lacourt/htmls/2024* /tmp/lacourt_htmls/


# do this too [to create lacourt_file_list.txt]
cd ~/lx/lx14/public/
bash ~/lx/lx14/public/get_lacourt_file_list.bash

exit
