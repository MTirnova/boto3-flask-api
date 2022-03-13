from flask import Flask, jsonify,request,make_response
import boto3
from config import config
import requests
import logging
app=Flask(__name__)
logging.basicConfig(
    filename=config['log_file'], 
    level=config['log_level']
)

@app.route("/ec2/list/",methods=['GET'])
def ec2_list():
    aws_access_key_id = request.args.get("aws_access_key_id")
    aws_secret_access_key = request.args.get("aws_secret_access_key")
    region_name = request.args.get("region_name")

    if (aws_access_key_id == None) or (aws_secret_access_key == None) or (region_name == None):
          return make_response(jsonify(Message="Eksik Parametre"), 400)

    client = boto3.client('ec2',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    response = client.describe_instances(
    )
    InstanceIds = []
    for instance in response["Reservations"][0]["Instances"]:
        InstanceIds.append(instance["InstanceId"])
        return make_response(jsonify(INSTANCEID=instance["InstanceId"]),200)

@app.route("/ec2/start/",methods=['GET'])
def ec2_start():
    aws_access_key_id = request.args.get("aws_access_key_id")
    aws_secret_access_key = request.args.get("aws_secret_access_key")
    region_name = request.args.get("region_name")
    InstanceId = request.args.get("InstanceId")

    if (aws_access_key_id == None) or (aws_secret_access_key == None) or (region_name == None) or (InstanceId == None):
          return make_response(jsonify(Message="Eksik Parametre"), 400)

    client = boto3.client('ec2',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    InstanceIds = InstanceId.split()
    response = client.describe_instances(
    )     
    response = client.start_instances(
    InstanceIds=InstanceIds
    )
    return make_response(jsonify(Message="Instance Basari ile Baslatildi"),200)


@app.route("/ec2/stop/",methods=['GET'])
def ec2_stop():
    aws_access_key_id = request.args.get("aws_access_key_id")
    aws_secret_access_key = request.args.get("aws_secret_access_key")
    region_name = request.args.get("region_name")
    InstanceId = request.args.get("InstanceId")

    if (aws_access_key_id == None) or (aws_secret_access_key == None) or (region_name == None) or (InstanceId == None):
          return make_response(jsonify(Message="Eksik Parametre"), 400)

    client = boto3.client('ec2',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    InstanceIds = InstanceId.split()
    response = client.describe_instances(
    )     
    response = client.stop_instances(
    InstanceIds=InstanceIds
    )
    return make_response(jsonify(Message="Instance Basari ile Durduruldu"),200)
    #
if __name__=="__main__":
    app.run(host=config["host"], port=config["port"], debug=True)