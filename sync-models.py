import json
import os

#CLONE MODELS
with open('/aws-stablediffusion/model-requirements.json') as file:
    temp = json.load(file)
    local_models = temp['model_ids']
    local_clip = temp['clip_ids']
    local_clip_vision = temp['clip_vision_ids']
    local_configs = temp['configs_ids']
    local_controlnet = temp['controlnet_ids']
    local_diffusers = temp ['diffusers_ids']
    local_diffusion_models = temp['diffusion_model_ids']
    local_embeddings = temp['embeddings_ids'],
    local_gligen = temp['gligen_ids']
    local_hypernetworks = temp['hypernetworks_ids']
    local_loras = temp['loras_ids']
    local_photomaker = temp['photomaker_ids']
    local_style_models = temp['style_models_ids']
    local_text_encoders = temp['text_encoders_ids']
    local_unet = temp['unet_ids']
    local_upscale_models = temp['upscale_models_ids']
    local_vae = temp['vae_ids']
    local_vae_approx = temp['vae_approx_ids']

with open('/mnt/data/model-requirements-remote.json') as file:
    temp = json.load(file)
    remote = temp['model_ids']
    remote_models = temp['model_ids']
    remote_clip = temp['clip_ids']
    remote_clip_vision = temp['clip_vision_ids']
    remote_configs = temp['configs_ids']
    remote_controlnet = temp['controlnet_ids']
    remote_diffusers = temp ['diffusers_ids']
    remote_diffusion_models = temp['diffusion_model_ids']
    remote_embeddings = temp['embeddings_ids'],
    remote_gligen = temp['gligen_ids']
    remote_hypernetworks = temp['hypernetworks_ids']
    remote_loras = temp['loras_ids']
    remote_photomaker = temp['photomaker_ids']
    remote_style_models = temp['style_models_ids']
    remote_text_encoders = temp['text_encoders_ids']
    remote_unet = temp['unet_ids']
    remote_upscale_models = temp['upscale_models_ids']
    remote_vae = temp['vae_ids']
    remote_vae_approx = temp['vae_approx_ids']


diff1 = list(set(local_models) - set(remote_models))
diff2 = list(set(local_clip) - set(remote_clip))
diff3 = list(set(local_clip_vision) - set(remote_clip_vision))
diff4 = list(set(local_configs) - set(remote_configs))
diff5 = list(set(local_controlnet) - set(remote_controlnet))
diff6 = list(set(local_diffusers) - set(remote_diffusers))
diff7 = list(set(local_diffusion_models) - set(remote_diffusion_models))
diff8 = list(set(local_embeddings) - set(remote_embeddings))
diff9 = list(set(local_gligen) - set(remote_gligen))
diff10 = list(set(local_hypernetworks) - set(remote_hypernetworks))
diff11 = list(set(local_loras) - set(remote_loras))
diff12 = list(set(local_photomaker) - set(remote_photomaker))
diff13 = list(set(local_style_models) - set(remote_style_models))
diff14 = list(set(local_text_encoders) - set(remote_text_encoders))
diff15 = list(set(local_unet) - set(remote_unet))
diff16 = list(set(local_upscale_models) - set(remote_upscale_models))
diff17 = list(set(local_vae) - set(remote_vae))
diff18 = list(set(local_vae_approx) - set(remote_vae_approx))

for id in diff1:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/checkpoints/"
    os.system(command)
for id in diff2:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/clip/"
    os.system(command)
for id in diff3:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/clip_vision/"
    os.system(command)
for id in diff4:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/configs/"
    os.system(command)
for id in diff5:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/controlnet/"
    os.system(command)
for id in diff6:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/diffusers/"
    os.system(command)
for id in diff7:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/diffusion_models/"
    os.system(command)
for id in diff8:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/embeddings/"
    os.system(command)
for id in diff9:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/gligen/"
    os.system(command)
for id in diff10:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/hypernetworks/"
    os.system(command)
for id in diff11:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/loras/"
    os.system(command)
for id in diff12:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/photomaker/"
    os.system(command)
for id in diff13:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/style_models/"
    os.system(command)
for id in diff14:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/text_encoders/"
    os.system(command)
for id in diff15:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/unet/"
    os.system(command)
for id in diff16:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/upscale_models/"
    os.system(command)
for id in diff17:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/vae/"
    os.system(command)
for id in diff18:
    command = "wget \"civitai.com/api/download/models/" + str(id) + "?token=" + os.environ['CIVITAI_KEY'] + "\" --content-disposition -P /mnt/data/models/vae_approx/"
    os.system(command)


with open('/aws-stablediffusion/model-requirements.json') as file:
    overwrite = file.read()

f = open("/mnt/data/model-requirements-remote.json", "w")
f.write(overwrite)
f.close()
