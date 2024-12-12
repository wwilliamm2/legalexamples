#!/bin/bash

# ~/lx/lx14/public/py/genR2index2.bash

# Generates a sorted list of cases     in my R2 bucket.
# Generates a sorted list of pdf files in my R2 bucket.

# demo:
# conda activate r2
# bash ~/lx/lx14/public/py/genR2index2.bash

export RCLONE_CONFIG_R2_TYPE=s3
export RCLONE_CONFIG_R2_PROVIDER=Cloudflare
export RCLONE_CONFIG_R2_ACCESS_KEY_ID=$ACCESS_KEY_ID
export RCLONE_CONFIG_R2_SECRET_ACCESS_KEY=$SECRET_ACCESS_KEY
export RCLONE_CONFIG_R2_ENDPOINT=https://${ACCOUNT_ID}.r2.cloudflarestorage.com

rclone=~/anaconda3/envs/r2/bin/rclone

cd ~/lx/lx14/public/

# $rclone lsf r2:2024-1209kv/ca/sacramento/cases/real_property/ | sort > /tmp/R2cases1.txt

# dev only
$rclone lsf r2:2024-1209kv/ca/sacramento/cases/real_property/ | grep 23CV000 > /tmp/R2cases1.txt
# dev only

rm -f /tmp/R2pdfs2.txt
for cn in `cat /tmp/R2cases1.txt`
do
    r2p=r2:2024-1209kv/ca/sacramento/cases/real_property/
    $rclone lsf ${r2p}${cn}|sed "s|^|$cn|">> /tmp/R2pdfs2.txt
done

r2prefix=https://lglx.org/ca/sacramento/cases/real_property/

rm -f /tmp/R2hrefs1.txt /tmp/R2hrefs2.txt

for pdf in `cat /tmp/R2pdfs2.txt`
do
    href=${r2prefix}${pdf}
    echo $href >> /tmp/R2hrefs1.txt
    echo '<a href="'${href}'">'${href}'</a>' >> /tmp/R2hrefs2.txt
done

exit

