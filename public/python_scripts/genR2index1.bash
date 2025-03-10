#!/bin/bash

# ~/lx/lx14/public/py/genR2index1.bash

# Generates a sorted list of cases in my R2 bucket.
# Generates a sorted list of pdf files in my R2 bucket.

# demo:
# conda activate r2
# bash ~/lx/lx14/public/py/genR2index1.bash | sort > /tmp/R2pdfs1.txt
# cp /tmp/R2cases1.txt ~/lx/lx14/public/
# cp /tmp/R2pdfs1.txt  ~/lx/lx14/public/

export RCLONE_CONFIG_R2_TYPE=s3
export RCLONE_CONFIG_R2_PROVIDER=Cloudflare
export RCLONE_CONFIG_R2_ACCESS_KEY_ID=$ACCESS_KEY_ID
export RCLONE_CONFIG_R2_SECRET_ACCESS_KEY=$SECRET_ACCESS_KEY
export RCLONE_CONFIG_R2_ENDPOINT=https://${ACCOUNT_ID}.r2.cloudflarestorage.com

rclone=~/anaconda3/envs/r2/bin/rclone

cd ~/lx/lx14/public/

$rclone lsf r2:2024-1209kv/ca/sacramento/cases/real_property/ | sort > /tmp/R2cases1.txt

for cn in `cat /tmp/R2cases1.txt`
do
    $rclone lsf r2:2024-1209kv/ca/sacramento/cases/real_property/$cn
done

r2prefix=https://lglx.org/ca/sacramento/cases/real_property/

exit

