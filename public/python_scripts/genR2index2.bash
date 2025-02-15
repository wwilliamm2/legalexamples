#!/bin/bash

# ~/lx/lx14/public/py/genR2index2.bash

# Generates a sorted list of cases     from my R2 bucket.
# Generates a sorted list of pdf files from my R2 bucket.

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

# dev only
#$rclone lsf r2:2024-1209kv/ca/sacramento/cases/real_property/ | grep 23CV000 > /tmp/R2cases1.txt
# dev only
r2p=r2:2024-1209kv/ca/sacramento/cases/real_property/
$rclone lsf $r2p | sort > /tmp/R2cases1.txt

rm -f /tmp/R2pdfs2.txt

for cn in `cat /tmp/R2cases1.txt`
do
    $rclone lsf ${r2p}${cn}|sed "s|^|$cn|">> /tmp/R2pdfs2.txt
done

r2prefix=https://lglx.org/ca/sacramento/cases/real_property/

rm -f /tmp/R2hrefs1.txt /tmp/R2hrefs2.html /tmp/R2hrefs_hr1.html

for pdf in `cat /tmp/R2pdfs2.txt`
do
    href=${r2prefix}${pdf}
    echo $href >> /tmp/R2hrefs1.txt
    echo '<a href="'${href}'">'${href}'</a>' >> /tmp/R2hrefs2.html
    echo '<a href="'${href}'" target="r2">'${href}'</a><hr />' >> /tmp/R2hrefs_hr1.html
done

cp /tmp/R2pdfs2.txt ~/lx/lx14/public/
cp /tmp/R2hrefs1.txt /tmp/R2hrefs2.html /tmp/R2hrefs_hr1.html ~/lx/lx14/public/
cat /tmp/R2hrefs_hr1.html > ~/lx/lx14/app/views/counties/_many_sacramento_pdfs.erb

exit

