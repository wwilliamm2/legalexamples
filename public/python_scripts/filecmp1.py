'''~/lx/lx14/public/py/filecmp1.py'''

'''
Creates a dictionary of keys which point to twins of the keys.

Demo:
Python -i filecmp1.py
'''

import glob, filecmp

fn1_s_l = glob.glob('/media/dan/ssd2/tmp/scscourt/pdfs/202*pdf')

fn2_s_l = list(fn1_s_l)

matches_l = []
for fn1_s in fn1_s_l:
    for fn2_s in fn2_s_l:
        if filecmp.cmp(fn1_s, fn2_s, shallow=False):
            # Filter out previous matches            
            if fn1_s < fn2_s:
                matches_l.append([fn1_s, fn2_s])
matches_l
for fn_s_l in matches_l:
    # rm the oldest file
    print('rm ',fn_s_l[0])
