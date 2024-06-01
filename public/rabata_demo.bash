#!/bin/bash

# ~/lx/lx14/public/rabata_demo.bash

echo $RABATASK
echo $RABATAKEY10
echo $RABATABUCKET

echo s3.rcs.rabata.io

exit

file=/path/to/file/to/upload.tar.gz
bucket=your-bucket
resource="/${bucket}/${file}"
contentType="application/x-compressed-tar"
dateValue=`date -R`
stringToSign="PUT\n\n${contentType}\n${dateValue}\n${resource}"
s3Key=xxxxxxxxxxxxxxxxxxxx
s3Secret=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${s3Secret} -binary | base64`
curl -X PUT -T "${file}" \
  -H "Host: ${bucket}.s3.amazonaws.com" \
  -H "Date: ${dateValue}" \
  -H "Content-Type: ${contentType}" \
  -H "Authorization: AWS ${s3Key}:${signature}" \
  https://${bucket}.s3.amazonaws.com/${file}

# https://glacius.tmont.com/articles/uploading-to-s3-in-bash
# https://gist.github.com/chrismdp/6c6b6c825b07f680e710
# https://stackoverflow.com/questions/44751574/uploading-to-amazon-s3-via-curl-route

