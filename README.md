# llama-vicuna-pre


## install fastchat

`pip install git+https://github.com/lm-sys/FastChat.git@v0.1.10`

## vicuna-delta-vo

`python3 -m fastchat.model.apply_delta --base ~/mm-agent/pretrained_models/LLaMA/7B-HF/ --target ~/mm-agent/pretrained_models/vicuna_working_weights/vicuna-7b-v0 --delta lmsys/vicuna-7b-delta-v0
`
