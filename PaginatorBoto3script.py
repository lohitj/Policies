#!/usr/bin/env python
import boto3
import xlwt
from xlwt import Workbook
# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'ETAG')
sheet1.write(0,1,'Key')
sheet1.write(0,2,'Metadata')
client = boto3.client('s3')
paginator = client.get_paginator('list_objects_v2').paginate(
        Bucket='elasticbeanstalk-ap-south-1-100931169541'
        )
i=1.0
for page in paginator:
    for objct in page['Contents']:
        response = client.get_object(
            Bucket='elasticbeanstalk-ap-south-1-100931169541',
            Key = objct['Key']
            )
        sheet1.write(int(i),0,objct['ETag'])
        sheet1.write(int(i),1,objct['Key'])
        sheet1.write(int(i),2,str(response['Metadata']))
        i = i+1
        if i==5000:
            break
        else:
            continue
wb.save("Etag3_example.xls")
