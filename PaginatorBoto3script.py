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
sheet1.write(0,3,'Size')
sheet1.write(0,4,'VersionId')
client = boto3.client('s3')
paginator = client.get_paginator('list_objects_v2').paginate(
        Bucket='elasticbeanstalk-ap-south-1-100931169541',
        PaginationConfig={'MaxItems': 20}
        )
i = 1.0
for page in paginator:
    for objct in page['Contents']:
        response = client.get_object(
            Bucket='elasticbeanstalk-ap-south-1-100931169541',
            Key = objct['Key']
            )
        print(response['VersionId'])
        sheet1.write(int(i),0,objct['ETag'])
        sheet1.write(int(i),1,objct['Key'])
        sheet1.write(int(i),2,str(response['Metadata']))
        sheet1.write(int(i),3,str(objct['Size']))
        sheet1.writte(int(i),4,response['VersionId'])
        print(objct['ETag'])
        print(objct['Key'])
        print(response['Metadata'])   
        i = i+1
wb.save("Etag3_example.xls")
