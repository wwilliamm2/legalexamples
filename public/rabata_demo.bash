#!/bin/bash

# ~/lx/lx14/public/rabata_demo.bash

echo $RABATASK
echo $RABATAKEY10
echo $RABATABUCKET

echo s3.rcs.rabata.io
echo s3.amazonaws.com

file=upload.tar.gz
bucket=$RABATABUCKET
resource="/${bucket}/${file}"
contentType="application/x-compressed-tar"
dateValue=`date -R`
stringToSign="PUT\n\n${contentType}\n${dateValue}\n${resource}"
s3Key=$RABATAKEY10
s3Secret=$RABATASK
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${s3Secret} -binary | base64`

/home/lc11/anaconda3/envs/lx12/bin/curl -X PUT -T "${file}" \
  -H "Host: ${bucket}.s3.rcs.rabata.io" \
  -H "Date: ${dateValue}" \
  -H "Content-Type: ${contentType}" \
  -H "Authorization: AWS ${s3Key}:${signature}" \
  https://${bucket}.s3.rcs.rabata.io/${file}

exit

# https://glacius.tmont.com/articles/uploading-to-s3-in-bash
# https://gist.github.com/chrismdp/6c6b6c825b07f680e710
# https://stackoverflow.com/questions/44751574/uploading-to-amazon-s3-via-curl-route
# s3.amazonaws.com == s3.rcs.rabata.io

# FAILS
