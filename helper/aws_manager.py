import boto3
import os
import pathlib

def aws_config(profile, region, aws_access_key_id, aws_secret_access_key):

    result = True

    try:
        credentials = '{}/.aws/credentials'.format(pathlib.Path.home())
        config = '{}/.aws/config'.format(pathlib.Path.home())

        # credentials
        f = open(credentials, "w+")
        f.write('[{}]\n'.format(profile))
        f.write('aws_access_key_id = {}\n'.format(aws_access_key_id))
        f.write('aws_secret_access_key = {}\n'.format(aws_secret_access_key))
        f.flush()
        f.close()

        # config
        f = open(config, "w+")
        f.write('[profile {}]\n'.format(profile))
        f.write('output = json\n')
        f.write('region = {}\n'.format(region))
        f.flush()
        f.close()

        boto3.setup_default_session(profile_name=profile)
    except Exception as e:
        print(e)
        result = False

    return result


def s3():
    print('---------- 05 ----------')

    s3 = boto3.resource('s3')
    list = []
    for bucket in s3.buckets.all():
        list.append(bucket.name)
    return ','.join(list)