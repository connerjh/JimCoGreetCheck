#!/usr/bin/env bash

git commit -a -m 'commiting'

rm JimCoGreetCheck.zip

zip -r JimCoGreetCheck.zip pymysql jimcodb.py lambda_function.py rds_config.py

aws lambda update-function-code \
--region us-east-1 \
--function-name   JimCoGreetCheck  \
--zip-file fileb://JimCoGreetCheck.zip
