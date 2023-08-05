"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import json


class BaseEC2:

    params = {
        "resource_name": "test-ec2",
        "instance_type": "t3a.micro"
    }

    def __init__(self, ami, vpc, **kwargs): 
        self.variable_reassignment(**kwargs)
        self.params["subnet_id"] = vpc.instance.private_subnet_ids.apply(lambda id: id[0])
        self.params["ami"] = ami
        self.create_ec2()

    def variable_reassignment(self, **kwargs):
        for key in kwargs:
            if key in self.params:
                self.params[key] = kwargs[key]
            else:
                print("hey this is probably an issue you should address")

    def create_ec2(self):
        # Create an AWS resource (ec2)
        main = aws.ec2.Instance(**self.params)