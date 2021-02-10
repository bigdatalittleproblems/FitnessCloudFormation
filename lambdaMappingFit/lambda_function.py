import json
import boto3
import io
from fitparse import FitFile
import pandas as pd
import matplotlib.pyplot as plt
import os

def semicirclestolatlong(semicircles):
    x = semicircles * (180 / (2 ** 31))
    return x

def mappingFunc(x, objectname):
    x['position_lat_conversion'] = semicirclestolatlong(x['position_lat'])
    x['position_long_conversion'] = semicirclestolatlong(x['position_long'])
    plt.plot(x['position_long_conversion'], x['position_lat_conversion'])
    s3Key = objectname.split('/')[-1].replace('.csv', '.png')
    filename = '/tmp/' + s3Key
    plt.savefig(filename)
    return filename, s3Key


def lambda_handler(event, context):
    bucketname = event['Records'][0]['s3']['bucket']['name']
    objectname = event['Records'][0]['s3']['object']['key']
    s3 = boto3.resource('s3')
    obj = s3.Object(bucketname, objectname)
    body = obj.get()['Body'].read()
    df = pd.read_csv(io.BytesIO(body))
    if 'position_lat' in list(df.columns):
        fileName, objKey = mappingFunc(df, objectname)
    else:
        return {"statusCode": 200, "response": "No Location Data"}

    destKey = 'map/{}'.format(objKey)
    with open(fileName, 'rb') as file_obj:
        obj = s3.Object(bucketname, destKey)
        obj.put(Body=file_obj)
    return {"statusCode": 200, "response": {"bucket": bucketname, "key": destKey}}
