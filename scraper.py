import requests 
import configparser
import xml.etree.ElementTree as ET
import boto3

config = configparser.ConfigParser()
config.read('api.cfg')
AWS_KEY = config.get('AWS', 'KEY')
SECRET = config.get('AWS', 'SECRET')
API_KEY = config.get("OBA","API_KEY")
STOP_ID = config.get("OBA","STOP_ID")


url = 'http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/' + STOP_ID + '.xml?key=' + API_KEY

r = requests.get(url)
tree = ET.parse(r.text)
root = tree.getroot()

s3 = boto3.client('s3',
                    region_name="us-west-2",
                    aws_access_key_id=AWS_KEY,
                    aws_secret_access_key=SECRET
                    )
