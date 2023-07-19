from huggingface_hub import snapshot_download


snapshot_download(repo_id="lmsys/vicuna-7b-delta-v0", 
                  cache_dir='/home/xiec/mm-agent/minigpt4-demo/pretrained/vicuna_weights/', 
                  allow_patterns="*.json, *.bin, *.model")

snapshot_download(repo_id="lmsys/vicuna-13b-delta-v0", 
                  cache_dir='/home/xiec/mm-agent/minigpt4-demo/pretrained/vicuna_weights/', 
                  allow_patterns="*.json, *.bin, *.model")
