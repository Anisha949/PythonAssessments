#import the json package
import json

#reading the json file
with open("trial.json", "r") as read_file:
#loading the read file
    data = json.load(read_file)

print(data)

#output the desired query
print(data['Records'][0]['s3']['bucket']['arn'])


'''output:
arn:aws:s3:::mybucket
'''
