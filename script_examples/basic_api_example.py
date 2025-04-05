import json
from urllib import request
import random
import os
import time

#This is the ComfyUI api prompt format.

#If you want it for a specific workflow you can "enable dev mode options"
#in the settings of the UI (gear beside the "Queue Size: ") this will enable
#a button on the UI to save workflows in api format.

#keep in mind ComfyUI is pre alpha software so this format will change a bit.

#this is the one for the default workflow

def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)

# Use this for local dev
#file_path = 'C:/Users/viet_/CodeProjects/aws-stablediffusion/script_examples/api_prompts/elf_dryad.json'

#Use this for AWS dev
file_path = '/home/ec2-user/aws-stablediffusion/script_examples/api_prompts/prompt.json'
batch_size = 40

with open(file_path, 'r') as file:
    prompt_text = file.read()
    prompt = json.loads(prompt_text)

    for iteration in range(batch_size):
        prompt["3"]["inputs"]["seed"] = random.randint(1,4294967294)
        queue_prompt(prompt)
