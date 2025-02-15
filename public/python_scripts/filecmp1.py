'''~/lx/lx14/public/py/filecmp1.py'''

'''
Creates a list of duplicate files to rm.

Demo:
Python -i filecmp1.py
'''

import glob, filecmp

fn1_s_l = sorted(glob.glob('/media/dan/ssd1/tmp/scscourt/pdfs/202*pdf'))

fn2_s_l = sorted(list(fn1_s_l))

matches_l = []
for fn1_s in fn1_s_l:
    for fn2_s in fn2_s_l:
        # Filter out redundant matches
        if fn1_s < fn2_s:
            if filecmp.cmp(fn1_s, fn2_s, shallow=False):
                matches_l.append([fn1_s, fn2_s])
# show the matches before I rm the dups
for match_s_l in matches_l:
    print('ls -l ', match_s_l[0], match_s_l[1])
print('exit')
dups_s_l = [fn_s_l[0] for fn_s_l in matches_l] # rm oldest
rm_these_l = sorted(list(set(dups_s_l)))
for fn_s in rm_these_l:
    print('rm ', fn_s)
