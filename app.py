from flask import Flask, jsonify, request, url_for
from helper.eks_manager import EKSManager
import helper.aws_manager as aws_manager

app = Flask(__name__)

host_addr = "0.0.0.0"
port_num = "9999"
base_url = "/api/v1"


@app.route('{}/'.format(base_url))
def index():
    return 'Hello world'

@app.route('{}/aws'.format(base_url), methods = [ "POST" ])
def aws():
    profile = request.form['profile']
    region = request.form['region']
    aws_key = request.form['aws_key']
    aws_secret_key = request.form['aws_secret_key']
    result = aws_manager.aws_config(profile, region, aws_key, aws_secret_key)
    return jsonify({"result": result })

@app.route('{}/aws/s3'.format(base_url))
def aws_s3():
    return aws_manager.s3()


# @app.route('{}/eks/<name>'.format(base_url),  methods = ['GET', 'POST'])
# def eks(name):
#
#     cluster_name = name
#     eks = EKSManager(cluster_name)
#
#     if request.method == "GET":
#         print("GET : {}".format(name))
#         return jsonify(eks.getEKSInfo())
#     else:
#         print("POST : {}".format(name))
#         return jsonify({'cluster_name': eks.getClusterName()})


if __name__ == "__main__":
    app.run(host=host_addr, port=port_num)

