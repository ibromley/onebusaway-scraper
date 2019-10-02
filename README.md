# OneBusAway API Scraper

An AWS lambda function to retrieve bus arrival/departure information and store data in S3

## Quickstart

Create a new empty S3 bucket within AWS utilizing either the Quick Launch wizard, [AWS CLI](https://docs.aws.amazon.com/cli/index.html), or the various AWS SDKs (e.g. [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for python).

Update the credentials and configuration details in `api.cfg`. Change the S3 bucket location to the path you just created.

Peform the loading of the database tables by running the `scraper.py` script.

```
$ python scraper.py
```