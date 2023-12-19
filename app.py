#!/usr/bin/env python3

from aws_cdk import App
from bb_fnds.cdk_constructs import pipeline_forge
from cdk.stack import Stack

app = App()
for stack in pipeline_forge.Stack.from_env(app):
    Stack(stack)

app.synth()
