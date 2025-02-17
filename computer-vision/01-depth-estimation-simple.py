# Simple Depth Estimation with Hugging Face

# Provide your HF access token in the HF_TOKEN variable.
# 
# Note that when you run this script, it will download the model to your machine,
# which can be many GB.
#
# The result is a PNG image saved to disk, the name of which is specified in 
# the .save() method.

from transformers import pipeline

HF_TOKEN = ""

bee_flower = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"
model = "depth-anything/Depth-Anything-V2-base-hf"  # ≈390MB

estimator = pipeline(task="depth-estimation", model=model, token=HF_TOKEN)
result = estimator(images=bee_flower)
result["depth"].save("depth-bee-flower.png")
