import json
import os

with open('model-requirements.json') as file:
    temp = json.load(file)
    local = temp['model_ids']

with open('model-requirements-remote.json') as file:
    temp = json.load(file)
    remote = temp['model_ids']

diff = list(set(local) - set(remote))

for id in diff:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/checkpoints/"
    print(os.environ)
    print(command)
    #os.system(command)