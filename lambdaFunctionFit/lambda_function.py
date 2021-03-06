import json
import boto3
from fitparse import FitFile
import pandas as pd
import os
destBucket = os.environ['Dest_Bucket']
def fit_parse(fitDir):
    fitfile = FitFile(fitDir)
    dataOutput={}
    workout = []
    messageFit=['activity','file_id','session','lap','record','device_info','event','segment_lap']
    for j in messageFit:
        try: 
            workout = []
            for records in fitfile.get_messages(j):
                r = {}
                for record_data in records:
                    r[record_data.name] = record_data.value
                    try:
                        workout.append(r)
                        dataOutput.update({j:workout})
                    except Exception as ex:
                        pass
            workout=pd.DataFrame(dataOutput[j])
            workout.drop_duplicates(inplace=True)
            dataOutput.update({j:workout})
        except:
            pass
    output=json.dumps({i:dataOutput[i].to_csv(index=False) for i in dataOutput})
    return output
def lambda_handler(event, context):
    bucketname=event['Records'][0]['s3']['bucket']['name']
    objectname=event['Records'][0]['s3']['object']['key']
    s3 = boto3.resource('s3')
    obj = s3.Object(bucketname, objectname)
    body = obj.get()['Body'].read()
    responseData = fit_parse(body)
    objectname.split('/')[-1]
    x=json.loads(responseData)
    finalObjName=objectname.split('/')[-1].replace('.fit','.csv')
    activityName=objectname.split('/')[-1].replace('.fit','')
    dataDestKey={'key':{"S":activityName},'bucket':{"S":destBucket}}
    for i in x:
        destKey=f"{i}/{finalObjName}"
        print(destKey)
        obj = s3.Object(destBucket,destKey)
        obj.put(Body=x[i])
        dataDestKey[i]={"S":destKey}
    print(dataDestKey)
    return {"statusCode": 200,"response":dataDestKey}