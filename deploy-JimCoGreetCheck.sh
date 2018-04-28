#!/usr/bin/env bash

aws lambda add-permission --function-name function:JimCoGreetCheck --statement-id 1 \
--principal connect.amazonaws.com  --action lambda:InvokeFunction --source-account 832433821903 \
--source-arn arn:aws:connect:us-east-1:832433821903:instance/148d3298-163b-4d8e-807b-b9b78b1a31ee \

git commit -a -m 'commiting'

rm JimCoGreetCheck.zip

zip -r JimCoGreetCheck.zip pymysql jimcodb.py lambda_function.py rds_config.py

aws lambda update-function-code \
--region us-east-1 \
--function-name   JimCoGreetCheck  \
--zip-file fileb://JimCoGreetCheck.zip
