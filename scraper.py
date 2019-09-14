import requests 
import configparser
import boto3
from datetime import datetime

# XML -> JSON parsing
from xmljson import parker as bf
from xml.etree.ElementTree import fromstring
from json import dumps

# Read configuration item
config = configparser.ConfigParser()
config.read('api.cfg')
AWS_KEY = config.get('AWS', 'KEY')
SECRET = config.get('AWS', 'SECRET')
BUCKET = config.get('AWS', 'BUCKET')
API_KEY = config.get("OBA","API_KEY")
STOP_ID = config.get("OBA","STOP_ID")


url = 'http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/' + STOP_ID + '.xml?key=' + API_KEY

r = requests.get(url)

s3 = boto3.client('s3',
                    region_name="us-west-2",
                    aws_access_key_id=AWS_KEY,
                    aws_secret_access_key=SECRET
                    )

json_object = dumps(bf.data(fromstring(r.text)))

object_name = STOP_ID + '/' + datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.json'

s3.put_object(Body=json_object, Bucket=BUCKET, Key=object_name)