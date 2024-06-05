#!/bin/bash

# public/py/tenttext_lacourt10.bash
# Prepares copies of html files. I will extract text from the copies.

rm -rf /tmp/lacourt_htmls/
rm -rf /tmp/lacourt_text/
rsync -av ~tent1/tent1/lacourt/htmls/ /tmp/lacourt_htmls/
exit
