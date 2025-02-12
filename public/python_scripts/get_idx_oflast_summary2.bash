#!/bin/bash

# get_idx_oflast_summary2.bash

# ls -ltr /home/dan/lx/jffj/lacourt/text/ | tail

# this is not working as I expect.

# maybe git will help
cd /home/dan/lx/jffj/lacourt/text/

# gpt, Please write ideas and syntax I can study during my efforts to ask git to list the most recent files committed to the git-repo. Thanks!

git log -n 1 --name-only

exit

(base) dan@hpsda6:~/lx/jffj/lacourt/text$ git log -n 1 --name-only
commit 409796c2b1260c1fb6e95aeaa186b7e6b327f262 (HEAD -> main, origin/main)
Author: Fred Tealyodeler <fred@fredt.edu>
Date:   Tue Feb 11 11:30:38 2025 -0800

    more

lacourt/text/2023_09_29_GLN_D/summary_08.txt
lacourt/text/2023_09_29_GLN_D/summary_09.txt
lacourt/text/2023_09_29_GLN_D/summary_10.txt

(base) dan@hpsda6:~/lx/jffj/lacourt/text$ grep -n 2023_09_18_ALH_3 /media/dan/ssd1/lx/legalexamples/public/python_scripts/tenttext_lacourt14.txt
1:/home/dan/lx/jffj/lacourt/text/2023_09_18_ALH_3/tent_ruling_01.txt
2:/home/dan/lx/jffj/lacourt/text/2023_09_18_ALH_3/tent_ruling_02.txt


(base) dan@hpsda6:~/lx/jffj/lacourt/text$ 
(base) dan@hpsda6:~/lx/jffj/lacourt/text$ grep -n 2023_09_29_GLN_D /media/dan/ssd1/lx/legalexamples/public/python_scripts/tenttext_lacourt14.txt
1572:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_01.txt
1573:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_02.txt
1574:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_03.txt
1575:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_04.txt
1576:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_05.txt
1577:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_06.txt
1578:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_07.txt
1579:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_08.txt
1580:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_09.txt
1581:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_10.txt
1582:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_11.txt
1583:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_12.txt
1584:/home/dan/lx/jffj/lacourt/text/2023_09_29_GLN_D/tent_ruling_13.txt
(base) dan@hpsda6:~/lx/jffj/lacourt/text$ 
(base) dan@hpsda6:~/lx/jffj/lacourt/text$ 
